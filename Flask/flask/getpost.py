from flask import Flask,render_template, request

## WSGI(web server gateway interface) application)
app=Flask(__name__)

@app.route("/")
def index():
    return "this is the index page"

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route('/about', methods=["GET"])
def about():
    return render_template("about.html")

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        # Handle form submission
        name=request.form['name']
        return f'HELLO {name}!'
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        # Handle form submission
        name=request.form['name']
        return f'HELLO {name}!'
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)