from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

CSV_FILE = "ai_job_trends_dataset.csv"

def load_csv():
    try:
        df = pd.read_csv(CSV_FILE, sep=None, engine="python", encoding="utf-8")
        return df
    except Exception:
        df = pd.read_csv(CSV_FILE, sep=None, engine="python", encoding="latin1")
        return df

@app.route("/")
def index():
    df = load_csv()
    html_table = df.to_html(classes="table table-striped table-bordered", index=False)
    return render_template("index.html", table=html_table)

if __name__ == "__main__":
    app.run()
