from bs4 import BeautifulSoup
import requests
from feedgen.feed import FeedGenerator
from datetime import datetime
from typing_util import assert_some, assert_type

main_url = "https://www.flightsimulator.com"
rss_url = "https://raw.githubusercontent.com/evroon/msfs-rss/main/feeds/msfs.xml"

# Initialize RSS feed.
fg = FeedGenerator()
fg.id(main_url)
fg.title("MSFS Blog")
fg.subtitle("Development updates of Microsoft Flight Simulator.")
fg.link(href=main_url, rel="alternate")
fg.logo("https://msfs-cdn.azureedge.net/wp-content/uploads/2020/03/msf-logo.png")
fg.link(href=rss_url, rel="self")
fg.language("en")

page = requests.get(main_url)
soup = BeautifulSoup(page.text, "html.parser")
posts = soup.find_all(class_="post")


# Add blog post entries to feed.
for post in posts:
    header = assert_some(post.find(class_="entry-title"))
    summary = assert_some(post.find(class_="entry-summary"))
    meta = assert_some(post.find(class_="entry-meta"))
    image = post.find(class_="img-fluid")

    title = header.text.strip()
    url = assert_some(header.find("a"))["href"]
    body = summary.text.strip()

    time = assert_some(meta.find("time"))
    date = datetime.fromisoformat(assert_type(time.get("datetime"), str))

    fe = fg.add_entry()
    fe.id(url)
    fe.title(title)
    fe.link(href=url)
    fe.pubDate(date)
    fe.updated(date)
    fe.summary(body)

    if image is not None:
        enclosure = assert_type(image["src"], str)
        img_headers = requests.head(enclosure).headers
        fe.enclosure(
            enclosure, img_headers["content-length"], img_headers["content-type"]
        )

fg.atom_file("feeds/msfs.xml", pretty=True)
