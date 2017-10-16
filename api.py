from flask import Flask, render_template, redirect, url_for, request
from apiclient.discovery import build
from api_keys import google_civic_info_key, lob_api_key
import lob

flask = Flask(__name__)

@flask.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sender_name = request.form.get('name')
        sender_address_1 = request.form.get('address1')
        sender_address_2 = request.form.get('address2')
        sender_city = request.form.get('city')
        sender_state = request.form.get('state')
        sender_zip = request.form.get('zip')
        sender_message = request.form.get('message')
        print(sender_name, sender_address_1, sender_address_2, sender_city, sender_state, sender_zip, sender_message)
    return render_template('index.html')

if __name__ == '__main__':
    flask.run(debug=True)