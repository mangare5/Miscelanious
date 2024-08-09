import xml.etree.ElementTree as ET

def convert_tmx_to_xlf(tmx_file, xlf_file):
    # Parse the TMX file with namespace support
    tree = ET.parse(tmx_file)
    root = tree.getroot()

    # Define the namespace map
    namespaces = {'xml': 'http://www.w3.org/XML/1998/namespace'}

    # Create the XLF structure
    xliff = ET.Element("xliff", version="1.2")
    file_elem = ET.SubElement(xliff, "file", {
        "source-language": "en-US",
        "target-language": "es-ES",
        "datatype": "plaintext",
        "original": tmx_file
    })
    body = ET.SubElement(file_elem, "body")
    
    # Iterate over translation units in TMX
    for tu in root.findall(".//tu"):
        trans_unit = ET.SubElement(body, "trans-unit", id=tu.get("tuid", ""))
        source_text = tu.find(".//tuv[@xml:lang='en-US']/seg", namespaces)
        target_text = tu.find(".//tuv[@xml:lang='es-ES']/seg", namespaces)

        if source_text is not None and target_text is not None:
            source = ET.SubElement(trans_unit, "source")
            target = ET.SubElement(trans_unit, "target")
            source.text = source_text.text
            target.text = target_text.text
        else:
            print(f"Warning: Could not find source or target for TU ID: {tu.get('tuid')}")

    # Write out XLF
    tree = ET.ElementTree(xliff)
    tree.write(xlf_file, encoding="utf-8", xml_declaration=True)

# Example usage:
convert_tmx_to_xlf("Align_test_EN-ES.tmx", "output.xlf")
