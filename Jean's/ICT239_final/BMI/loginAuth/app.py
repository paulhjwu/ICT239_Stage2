1234from init import *

app = create_app()

#Route to the relevant webpage

@app.route('/')
@login_required #added in later
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    #return render_template('profile.html')

    #{EDITS}!!!!!!
    return render_template('profile.html', name=current_user._record['name'])

@app.route('/login', methods=['GET', 'POST'])
def login():

    #request.method GET POST
    if request.method == "GET":
        return render_template('login.html')

    elif request.method == "POST":
        #get the user input on email, password, remember me checkbox value
        email = request.form.get('email')
        password = request.form.get('password')
        #remember check box : True = checked, False = unchecked
        remember = True if request.form.get('remember') else False

        #check if the user exist in the database, and if user exist, check if the password is the same as database
        user = fitwellUser.get_user_byId(email=email)
        #getRecord = user.get_record()
        #print("USER 2: " + str(getRecord['password']))

        if not user or not check_password_hash(user._record['password'], password):
            #display error message in the login.html - flash method
            flash('Please check your login details and try again.')
            #if user doesn't not exist or password is wrong
            return redirect(url_for('login'))

        #the check passes, and we know that user has the right credentials
        #login_user method from flash-login package
        login_user(user, remember=remember)
        #login_user(user)

        #redirect the user to the profile page
        return redirect(url_for('profile'))
    

@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method ==  'GET':    
        return render_template('signup.html')

    elif request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        #check if this email exist in the database = flash message, redirect the user to signup
        user = fitwellUser.get_user_byId(email=email)

        if user:    #if user is found
            flash('Email address already exists')
            return redirect(url_for('signup'))

        #create the new user in the database
        new_user = fitwellUser(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    #flask-login method
    logout_user()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=8000)