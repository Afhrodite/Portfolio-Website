from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Message from {name} ({email}): {message}")
        flash("Message sent successfully!", "success")
        return redirect("/contact")
    return render_template("contact.html")

@app.route('/programming')
def programming():
    return render_template('programming.html')

@app.route('/civil')
def civil_engineering():
    return render_template('civil_engineering.html')

if __name__ == "__main__":
    app.run(debug=True)