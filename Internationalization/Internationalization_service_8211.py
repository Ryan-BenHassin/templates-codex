#TODO
import flask
from flask_babel import Babel
from flask_babel import _

app = flask.Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

@babel.localeselector
def get_locale():
 return 'fr' # change this to 'es' for Spanish, 'fr' for French, etc.

@app.route('/')
def index():
 return _('Hello, World!')

if __name__ == '__main__':
 app.run()
