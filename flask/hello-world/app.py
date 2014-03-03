from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    names = ["michael", "john", "edward", "liz"]
    rand = random.randint(100,500)
    url = "http://placekitten.com/g/{}/{}".format(rand,rand)
    return render_template("layout.html", names=names, url=url)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
