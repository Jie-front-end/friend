from flask import Flask,render_template, abort

from jinja2 import TemplateNotFound
from flask_sqlalchemy import SQLAlchemy
import friend.config.config
from friend.mess import me
from friend.profile import pf
from friend.reglog import rl
from flask_cors import *
from friend.model.user import User


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost/friend"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "mxjdd"


app.register_blueprint(me)
app.register_blueprint(pf)
app.register_blueprint(rl)

db = SQLAlchemy(app)
CORS(app, supports_credentials=True)
@app.route('/')
def get_sample():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)
if __name__ == '__main__':
    app.run()