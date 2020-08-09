import requests
import re
import time


def drop_table(string):
    if "<table" in string:
        string = string[:string.index("<table")] + string[string.index("</table>"):]
    if "<table" in string:
        string = string[:string.index("<table")] + string[string.index("</table>"):]

    if "<span" in string:
        string = string[:string.index("<span")] + string[string.index("</span>"):]

    return string


def get_link(ur):
    source = requests.get(ur)

    name = str(source.url).split("/")[-1].replace('_', " ")

    if name == "Philosophy":
        print(name)
        print("We found Philosophy")
        return 1

    if name in visited:
        print(name)
        print("Error: No Philosophy found. (Looping.)")
        return 0

    visited.append(name)
    print(name)

    source = str(source.content)
    source = re.findall("<p>.*", source)[0]
    source = drop_table(source)

    source2 = re.findall("href=\"/wiki/[a-zA-Z_,-?$()]+\" title=\"[a-z A-Z_]+\">[a-zA-Z_ ]+</a>", source)

    if len(source2) == 0:
        print("Error: No Philosophy found. (No more links.)")
        return 0;

    time.sleep(0.6)

    the_link = ""
    for link in source2:

        if source[source.index(link) - 4] == '(':
            continue
        else:
            the_link = link
            break

    the_link = "https://en.wikipedia.org" + the_link[6:the_link.index("title=") - 2]
    get_link(the_link)


url = 'https://en.wikipedia.org/wiki/Special:Random'
visited = []

get_link(url)

"""count = 0;
for i in range(100):
  num = get_link(url)
     if num is None:
      count = count + 0
            else:
      count = count + 1
  visited = []
print(count)"""
