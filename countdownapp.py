from flask import Flask, render_template_string, send_from_directory
from datetime import datetime
import os

app = Flask(__name__)

GO_LIVE_DATE = datetime(2025, 11, 14, 0, 0, 0)

@app.route('/')
def countdown():
    now = datetime.now()
    delta = GO_LIVE_DATE - now
    days = max(delta.days, 0)
    seconds = max(delta.seconds, 0)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    # Load HTML template from index.html in the root folder
    with open('index.html', 'r') as f:
        html_template = f.read()

    # Render template with live values
    return render_template_string(
        html_template,
        days=days,
        hours=f"{hours:02d}",
        minutes=f"{minutes:02d}",
        seconds=f"{secs:02d}"
    )

@app.route('/nuskin_logo.png')
def logo():
    return send_from_directory(os.getcwd(), 'nuskin_logo.png')

if __name__ == '__main__':
    app.run(debug=True)
