from flask import Flask, render_template_string, url_for
import feedparser

app = Flask(__name__)

# RSS feeds 
FEEDS = {
    "BBC News": "https://feeds.bbci.co.uk/news/uk/rss.xml",
    "BBC Lincs": "https://feeds.bbci.co.uk/news/england/lincolnshire/rss.xml",
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
    
    <link rel="icon" type="image/png" href="{{ url_for('static', filename='1775855183417.png') }}">
    <link rel="apple-touch-icon" href="{{ url_for('static', filename='1775855183417.png') }}">
    
    <style>
        body { font-family: sans-serif; padding: 20px; background: #f4f4f9; color: #333; }
        .story { background: white; padding: 15px; margin-bottom: 12px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        a { text-decoration: none; color: #007bff; font-weight: bold; font-size: 1.1em; }
        h1 { color: #222; border-bottom: 2px solid #007bff; padding-bottom: 10px; }
        h2 { color: #555; margin-top: 30px; font-size: 1.2em; text-transform: uppercase; letter-spacing: 1px; }
    </style>
</head>
<body>
    <h1>My News</h1>
    {% for source, url in feeds.items() %}
        <h2>{{ source }}</h2>
        {% set entries = get_feed(url) %}
        {% if entries %}
            {% for entry in entries[:5] %}
                <div class="story">
                    <a href="{{ entry.link }}">{{ entry.title }}</a>
                </div>
            {% endfor %}
        {% else %}
            <p>Could not load stories for {{ source }}</p>
        {% endif %}
    {% endfor %}
</body>
</html>
"""

def get_feed(url):
    
    try:
        return feedparser.parse(url).entries
    except:
        return []

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, feeds=FEEDS, get_feed=get_feed)

if __name__ == "__main__":
    app.run()
