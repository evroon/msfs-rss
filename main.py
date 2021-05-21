from bs4 import BeautifulSoup
import requests
from feedgen.feed import FeedGenerator
from datetime import datetime

main_url = 'https://www.flightsimulator.com'
rss_url = 'https://raw.githubusercontent.com/evroon/msfs-rss/main/atom.xml'

# Initialize RSS feed.
fg = FeedGenerator()
fg.id(main_url)
fg.title('MSFS Blog')
fg.subtitle('Development updates of Microsoft Flight Simulator.')
fg.link(href=main_url, rel='alternate')
fg.logo('https://msfs-cdn.azureedge.net/wp-content/uploads/2020/03/msf-logo.png')
fg.link(href=rss_url, rel='self')
fg.language('en')

page = requests.get(main_url)
soup = BeautifulSoup(page.text, 'html.parser')
posts = soup.find_all(class_='post')

# Add blog post entries to feed.
for post in posts:
    header = post.find(class_='entry-title')
    summary = post.find(class_='entry-summary')
    meta = post.find(class_='entry-meta')
    image = post.find(class_='img-fluid')

    title = header.text.strip()
    url = header.find('a')['href']
    body = summary.text.strip()
    date = datetime.fromisoformat(meta.find('time')['datetime'])
    enclosure = image['src']

    fe = fg.add_entry()
    fe.id(url)
    fe.title(title)
    fe.link(href=url)
    fe.pubDate(date)
    fe.summary(body)
    fe.enclosure(enclosure)

fg.atom_file('atom.xml')
