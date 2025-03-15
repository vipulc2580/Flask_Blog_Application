from datetime import datetime
from flask import current_app
from flaskblog import db,login_manager
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer, BadSignature, SignatureExpired

@login_manager.user_loader
def load_user(user_id):
    user=User.query.get(int(user_id))
    return user

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    posts=db.relationship('Post',backref='author',lazy=True)

    def __repr__(self):
        return f"User('{self.username}, {self.email}, {self.image_file},{self.id}')"
    
    def get_reset_token(self):
        s=Serializer(current_app.config['SECRET_KEY'])
        SALT = "email-confirmation"
        return s.dumps({'user_id':self.id},salt=SALT)

    @staticmethod
    def verfiy_reset_token(token,expire_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        SALT = "email-confirmation"
        try:
            user_id = s.loads(token, salt=SALT, max_age=expire_sec)
            print(user_id,type(user_id))
            return User.query.get(user_id.get('user_id'))  
        except SignatureExpired:
            return None  
        except BadSignature:
            return None  






class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"