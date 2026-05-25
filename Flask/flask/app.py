from flask import Flask,render_template

## WSGI(web server gateway interface) application)
app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/index")
def index():
    return "this is the index page"

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)