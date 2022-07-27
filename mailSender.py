from importlib.resources import path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders





#####
# 
# get list of emails from a file 
# 
# 
# ###
emailsList = []

# use demoEmails.txt file to test the program before sending real mail message 
fileToRead = 'emails.txt'
delimiterInFile = [',', ';']
file = open(fileToRead, 'r') 
listLine = file.readlines()
for itemLine in listLine:
    orgItem = str(itemLine)
    item = orgItem
    if "\n" in orgItem:
        orgItemLength = len(orgItem)
        item = orgItem[:orgItemLength - 1]
    emailsList.append(item)
    
    
# deleting duplicates emails from the list
emailsList = list(set(emailsList))

    
    



####
# 
# mail details and actions
# 
# 
# #####



mail_content = 'Hi Friend  - I am looking for a new role and would appreciate your support...'


#The mail addresses and password
sender_address = 'test@gmail.com'
sender_pass = 'yourAppPassword' # application password that you get from your gmail / apppassword , ! you can find more in gmailSettings/security:googlesignin  or https://myaccount.google.com/security , SEE image attached with this project /apppasswordsImageExample.png
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = sender_address
message['Subject'] = 'full stack developer...'   #The subject line

#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
pdfname = 'pdfname.pdf'
pdfPath = 'YourPathToPdfFile'+ pdfname

# open the file in bynary
binary_pdf = open(pdfPath, 'rb')

payload = MIMEBase('application', 'octate-stream', Name=pdfname)
# payload = MIMEBase('application', 'pdf', Name=pdfname)
payload.set_payload((binary_pdf).read())

# enconding the binary into base64
encoders.encode_base64(payload)

# add header with pdf name
payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
message.attach(payload) ## to Disable attaching file with the email comment this line
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()

emailsListLength = len(emailsList)

for i in range( len(emailsList) ):
    email = emailsList[i]    
    session.sendmail(sender_address, email, text)
    print(f'Mail Sent to - {email}, {i+1} / {emailsListLength}.')

print(f"total mails sent: {emailsListLength}")
session.quit()
