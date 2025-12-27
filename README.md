# Flight simulator RSS Feeds
[![Update RSS feeds](https://github.com/evroon/msfs-rss/actions/workflows/update_feed.yaml/badge.svg)](https://github.com/evroon/msfs-rss/actions/workflows/update_feed.yaml)

RSS feed for:
* [MSFS blog](https://www.flightsimulator.com): https://raw.githubusercontent.com/evroon/msfs-rss/main/feeds/msfs.xml
* [Thresholdx](https://www.thresholdx.net/news): https://raw.githubusercontent.com/evroon/msfs-rss/main/feeds/thresholdx.xml

You can add these RSS feeds to your favorite RSS reader. Github Actions updates the RSS feeds at 18:00 UTC every day.

## Usage
The Python script can be run by simply running one of the Python scripts:
```bash
uv run src/msfs.py
```
