import time
import sele_code
import mail_generator
from tkinter.filedialog import askopenfilename
import pandas as pd
from nordvpn_switcher import initialize_VPN,rotate_VPN

def family():
    print('Family Code')
    instructions = initialize_VPN(area_input=['Europe'])
    email_df = pd.DataFrame(columns=['Passport', 'Last Name', 'First Name', 'Email', 'Phone', 'Date', 'Time'])
    filename = askopenfilename()
    #filename = '/Casablanca2.xlsx'
    ind = filename.find('.xlsx') - 1
    loc = ''
    while filename[ind] != '/':
        loc = filename[ind] + loc
        ind = ind - 1

    if 'Agadir' in loc:
        loc = 6
    elif 'Casablanca' in loc:
        loc = 2
    elif 'Nador' in loc:
        loc = 4
    elif 'Rabat' in loc:
        loc = 3
    elif 'Tangier' in loc:
        loc = 1
    elif 'Tetouan' in loc:
        loc = 5
    else:
        print('Error')
        raise ValueError
    
    df = pd.read_excel(filename)
    
    df['dateOfBirth'] = df['dateOfBirth'].dt.strftime('%Y-%b-%d %H:%I:%S')
    df['passportIssueDate'] = df['passportIssueDate'].dt.strftime('%Y-%b-%d %H:%I:%S')
    df['passportExDate'] = df['passportExDate'].dt.strftime('%Y-%b-%d %H:%I:%S')
    rows = df['family'].to_list()[-1]
    print(rows)
    for i in range(rows):

        df1 = df[df['family'] == i + 1]
        df1 = df1.reset_index(drop=1)
        fName = df1['fName']
        lName = df1['lName']
        DoB = df1['dateOfBirth']
        pNu = df1['passportNo']
        p_issue_date = df1['passportIssueDate']
        p_exp_date = df1['passportExDate']
        p_place = df1['passportIssuePlace']
    
        while True:
            try:
                # email = mail_generator.generate_email()
                email = "9wjsynm42b@isecmail.org"
                email_df = sele_code.main_sele_family(email, loc, fName, lName, DoB, pNu, p_issue_date, p_exp_date,p_place, df1.shape[0],email_df, instructions)
                # email_df = sele_code.main_sele_family(email, loc, fName, lName, DoB, pNu, p_issue_date, p_exp_date,p_place, df1.shape[0],email_df)

                print(fName, lName, pNu)
                break
            except:
                print('Error why?', fName, lName, pNu)
                break
    return email_df



out = family()
out.to_excel('Appointments_family'+str(time.time()) + '.xlsx')