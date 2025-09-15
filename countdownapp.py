from flask import Flask, render_template_string, send_from_directory
from datetime import datetime
import os
import pytz

app = Flask(__name__)

# Use Mountain Time (Salt Lake City)
MT = pytz.timezone('America/Denver')

# Localize go-live date to Mountain Time
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

    # Zero pad hours, minutes, and seconds before passing to template
    hours_str = f"{hours:02d}"
    minutes_str = f"{minutes:02d}"
    seconds_str = f"{secs:02d}"

    with open('index.html', 'r') as f:
        html_template = f.read()

    return render_template_string(
        html_template,
        days=days,
        hours=hours_str,
        minutes=minutes_str,
        seconds=seconds_str
    )

@app.route('/Nu-Skin-Logo.png')
def logo():
    return send_from_directory(os.getcwd(), 'Nu-Skin-Logo.png')

if __name__ == '__main__':
    app.run(debug=True)
