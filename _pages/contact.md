---
title: Contact Me
layout: page
permalink: /contact/
---

<!-- modify this form HTML and place wherever you want your form -->

<form
  action="{{site.data.settings.formspree-action}}"
  method="POST"
>
	<div class="grid gap-4">

  <label>
    Your email:  </label>
    <input class="border py-2 px-3 text-grey-darkest rounded" type="text" name="_replyto">

  <label>
    Your message:  </label>
    <textarea class="border py-2 px-3 text-grey-darkest rounded" name="message"></textarea>

  <!-- your other form fields go here -->

<button class="px-4 py-3 rounded text-center text-white bg-green-500 hover:bg-green-400" type="submit">Send</button>

</div>

</form>
