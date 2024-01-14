"""
wiki introduction
"""

import wikipedia

search_phrase = input("What do you want to search? ")
try:
    page = wikipedia.page(search_phrase)
    print(f"title: {page.title}\nsummary: {wikipedia.summary(search_phrase)}\nurl: {page.url}")
except wikipedia.exceptions.DisambiguationError as e:
    print(e.options)

