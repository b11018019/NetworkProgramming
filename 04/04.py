from flask import Flask, redirect, url_for, render_template, request, session
app = Flask(__name__)
app.secret_key = "#230dec61-fee8-4ef2-a791-36f9e680c9fc"
#login
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user

        user = request.form["nm01"]
        session["user01"] = user
        
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" and "user01" in session:
        user = session["user"]
        user01 = session["user01"]
        return render_template("user.html",user=user,user01=user01)
    else:
        return redirect(url_for("login"))
if __name__ =="__main__":
    app.run()