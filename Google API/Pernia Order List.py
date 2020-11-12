from __future__ import print_function
####################################Import#########################################################################################################################################################
try:
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
    import shutil
except:
    import subprocess
    import sys
    modules='google-api-python-client google-auth-httplib2 google-auth-oauthlib pandas numpy PyPDF2'.split()
    for i in modules:
        subprocess.check_call(['pip','install',i])
tk=Tk()
tk.geometry('400x240')
tk.title('Pernia Order List')
style=ttk.Style()
style.configure('TLabel',foreground='blue',font=('Times New Roman Bold',14),anchor='center')
style.configure('TButton',foreground='#066ED6',background='#022873',font=('Times New Roman Bold',17),anchor='center')
######################################Tasks Authentication#########################################################################################################################################
print('Establishing connection with google')
try:
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
    SCOPESG=['https://mail.google.com/']
    credsg=None
    if os.path.exists('token gmail.pickle'):
        with open('token gmail.pickle','rb') as tokeng:
            credsg=pickle.load(tokeng)
    if not credsg or not credsg.valid:
        if credsg and credsg.expired and credsg.refresh_token:
            credsg.refresh(Request())
        else:
            flow=InstalledAppFlow.from_client_secrets_file('credentials gmail.json',SCOPESG)
            credsg=flow.run_local_server(port=0)
        with open('token gmail.pickle','wb') as tokeng:
            pickle.dump(credsg,tokeng)
    serviceg=build('gmail','v1',credentials=credsg)
    print('Connection established')
except:
    sleep(2)
    print('Connection not established,check internet')
    input('Press enter to quit...')
    quit()
#####################################Tasks Import##################################################################################################################################################
tasks=service.tasks().list(tasklist='@default',maxResults=100).execute()
po_no=[]
p_name=[]
qty=[]
price=[]
attach=[]
filename=[]
sr=[]
for i in tasks['items']:
    if len(i)==10 and i['title'][:8]=='Purchase':
        attach.append(i['links'][0]['link'][-16:])
#######################################Gmail#######################################################################################################################################################
def email_po():
    df=pd.DataFrame({'Sr. No.':sr,'PO No':po_no,'Name':p_name,'Qty':qty,'Amount':price})
    writer=ExcelWriter('Pernia Order.xlsx')
    df.to_excel(writer,'Sheet1',index=False)
    writer.save()
    shutil.copy('Pernia Order.xlsx','c:/users/singhania/desktop/Pernia Order.xlsx')
    emails=Toplevel(tk)
    emails.wm_iconbitmap('Logo 3.ico')
    fromaddr='info@assemblagetheshop.com'
    toaddr='singhania.rajat1209@gmail.com'
    msg=MIMEMultipart()
    msg['From']=fromaddr
    msg['To']=toaddr
    msg['Subject']='Pernia Order from Google Tasks'
    filename='Pernia Order.xlsx'
    attachment=open('Pernia Order.xlsx','rb')
    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition','attachment; filename= %s' % filename)
    msg.attach(p)
    s=smtplib.SMTP('smtp.hostinger.in',587) 
    s.starttls() 
    s.login(fromaddr,'Lollipop@4554') 
    text=msg.as_string()
    s.sendmail(fromaddr,toaddr,text)
    s.quit()
    ttk.Label(emails,text='Email sent').pack()
    ttk.Button(emails,text='Exit',command=emails.destroy,style='TButton').pack(side=TOP,expand=YES)
print('Downloading...................')
for i in attach:
    try:
        message=serviceg.users().messages().get(userId='me',id=i).execute()
        att=serviceg.users().messages().attachments().get(userId='me',messageId=i,id=message['payload']['parts'][1]['body']['attachmentId']).execute()
    except:
        pass
    if message['payload']['parts'][1]['filename']:
        file_data=base64.urlsafe_b64decode(att['data'].encode('UTF-8'))
        path=''.join(['order files/',message['payload']['parts'][1]['filename']])
        f=open(path,'wb')
        f.write(file_data)
        f.close()
        filename.append(message['payload']['parts'][1]['filename'])
del i
for i in filename:
    pdfFileObj=open('order files/'+i,'rb') 
    pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
    pageObj=pdfReader.getPage(0)
    a=pageObj.extractText()
    b=a.split('\n')
    for x in b:
        if x[:5]=='PO No':
            po_no.append(int(x[-5:]))
            lol=x[-5:]
            break
    del x
    for x in range(len(b)):
        if b[x][:4]=='ASSC':
            cnt=x+2
            if b[cnt+2]!='Size':
                p_name.append(b[cnt]+' '+b[cnt+1])
                break
            elif b[cnt+2]=='Size':
                p_name.append(b[cnt])
                break
    del x
    for x in range(len(b)):
        if b[x]=='Product Image':
            cnt=x-3
            qty.append(int(b[cnt]))
            break
    del x
    for x in range(len(b)):
        if b[x]=='Total Amount (Inc of Taxes)':
            price.append(int(b[x+1]))
            break
    pdfFileObj.close()
    print('Downloaded file for PO No.: %s'%lol)
del i
for i in range(len(po_no)):
    sr.append(i+1)
######################################Print Tasks##################################################################################################################################################
def show_pernia():
    leadwin=Toplevel(tk)
    leadwin.wm_iconbitmap('Logo 3.ico')
    style.configure('TLabel',foreground='blue',font=('Times New Roman Bold',14),anchor='center')
    ttk.Label(leadwin,text='Order List',style='TLabel').grid(row=0,column=2)
    order=ttk.Treeview(leadwin,column=('column1','column2','column3','column4','column5'),show='headings')
    order.heading('#1',text='Sr. No.')
    order.column('#1',minwidth=0,width=50)
    order.heading('#2',text='PO No.')
    order.column('#2',minwidth=0,width=65)
    order.heading('#3',text='Product Name')
    order.column('#3',minwidth=0,width=350)
    order.heading('#4',text='QTY')
    order.column('#4',minwidth=0,width=30)
    order.heading('#5',text='Price')
    order.column('#5',minwidth=0,width=60)
    order.grid(row=1,column=0,columnspan=6)
    for i in range(len(po_no)):
        a=[]
        a.append(str(i+1))
        a.append(po_no[i])
        a.append(p_name[i])
        a.append(qty[i])
        a.append(price[i])
        order.insert('','end',values=a)
    ttk.Button(leadwin,command=leadwin.destroy,text='Exit',style='TButton').grid(row=0,column=3)
    leadwin.mainloop()
#######################################Delete file#################################################################################################################################################
def delete():
    try:
        for i in filename:
            os.remove(''.join(['order files/',i]))
    except:
        pass
    try:
        os.remove('Pernia Order.xlsx')
    except:
        pass
###################################################################################################################################################################################################
tk.wm_iconbitmap('Logo 3.ico')
ttk.Button(tk,command=email_po,text='Email files',style='TButton').pack(side=TOP,expand=YES)
ttk.Button(tk,command=show_pernia,text='Pernia Order numbers',style='TButton').pack(side=TOP,expand=YES)
ttk.Button(tk,command=lambda:[tk.destroy(),delete()],text='Exit',style='TButton').pack(side=TOP,expand=YES)
delete()
tk.mainloop()
