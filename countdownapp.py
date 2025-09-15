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

    # HTML template as a string, using logo.png from root folder
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>India MVP-1 Business Go Live Countdown</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
            img {{ width: 150px; }}
            h1 {{ font-size: 24px; margin-bottom: 10px; }}
            .countdown {{ font-size: 48px; margin-top: 20px; color: #007ba7; }}
        </style>
    </head>
    <body>
        <img src="/nuskin_logo.png" alt="Nuskin Logo" />
        <h1>India MVP-1 Business Go Live - 14-Nov-2025</h1>
        <div>Day remaining: T-{days}</div>
        <div class="countdown">{hours:02d}:{minutes:02d}:{secs:02d}</div>
        <script>
            setTimeout(() => location.reload(), 1000);
        </script>
    </body>
    </html>"""

    return render_template_string(html_template)

# Route to serve the logo image from root folder
@app.route('/nuskin_logo.png')
def logo():
    return send_from_directory(os.getcwd(), 'nuskin_logo.png')

if __name__ == '__main__':
    app.run(debug=True)
