from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Task 2
@app.route('/')
def home():
    return """
    <h1>Favorite Acronyms</h1>
    <p>1: ASAP (As Soon As Possible)</p>
    <p>2: BBL (Be Back Later)</p>
    <p>3: BOGOF (Buy One Get One Free)</p>
    """

# Task 3,4
@app.route('/lucy')
def lucy():
    favorite_acronym = "ASAP (As Soon As Possible)"
    return render_template('template.html',
                           acronym=favorite_acronym)

if __name__ == '__main__':
    app.run(debug=True)
