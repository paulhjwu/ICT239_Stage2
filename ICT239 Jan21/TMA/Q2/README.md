py# DCS Smart Trolley migration project

# One-time setup

    $ cd <to-this-directory>
    $ python3 -m venv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt

# Run Flask app

    $ cd <to-this-directory>
    $ . venv/bin/activate
    $ mongod --dbpath your_data_directory
    $ "flask run" or "Use VS Code" to run

# Routes
| function | route | html | javascript
| - | - | - | -
| `login` | `/login` | `login.html` | - 
| `register` | `/register` | `register.html`
| `logout` | `/logout` | - | -
| `index` | `/` | `dashboard.html` | `dashboard.js`
| `account` | `/account` | `account.html` | -
| `email` | `/email` | `email.html` | -
| `download` | `/download` | `download.html` | `download.js`
| `seed` | `/seed` | `seed.html` | - | not visible

- All templates share the same css file - `index.css`
- `login.html`, `register.html`, and `base_logged.html` extends `base.html`
- `account.html`, `dashboard.html`, `download.html`, and `email.html` extends `base_logged.html`

# Dependencies

| dependencies | notes | link
| - | - | -
| dnspython | required for `pymongo` | -
| pymongo | For connection with MongoDB server | https://pymongo.readthedocs.io/en/| stable/
| flask-login | For managing user session | https://flask-login.readthedocs.io/en/latest/
| flask-mail | For sending email with csv attachment | https://pythonhosted.org/Flask-Mail/
