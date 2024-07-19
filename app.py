# app.py

from flask import render_template
import connexion

# app = Flask(__name__)

app = connexion.App(__name__, specification_dir='./')
app.add_api("swagger.yaml")


@app.route('/')
def home():
    return render_template('home.html') # render a template

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True) # run our Flask app

