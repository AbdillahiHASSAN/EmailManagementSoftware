
from microsoft.graph import GraphServiceClient

import os
from flask import Flask, render_template, request
# Add other necessary imports here

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Email Management Software!"

if __name__ == '__main__':
    app.run()

from msal import PublicClientApplication
import webbrowser


client_id = '35b09450-c820-483f-8efd-d5c1a0ac08b5'
client_secret = 'Y6a5c3ef8-419e-4837-94df-fbf079762366'
redirect_uri = 'http://localhost:5000/callback'


authority = 'https://login.microsoftonline.com/common'
app = PublicClientApplication(client_id, authority=authority)


scopes = ['User.Read', 'Mail.Read']
auth_url = app.get_authorization_request_url(scopes, redirect_uri=redirect_uri)
webbrowser.open(auth_url)

authorization_code = input('Enter the authorization code from the redirect URL: ')

token_response = app.acquire_token_by_authorization_code(authorization_code, scopes=scopes, redirect_uri=redirect_uri)
access_token = token_response['access_token']


graph_client = GraphServiceClient(token={"access_token": access_token})


messages = graph_client.users['me'].messages.request().get()
for message in messages:
    print('Subject:', message.subject)

