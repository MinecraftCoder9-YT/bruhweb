import json, requests

def GET(name, tld):
    with open("connections.json") as file:
        o = json.load(file)
        for website in o:
            if website == f"{name}.{tld}":
                page = requests.get(o[website]["source"])
                return page.text