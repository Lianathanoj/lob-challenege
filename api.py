from flask import Flask, render_template, redirect, url_for, request
from apiclient.discovery import build
from webbrowser import open
from api_keys import google_civic_info_key, lob_api_key
import lob

flask = Flask(__name__)
civic_info_api = build('civicinfo', 'v2', developerKey=google_civic_info_key)
lob.api_key = lob_api_key

@flask.route('/', methods=['GET', 'POST'])
def index():
    # on form submit, get information
    if request.method == 'POST':
        sender_name = request.form.get('name')
        sender_address_line1 = request.form.get('address1')
        sender_address_line2 = request.form.get('address2')
        sender_city = request.form.get('city')
        sender_state = request.form.get('state')
        sender_zip = request.form.get('zip')
        sender_message = request.form.get('message')
        print(sender_name, sender_address_line1, sender_address_line2, sender_city, sender_state, sender_zip, sender_message)

        # find representative to contact using Lob API
        rep = civic_info_api.representatives().representativeInfoByAddress(address = sender_address_line1,
                                                                           levels='administrativeArea1',
                                                                           roles='deputyHeadOfGovernment')
        response = rep.execute()
        sendee_address = response['officials'][0]['address'][0]
        try:
            sendee_address_line2 = sendee_address['line2']
        except KeyError:
            sendee_address_line2 = ''
        finally:
            sendee_name = response['officials'][0]['name']
            sendee_address_line1 = sendee_address['line1']
            sendee_city = sendee_address['city']
            sendee_state = sendee_address['state']
            sendee_zip = sendee_address['zip']

        letter = lob.Letter.create(
            description = 'Letter to Representative',
            to_address = {
                'name': sendee_name,
                'address_line1': sendee_address_line1,
                'address_line2': sendee_address_line2,
                'address_city': sendee_city,
                'address_state': sendee_state,
                'address_zip': sendee_zip,
                'address_country': 'US'
            },
            from_address = {
                'name': sender_name,
                'address_line1': sender_address_line1,
                'address_line2': sender_address_line2,
                'address_city': sender_city,
                'address_state': sender_state,
                'address_zip': sender_zip,
                'address_country': 'US'
            },
            file = '<html style="padding-top: 3in; margin: .5in;">{{ message }}</html>',
            merge_variables = {
                'message': sender_message
            },
            color = True
        )
        return render_template('index.html', url=letter['url'])
    return render_template('index.html')

if __name__ == '__main__':
    flask.run(debug=True)