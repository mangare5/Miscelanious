This script converts tmx into xlf.<br>
You only need to replace the languages:<br>
source_text = tu.find(".//tuv[@lang='en']/seg")<br>
target_text = tu.find(".//tuv[@lang='fr']/seg")<br>
<br><br>
And specify your tmx name.
