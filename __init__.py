from flask import Flask, render_template

app = Flask(__name__)

'''
This is the index/home page of the web app
'''
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route()

if __name__ == "__main__":
    app.run(port=8000)
