import json, webbrowser

def GET(name, tld):
    with open("connections.json") as file:
        o = json.load(file)
        for website in o:
            if website == f"{name}.{tld}":
                webbrowser.open(o[website]["source"])