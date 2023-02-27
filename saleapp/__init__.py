from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
import cloudinary
from flask_login import LoginManager
from flask_socketio import SocketIO

app = Flask(__name__)

app.secret_key = '689567gh$^^&*#%^&*^&%^*DFGH^&*&*^*'
<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/flight?charset=utf8mb4' % quote("Admin@123")
=======
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/quanlymaybay?charset=utf8mb4'
>>>>>>> 53ddffd1a841d3d39424675f39531e71cdfe1215
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


cloudinary.config(
    cloud_name="dhffue7d7",
    api_key="215425482852391",
    api_secret="a9xaGBMJr7KgKhJa-1RpSpx_AmU"
)

db = SQLAlchemy(app=app)
login = LoginManager(app=app)
socketio = SocketIO(app)


