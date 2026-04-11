from flask import Flask, render_template_string
import feedparser

app = Flask(__name__)

# RSS feeds 

FEEDS = {
    "BBC News": "https://feeds.bbci.co.uk/news/uk/rss.xml",
    "The Guardian": "https://www.theguardian.com/uk-news/rss",
    "Sky News": "https://feeds.skynews.com/feeds/rss/home.xml",
    "Independent": "https://www.independent.co.uk/rss"
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My News Feed</title>

<link rel="icon" type="image/png" href="{{ url_for('static', filename='icon.png') }}">
    
    <style>
        body { font-family: sans-serif; padding: 20px; background: #f4f4f9; }
        .story { background: white; padding: 15px; margin-bottom: 10px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        a { text-decoration: none; color: #007bff; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Latest Stories</h1>
    {% for source, url in feeds.items() %}
        <h2>{{ source }}</h2>
        {% set entries = get_feed(url) %}
        {% for entry in entries[:5] %}
            <div class="story">
                <a href="{{ entry.link }}">{{ entry.title }}</a>
            </div>
        {% endfor %}
    {% endfor %}
</body>
</html>
"""

def get_feed(url):
    return feedparser.parse(url).entries

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, feeds=FEEDS, get_feed=get_feed)

if __name__ == "__main__":
    app.run()
  
