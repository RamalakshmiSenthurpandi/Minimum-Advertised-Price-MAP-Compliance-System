def load_pl_table(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def load_sku_xml(path):
    root = ET.parse(path).getroot()
    return {item.find("Sku").text: item.find("PN").text for item in root}
