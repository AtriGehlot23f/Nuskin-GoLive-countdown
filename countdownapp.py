from flask import Flask, render_template
from datetime import datetime

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
    return render_template('index.html',
                           days=days,
                           hours=f"{hours:02d}",
                           minutes=f"{minutes:02d}",
                           seconds=f"{secs:02d}")

if __name__ == '__main__':
    app.run(debug=True)
