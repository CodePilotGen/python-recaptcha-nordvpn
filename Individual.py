import sele_code
import mail_generator
from tkinter.filedialog import askopenfilename
import pandas as pd
from nordvpn_switcher import initialize_VPN,rotate_VPN
import time

def ind():
    instructions = initialize_VPN(area_input=['spain'])
    email_df = pd.DataFrame(columns=['Passport', 'Last Name', 'First Name', 'Email', 'Phone', 'Date', 'Time'])

    filename = askopenfilename()
    #filename = '/Casablanca.xlsx'
    ind = filename.find('.xlsx') - 1
    loc = ''
    while filename[ind] != '/':
        loc = filename[ind] + loc
        ind = ind - 1

    if loc == 'Agadir':
        loc = 6
    elif loc == 'Casablanca':
        loc = 2
    elif loc == 'Nador':
        loc = 4
    elif loc == 'Rabat':
        loc = 3
    elif loc == 'Tangier':
        loc = 1
    elif loc == 'Tetouan':
        loc = 5
    else:
        print('Error')
        raise ValueError



    df = pd.read_excel(filename)
    df['dateOfBirth'] = df['dateOfBirth'].dt.strftime('%Y-%b-%d %H:%I:%S')
    df['passportIssueDate'] = df['passportIssueDate'].dt.strftime('%Y-%b-%d %H:%I:%S')
    df['passportExDate'] = df['passportExDate'].dt.strftime('%Y-%b-%d %H:%I:%S')
    for i in range(df.shape[0]):
        fName = df['fName'][i]
        lName = df['lName'][i]
        DoB = df['dateOfBirth'][i]
        pNu = df['passportNo'][i]
        p_issue_date = df['passportIssueDate'][i]
        p_exp_date = df['passportExDate'][i]
        p_place = df['passportIssuePlace'][i]
        while True:
            try:
                email = mail_generator.generate_email()

                email_df = sele_code.main_sele(email, loc, fName, lName, str(DoB), pNu, str(p_issue_date), str(p_exp_date), p_place,
                                    email_df, instructions)
                print(fName, lName, pNu)
                break
            except:
                print('Error', fName, lName, pNu)
    return email_df


out = ind()
out.to_excel('Appointments_ind'+str(time.time()) + '.xlsx')