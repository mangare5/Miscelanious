This script converts tmx into xlf.
You only need to replace the languages:
source_text = tu.find(".//tuv[@lang='en']/seg")
target_text = tu.find(".//tuv[@lang='fr']/seg")

And specify your tmx name.
