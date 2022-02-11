import pytz
from bs4 import BeautifulSoup
import requests
from feedgen.feed import FeedGenerator
from datetime import datetime

main_url = 'https://www.thresholdx.net/news'
rss_url = 'https://raw.githubusercontent.com/evroon/msfs-rss/main/feeds/threshold.xml'

# Initialize RSS feed.
fg = FeedGenerator()
fg.id(main_url)
fg.title('Thresholdx blog')
fg.subtitle('News about flight simulators.')
fg.link(href=main_url, rel='alternate')
fg.logo('https://assets-global.website-files.com/5b27a494dc3d3103abc01d83/5f2387c90e9e1dca5453fc23_web1.png')
fg.link(href=rss_url, rel='self')
fg.language('en')

page = requests.get(main_url)
soup = BeautifulSoup(page.text, 'html.parser')
posts = soup.find_all(class_='w-dyn-item')


# Add blog post entries to feed.
for post in posts:
    if post.find(class_='frontpage') or not post.find(class_='t-invert'):
        continue

    title = post.find(class_='t-invert').text
    sim_tags = post.find(class_='flexh').find_all('div')
    sim_tag = [tag for tag in sim_tags if 'w-condition-invisible' not in tag['class']][0].text

    image = post.find('img')
    url = post.find('a')['href']
    date = datetime.strptime(post.find(class_='vsp').text, '%b %d, %Y').astimezone(pytz.UTC)

    body_response = requests.get(main_url.rstrip('/news') + url)
    summary = f'Sim: {sim_tag}'

    if body_response.ok:
        soup = BeautifulSoup(body_response.text, 'html.parser')
        paragraphs = soup.find(class_='w-richtext').find_all('p')
        summary += '. ' + ' '.join([p.text for p in paragraphs])

    fe = fg.add_entry()
    fe.id(url)
    fe.title(title)
    fe.link(href=url)
    fe.pubDate(date)
    fe.updated(date)
    fe.summary(summary)

    if image is not None:
        enclosure = image['src']
        img_headers = requests.head(enclosure).headers
        fe.enclosure(enclosure, img_headers['content-length'], img_headers['content-type'])

fg.atom_file('feeds/thresholdx.xml', pretty=True)
