import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
import email
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
creds = None
if os.path.exists('token gmail.pickle'):
    with open('token gmail.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('c:/users/sarthak/downloads/credentials (1).json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token gmail.pickle', 'wb') as token:
        pickle.dump(creds, token)
def ListMessagesMatchingQuery(service, user_id, query=''):
    response = service.users().messages().list(userId=user_id,q=query).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])
    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id, q=query,pageToken=page_token).execute()
      messages.extend(response['messages'])
    return messages
print(ListMessagesMatchingQuery(build('gmail', 'v1', credentials=creds),'me','from:singhania.rajat1209@gmail.com'))
def GetMessage(service, user_id, msg_id):
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()
    print ('Message snippet: %s' % message['snippet'])
print(GetMessage(build('gmail', 'v1', credentials=creds),'me','16f225602391776a'))
def GetAttachments(service, user_id, msg_id, store_dir):
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()
    for part in message['payload']['parts']:
      if part['filename']:
        file_data = base64.urlsafe_b64decode(part['body']['data'].encode('UTF-8'))
        path = ''.join([store_dir, part['filename']])
        f = open(path, 'w')
        f.write(file_data)
        f.close()
GetAttachments(build('gmail', 'v1', credentials=creds),'sathak2806singhania@gmail.com','16a91ec5c444da727a91','c:/users/sarthak/downloads/')
