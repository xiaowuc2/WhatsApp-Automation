print("Message sent, sir")
from twilio.rest import Client

account_sid = 'AC4e6d28bc6d62313926805013be9b8d19'
auth_token = 'b7f0ec4d83c12e12fb0cef422a5cc777'
client = Client(account_sid, auth_token)

def send_love():
    message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='from rohit ',
                              to='whatsapp:+918145669222'
                          )

    print(message.sid)
