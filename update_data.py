import os
import requests
import google.generativeai as genai

# API சாவிகளை அமைத்தல்
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
news_api_key = os.environ["NEWS_API_KEY"]

# செய்திகளைத் திரட்டுதல்
news_url = f"https://newsapi.org/v2/top-headlines?category=business&language=en&apiKey={news_api_key}"
articles = requests.get(news_url).json().get("articles", [])
headlines = "\n".join([a["title"] for a in articles[:5]])

# Gemini மூலம் பகுப்பாய்வு
model = genai.GenerativeModel('gemini-pro')
prompt = f"Analyze these financial headlines and recommend 5 stocks:\n{headlines}"
analysis = model.generate_content(prompt).text

# index.html கோப்பைப் புதுப்பித்தல்
html_content = f"""
<!DOCTYPE html>
<html>
<head><title>Autonomous Stocks</title></head>
<body>
    <h1>Autonomous Intraday Picks</h1>
    <pre>{analysis}</pre>
</body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html_content)

print("Index.html updated successfully.")
