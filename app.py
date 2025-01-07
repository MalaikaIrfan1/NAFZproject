from flask import Flask , render_template
app = Flask(__name__)

@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/about")
def about():        
    return render_template("about.html")

@app.route("/review")
def member():
    return render_template("review.html")

@app.route("/homepage")
def home():        
    return render_template("homepage.html")

if __name__ == '__main__':
    app.run(debug=True)