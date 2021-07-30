import re
import os
import exif
from PIL import Image
from dotenv import load_dotenv
load_dotenv(verbose=True)

thumb = input('Generate thumbnails? (y/n): ')
overwrite_thumb = 'n'
if thumb == 'y': overwrite_thumb = input('Overwrite existing thumbnails? (y/n): ')
  
overwrite_markdown = input('Overwrite existing markdowns? (y/n): ')

with open('photo_template.md', encoding='utf8') as f:
  template = f.read()

print()

result = { "total": 0, "thumbnail": 0, "markdown": 0, "error": 0, "skipped": 0 }
  
for i, photo in enumerate(os.scandir(os.path.join(os.getcwd(), 'photos'))):
  result['total'] += 1
  if photo.is_dir():
    result['skipped'] += 1
    print(i + 1, '/', len(os.listdir(os.path.join(os.getcwd(), 'photos'))), ' folder:', os.path.basename(photo))
    continue
  with open(os.path.join(os.getcwd(), 'photos', photo), 'rb') as f:
    md = template
    img = exif.Image(f)
    [ filename, ext ] = os.path.basename(f.name).rsplit('.', 1)
    print(i + 1, '/', len(os.listdir(os.path.join(os.getcwd(), 'photos'))), ' file:', filename + '.' + ext, end='')

    try:
      if overwrite_markdown == 'y' or not os.path.isfile(os.path.join(os.getcwd(), '../../_photos', filename + '.md')):
        md = re.sub('##name##', os.path.basename(f.name), md)
        md = re.sub('##thumbnail##', filename + '_thumbnail.' + ext, md)
        md = re.sub('##date##', img.datetime_original[:img.datetime_original.index(' ')].replace(':', '-'), md)
        md = re.sub('##camera##', img.model if hasattr(img, 'model') else 'N/A', md)
        md = re.sub('##lens##', img.lens_model if hasattr(img, 'lens_model') else 'N/A', md)
        md = re.sub('##aperture##', str(img.f_number) if hasattr(img, 'f_number') else 'N/A', md)
      
        if hasattr(img, 'exposure_time'):
          md = re.sub('##shutter##', str(img.exposure_time if img.exposure_time >= 1 else '1/'+ str(round(1 / img.exposure_time))), md)
        else:
          md = re.sub('##shutter##', 'N/A', md)
        
        md = re.sub('##iso##', str(img.photographic_sensitivity) if hasattr(img, 'photographic_sensitivity') else 'N/A', md)
        md = re.sub('##focal##', str(img.focal_length) if hasattr(img, 'focal_length') else 'N/A', md)
        md = re.sub('##exposure##', str(round(img.exposure_bias_value, 3)) if hasattr(img, 'exposure_bias_value') else 'N/A', md)

        if hasattr(img, 'flash') and img.flash.flash_fired:
          md = re.sub('##flash##', 'flash on', md)
          md = re.sub('##flashicon##', 'flash-on', md)
        else:
          md = re.sub('##flash##', 'flash off', md)
          md = re.sub('##flashicon##', 'flash-off', md)

        md = re.sub('##datetime##', img.datetime_original.replace(':', '-', 2), md)
      
        if hasattr(img, 'gps_latitude'):
          GoogleMapsEmbedApiToken = os.getenv('GoogleMapsEmbedApiToken')
          map = img.gps_map_datum if hasattr(img, 'gps_map_datum') else ''
          md = re.sub('##location##', f'{map} {round(img.gps_latitude[0] + img.gps_latitude[1] / 60, 6)}{img.gps_latitude_ref}, {round(img.gps_longitude[0] + img.gps_longitude[1] / 60, 6)}{img.gps_longitude_ref} Δ{img.gps_altitude}m  \n<iframe src="https://www.google.com/maps/embed/v1/place?key={GoogleMapsEmbedApiToken}&zoom=17&q={img.gps_latitude[0] + img.gps_latitude[1] / 60},{img.gps_longitude[0] + img.gps_longitude[1] / 60}&center={img.gps_latitude[0] + img.gps_latitude[1] / 60},{img.gps_longitude[0] + img.gps_longitude[1] / 60}" frameborder="0" style="width: 80%; max-width:400px; height: 300px; margin: -1rem 0 1rem 50px; border: 0;"></iframe>', md)
        else:
          md = re.sub('##location##', 'N/A', md)
        
        md = re.sub('##size##', str(round(os.path.getsize(f.name) / (1024 * 1024), 1)), md)

      if thumb == 'y':
        if overwrite_thumb == 'y' or not os.path.isfile(os.path.join(os.getcwd(), 'photos', 'thumbnails', filename + '_thumbnail.' + ext)):
          image = Image.open(os.path.join(os.getcwd(), 'photos', photo))
          image.thumbnail((1000, 1000), Image.ANTIALIAS)
          image.save(os.path.join(os.getcwd(), 'photos', 'thumbnails', filename + '_thumbnail.' + ext))
          print(' thumbnail: O', end='')
          result['thumbnail'] += 1
        else: print(' thumbnail: X', end='')
      else: print(' thumbnail: X', end='')
            

    except Exception as e:
      print(' error')
      result['error'] += 1
      print(e)
      continue
      
    if overwrite_markdown == 'y' or not os.path.isfile(os.path.join(os.getcwd(), '../../_photos', filename + '.md')):
      with open(os.path.join(os.getcwd(), '../../_photos', filename + '.md'), 'w', encoding='utf8') as markdown:
        markdown.write(md)
        print(' markdown: O', end='')
        result['markdown'] += 1
    else: print(' markdown: X', end='')

    print()

print('RESULT: total: ', result['total'])
print('  markdown generation: ', result['markdown'])
print('  thumbnail generation: ', result['thumbnail'])
print('  error: ', result['error'])
print('  skipped: ', result['skipped'])