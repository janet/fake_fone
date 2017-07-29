# About

Fake fone is a web app that sends text messages using Twilio's api

# To start development locally

1. Clone this repo `git clone git@github.com:janet/fake_fone.git`

1. Create python virtualenv and install requirements and app


        $ virtualenv env
        $ source env/bin/activate
        $ (env) pip install -r requirements.txt

1. Set environment variables


        $ (env) export SECRET_KEY='' # enter your secret key
        $ (env) export TWILIO_ACCOUNT_SID='' # enter your twilio account sid
        $ (env) export TWILIO_AUTH_TOKEN='' # enter your twilio auth token

1. Run @ http://localhost:5000/


        $ (env) python server.py


# Deployed Versions

## Heroku

http://fake-fone.herokuapp.com/

# Screenshot

![screnshot](https://github.com/janet/fake_fone/static/img/screenshot.png "Fake phone... who dis")
