from flask import Flask
from flask import render_template, request, redirect

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required

from werkzeug.security import generate_password_hash, check_password_hash

from flask_bootstrap import Bootstrap

from datetime import datetime
import pytz
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # SQLite3
app.config['SECRET_KEY'] = os.urandom(24)  # 暗号化用

db = SQLAlchemy(app)  # インスタンス化してアプリを紐付け
bootstrap = Bootstrap(app)  # インスタンス化してアプリを紐付け

login_manager = LoginManager()
login_manager.init_app(app)

# Blog DB
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50),  nullable=False)
    body = db.Column(db.String(300),  nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, 
                    default=datetime.now(pytz.timezone('Asia/Tokyo')))

"""
DB の作成は、pythonの対話モードから、以下のコマンドで（初期化）
# python3
>>> from app import db
>>> db.create_all()
"""

# user DB
class User(UserMixin, db.Model):  # 2つを継承
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(12), nullable=False)


# ログイン状態の確認のため、、、
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/", methods=['GET', 'POST'])
@login_required
def index():

    if request.method == 'GET':
        posts = Post.query.all()
        return render_template('index.html', posts=posts)

@app.route("/create", methods=['GET', 'POST'])
@login_required
def create():

    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')

        post = Post(title=title, body=body)

        db.session.add(post)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('create.html')

@app.route("/<int:id>/update", methods=['GET', 'POST'])
@login_required
def update(id):

    post = Post.query.get(id)
    if request.method == 'GET':
        return render_template('update.html', post=post)

    else:
        post.title = request.form.get('title')
        post.body = request.form.get('body')

        db.session.commit()

        return redirect('/')

@app.route("/<int:id>/delete", methods=['GET'])
@login_required
def delete(id):

    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect('/')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User(username=username, password=generate_password_hash(password, method='sha256'))

        db.session.add(user)
        db.session.commit()
        return redirect('/login')

    else:
        return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        # password chkのみ　→　パスワード間違いやユーザなしの処理が必要
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect('/')

    else:
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')
