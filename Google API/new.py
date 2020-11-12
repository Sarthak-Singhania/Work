import pickle
import os.path
import PyPDF2
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import smtplib
import base64
import email
from apiclient import errors
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
from time import sleep
from tkinter import *
from tkinter import ttk
from time import sleep
import subprocess
import sys
SCOPES=['https://www.googleapis.com/auth/tasks']
creds=None
if os.path.exists('token tasks.pickle'):
    with open('token tasks.pickle','rb') as token:
        creds=pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow=InstalledAppFlow.from_client_secrets_file('credentials tasks.json',SCOPES)
        creds=flow.run_local_server(port=0)
    with open('token tasks.pickle','wb') as token:
        pickle.dump(creds,token)
service=build('tasks','v1',credentials=creds)
tasks=service.tasks().list(tasklist='@default',maxResults=100,showCompleted=True,showHidden=True).execute()
for i in tasks['items']:
    if len(i)==10 and i['title'][:8]=='Purchase':
        print(i)
