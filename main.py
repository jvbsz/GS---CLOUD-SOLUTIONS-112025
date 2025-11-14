from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv("ai_job_trends_dataset.csv")
    html_table = df.to_html(classes='table table-striped', index=False)
    return render_template("index.html", table=html_table)

if __name__ == '__main__':
    app.run()
