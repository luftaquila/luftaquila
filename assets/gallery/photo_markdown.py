import re
import os
import exif
from PIL import Image
from fractions import Fraction
from decimal import Decimal

with open('photo_template.md', encoding='utf8') as f:
  template = f.read()

for photo in os.listdir(os.path.join(os.getcwd(), 'photos')):
  with open(os.path.join(os.getcwd(), 'photos', photo), 'rb') as f:
    md = template
    img = exif.Image(f)
    [ filename, ext ] = os.path.basename(f.name).rsplit('.', 1)

    md = re.sub('##name##', os.path.basename(f.name), md)
    md = re.sub('##thumbnail##', filename + '_thumbnail.' + ext, md)
    md = re.sub('##date##', img.datetime_original[:img.datetime_original.index(' ')].replace(':', '-'), md)
    md = re.sub('##camera##', img.model, md)
    md = re.sub('##lens##', img.lens_model, md)
    md = re.sub('##aperture##', str(img.f_number), md)
    md = re.sub('##shutter##', str(Fraction(Decimal(str(img.exposure_time)))), md)
    md = re.sub('##iso##', str(img.photographic_sensitivity), md)
    md = re.sub('##focal##', str(img.focal_length), md)
    md = re.sub('##exposure##', str(img.exposure_bias_value), md)

    if img.flash.flash_fired:
      md = re.sub('##flash##', 'flash on', md)
      md = re.sub('##flashicon##', 'flash-on', md)
    else:
      md = re.sub('##flash##', 'flash off', md)
      md = re.sub('##flashicon##', 'flash-off', md)

    md = re.sub('##datetime##', img.datetime_original.replace(':', '-', 2), md)
    md = re.sub('##location##', '', md)
    md = re.sub('##size##', str(round(os.path.getsize(f.name) / (1024 * 1024), 1)), md)

    image = Image.open(os.path.join(os.getcwd(), 'photos', photo))
    image.thumbnail((1000, 1000), Image.ANTIALIAS)
    image.save(os.path.join(os.getcwd(), 'thumbnails', filename + '_thumbnail.' + ext))

    with open(os.path.join(os.getcwd(), 'markdowns', filename + '.md'), 'w', encoding='utf8') as markdown:
        markdown.write(md)
