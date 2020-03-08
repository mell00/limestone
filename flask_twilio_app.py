from flask import Flask, Response, request, render_template
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

TWILIO_ACCOUNT_SID = 'ACc0959b76fea556d259638277398977d8'
TWILIO_AUTH_TOKEN = '744dc88de3147709533a1f03246111ea'
TWILIO_PHONE_NUMBER = '+12166665403'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) #create twilio account client
app = Flask(__name__) #flask web app

# Create a route to handle incoming SMS messages
# This app assumes ANY response indicates they are safely out
@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    #############################################################
    #################update database user status#################
    #############################################################
    print(f'Incoming message from {request.values.get("From")}: ${request.values.get("Body")}')

    # Here, we're generating TwiML using the Python helper library
    resp = MessagingResponse()
    resp.message("Thank you.")
    return str(resp)

if __name__ == '__main__':
    # Note that in production, you would want to disable debugging
    app.run(debug=True)
