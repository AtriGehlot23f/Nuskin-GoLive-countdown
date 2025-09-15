from flask import Flask, render_template_string, send_from_directory
from datetime import datetime
import os
import pytz

app = Flask(__name__)

# Use Mountain Time (Salt Lake City, Utah)
MT = pytz.timezone('America/Denver')

# Localize Go Live date to Mountain Time
GO_LIVE_DATE = MT.localize(datetime(2025, 11, 14, 0, 0, 0))

@app.route('/')
def countdown():
    now = datetime.now(MT)
    delta = GO_LIVE_DATE - now
    days = max(delta.days, 0)
    seconds = max(delta.seconds, 0)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    # Load HTML template from root folder index.html
    with open('index.html', 'r') as f:
        html_template = f.read()

    # Render template with countdown values
    return render_template_string(
        html_template,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=secs
    )

# Serve logo image from root folder
@app.route('/Nu-Skin-Logo.png')
def logo():
    return send_from_directory(os.getcwd(), 'Nu-Skin-Logo.png')

if __name__ == '__main__':
    app.run(debug=True)
