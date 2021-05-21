# MSFS Blog RSS Feed
[![Update RSS feed](https://github.com/evroon/msfs-rss/actions/workflows/update_feed.yaml/badge.svg)](https://github.com/evroon/msfs-rss/actions/workflows/update_feed.yaml)

RSS feed for the MSFS blog: https://www.flightsimulator.com.

The RSS feed URL is: https://raw.githubusercontent.com/evroon/msfs-rss/main/atom.xml, which you can add to your favorite RSS reader. Github Actions updates the RSS feed at 18:00 UTC every day.

## Usage
The Python script can be run by first installing the dependencies:

```bash
python3 -m pip install -r requirements.txt
```

And simply running the Python script:
```bash
python3 main.py
```
