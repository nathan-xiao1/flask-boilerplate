from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from models import User

app = Flask(__name__)
app.secret_key = '\xee\xa4;{2\x87K\x0b' # CHANGEME
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id) # TODO

if __name__ == "__main__":
  app.run()

@app.route('/')
def home():
    return render_template('pages/index.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        login_user(None) # TODO
        return redirect('/')
    return render_template('pages/login.html')
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")