# Build another Hacker News (https://news.ycombinator.com/news) using web scraping
# Show stories that has over 100 points of votes from highest to lowest in the terminal
# Usage: 'python3 scrape-hn.py [pages_you_want_to_read]'

import sys
import requests
from bs4 import BeautifulSoup
import pprint

pages = int(sys.argv[1])


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def append_stories_over_100_points(links, subtext, hn):
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)

        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'title': title, 'link': href,
                          'votes': points})


def create_custom_hn(pages):
    hn = []

    for page in range(1, pages + 1):
        res = requests.get(f'https://news.ycombinator.com/news?p={page}')
        soup = BeautifulSoup(res.text, 'html.parser')

        links = soup.select('.storylink')
        subtext = soup.select('.subtext')

        append_stories_over_100_points(links, subtext, hn)

    return sort_stories_by_votes(hn)


if __name__ == '__main__':
    pprint.pprint(create_custom_hn(pages))
