import pyperclip
import requests
import random
import string
import time
import sys
import re
import os

API = 'https://www.1secmail.com/api/v1/'
domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
domain = random.choice(domainList)

def banner():
    pass

def generateUserName():
    name = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name) for i in range(10))
    return username

def extract():
    getUserName = re.search(r'login=(.*)&',newMail).group(1)
    getDomain = re.search(r'domain=(.*)', newMail).group(1)
    return [getUserName, getDomain]

# Got this from https://stackoverflow.com/a/43952192/13276219
def print_statusline(msg: str):
    last_msg_length = len(print_statusline.last_msg) if hasattr(print_statusline, 'last_msg') else 0
    print(' ' * last_msg_length, end='\r')
    print(msg, end='\r')
    sys.stdout.flush()
    print_statusline.last_msg = msg

def deleteMail():
    url = 'https://www.1secmail.com/mailbox'
    data = {
        'action': 'deleteMailbox',
        'login': f'{extract()[0]}',
        'domain': f'{extract()[1]}'
    }

    print_statusline("Disposing your email address - " + mail + '\n')
    req = requests.post(url, data=data)

def checkMails():
    global newMail, regMail, mail
    otp = ''
    act_link = ''
    password = ''
    verfi_code = ''
    reqLink = f'{API}?action=getMessages&login={extract()[0]}&domain={extract()[1]}'
    req = requests.get(reqLink).json()
    length = len(req)
    if length == 0:
        print_statusline("Your mailbox is empty. Hold tight. Mailbox is refreshed automatically every 5 seconds.")
    else:
        idList = []
        for i in req:
            for k,v in i.items():
                if k == 'id':
                    mailId = v
                    idList.append(mailId)

        x = 'mails' if length > 1 else 'mail'
        print_statusline(f"You received {length} {x}. (Mailbox is refreshed automatically every 5 seconds.)")

        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, r'All Mails')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

        for i in idList:
            msgRead = f'{API}?action=readMessage&login={extract()[0]}&domain={extract()[1]}&id={i}'
            req = requests.get(msgRead).json()
            for k,v in req.items():
                if k == 'from':
                    sender = v
                if k == 'subject':
                    subject = v
                if k == 'date':
                    date = v
                if k == 'body':
                    # Find the password
                    content = v
                    ind_pass_start = v.find('Password')
                    if ind_pass_start == -1:
                        pass
                    else:
                        password = v[ind_pass_start+18:ind_pass_start+26]
                        print('Password:', password)

                    # Find the activation code:
                    ind_act_start = v.find('Please verify you email')
                    ind_act_end = v.find('to validate you email. ')
                    if ind_act_end == -1:
                        pass
                    else:
                        act_link = v[ind_act_start + 48: ind_act_end - 17]

                        print('Activation:', act_link)

                    # Find OTP:
                    otp_ind = v.find('OTP - ')
                    if otp_ind == -1:
                        pass
                    else:
                        otp = v[otp_ind + 6:otp_ind + 11]
                        while otp[-1] not in string.digits:
                            otp = otp.replace(otp[-1],'')
                        print('OTP:', otp)

                    # Find Verification code:
                    veri_ind = v.find('Verification code - ')
                    if verfi_code == -1:
                        pass
                    else:
                        verfi_code = v[veri_ind + 20: veri_ind + 24]
                        print(verfi_code)


            return act_link, password, otp, verfi_code

def generate_email():
    global newMail, regMail, mail
    try:

        newMail = f"{API}?login={generateUserName()}&domain={domain}"
        reqMail = requests.get(newMail)
        mail = f"{extract()[0]}@{extract()[1]}"
        #pyperclip.copy(mail)
        print("\nYour temporary email is " + mail + " (Email address copied to clipboard.)" + "\n")
        print(f"---------------------------- | Inbox of {mail} | ----------------------------\n")

        return mail

    except(KeyboardInterrupt):
        deleteMail()
        print("\nProgramme Interrupted")
        os.system('cls' if os.name == 'nt' else 'clear')









