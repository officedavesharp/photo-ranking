from flask import Flask, render_template
import os

app = Flask(__name__, 
    static_folder='static',  # specify the static folder
    template_folder='templates'  # specify the templates folder
)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
