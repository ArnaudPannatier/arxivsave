import argparse
import xml.etree.ElementTree as ET
from io import StringIO
from pathlib import Path

import requests


def get_et(xml):
    it = ET.iterparse(StringIO(xml))
    for _, el in it:
        _, has_namespace, postfix = el.tag.rpartition('}')
        if has_namespace:
            el.tag = postfix  # strip all namespaces
    return it.root

def query_article(id):
    params = {"id_list": id}
    res = requests.get("https://export.arxiv.org/api/query", params=params)
    return res.text

def url_pdf(id):
    return "https://arxiv.org/pdf/{}.pdf".format(id)

def save_pdf(title,id):
    res = requests.get(url_pdf(id))
    path = Path.home() / "Documents" / "arxiv" / f"{title}.pdf"
    with path.open("ab") as f:
        f.write(res.content)

def save(id=None):
    if id is None:
        parser = argparse.ArgumentParser()
        parser.add_argument("id", type=str)
        args = parser.parse_args()
        id = args.id

    tree = get_et(query_article(id))
    title = tree.find("entry").find("title").text

    save_pdf(title.replace(" ", "-").replace("\n","").replace("--", "-").lower(),id)


