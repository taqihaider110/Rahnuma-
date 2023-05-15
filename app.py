from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key="hello"
# app.config[]
app.permanent_session_lifetime=timedelta(minutes=1 )

@app.route("/",methods=["POST","GET"])
def login():
    if request.method =="POST":
        session.permanent =True
        user =request.form["nm"]
        session["user"]=user
        flash("Login Succesfull!")
        return redirect(url_for("home"))
    else:
        if "user" in session:
            flash("Already logged In!")
            return redirect(url_for("home"))
        return render_template("login.html")
    
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

    
@app.route("/service")
def service():
    return render_template("service.html")

    
@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/user")
def user():
    if "user" in session:
        user=session["user"]
        return render_template("user.html",user=user)
    else:
        flash("You are not logged In!")
        return redirect(url_for("login"))
@app.route("/logout")
def logout():
    flash(f"You have been logged out","info")
    session.pop("user",None)
    return redirect(url_for("login"))
if __name__=="__main__":
    app.run(debug=True)