from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='Assets')


@app.route("/")
def home_page():
    return render_template("home_page.html")


@app.route("/rrn")
def rrn():
    return render_template("rrn.html")


@app.route("/lstm")
def lstm():
    return render_template("lstm.html")


@app.route("/gru")
def gru():
    return render_template("gru.html")


@app.route("/am")
def am():
    return render_template("am.html")


@app.route("/trans")
def trans():
    return render_template("trans.html")


@app.route("/bs")
def bs():
    return render_template("bs.html")


@app.route("/tks")
def tks():
    return render_template("tks.html")


@app.route("/ts")
def ts():
    return render_template("ts.html")


@app.route("/pe")
def pe():
    return render_template("pe.html")


@app.route("/ft")
def ft():
    return render_template("ft.html")


if __name__ == "__main__":
    app.run(debug=True)
