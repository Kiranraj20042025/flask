from flask import Blueprint,render_template

auth=Blueprint('auth',__name__)

@auth.route('/register')
def register():
    return render_template('registration.html')

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/end')
def end():
    return render_template('end.html')
    

