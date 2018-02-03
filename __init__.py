from flask import Flask, render_template

app = Flask(__name__)

'''
This is the index/home page of the web app
'''
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pictures")
def pictures():
    return render_template("pictures.html")

@app.route("/video")
def videos():
    return render_template("videos.html")

if __name__ == "__main__":
    app.run(port=8000)
