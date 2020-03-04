from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    dummyData =[
    {
        "name": {"first": "Hifza", "last":"Zaheer"},
        "title": "First Post",
        "content": "This is some dummy data for Flask Lectures"
    },
    {
        "name": {"first": "Hiiiiiiz", "last": "Zaheer"},
        "title": "Second_Post",
        "content": "This is even more dummy data from the flask Lectures"
    }
]
    return render_template("index.html" , title="Home",posts=dummyData)
if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)
