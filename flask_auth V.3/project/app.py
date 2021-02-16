from project.__init__ import *
# from project.main import *
# from project.auth import *

app = create_app()

#app.register_blueprint(main)
#app.register_blueprint(auth)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "GET":
        return render_template('login.html')
    
    elif request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = fitwellUser.get_user_byId(email=email)

        # check if user actually exists
        # take the user supplied password, hash it, and compare it to the hashed password in database
        if not user or not check_password_hash(user.record['password'], password): 
            flash('Please check your login details and try again.')
            return redirect(url_for('login')) # if user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect(url_for('profile'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method=='GET':
        return render_template('signup.html')

    elif request.method=='POST':

        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = fitwellUser.get_user_byId(email=email) # if this returns a user, then the email already exists in database

        if user: # if a user is found, we want to redirect back to signup page so user can try again  
            flash('Email address already exists')
            return redirect(url_for('signup'))

        # create new user with the form data. Hash the password so plaintext version isn't saved.
        new_user = fitwellUser(email=email, name=name, password=generate_password_hash(password, method='sha256'))

        # add the new user to the database
        # db.session.add(new_user)
        # db.session.commit()

        return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.record['name'])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') 
