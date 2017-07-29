from flask import Flask, render_template, request, redirect
from twilio_client import client
import os

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']




@app.route('/')
def main():
    return render_template('main.html')


@app.route('/send_text', methods=['POST'])
def send_text():

    phone = request.form.get("phone")
    text = request.form.get("message")

    message = client.api.account.messages.create(
        to="+15106840288",
        from_="+15103451264",
        body=text)

    return redirect('/')

