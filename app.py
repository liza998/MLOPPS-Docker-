from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/greet', methods = ["POST"])
def greet():
    if request.method == "POST":
        username = request.form["username"]
        return f"Welcome {username} to the first Docker File"
    else:
        return f"Didnot get the name"

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)