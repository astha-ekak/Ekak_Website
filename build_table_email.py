from pretty_html_table import build_table
import pandas as pd
import send_html_email
# email_data=[[1,2],[1,2]]


user_data = {
    'Name': ["John"],
    "Age": ["Age"]

}

def get_pretty_table(userDate):
    """
    Its Return HTML TABLE
    :return:
    """
    # gdp_dict = {'Name': e_name,
    # 'Recorded Entry time':e_capture_time,
    # 'Expected Entry time' : e_actual_entry_time,
    # 'Threshold Entry time' : '10 Min',
    # 'Status' : e_status ,
    # }

    # data = pd.DataFrame(gdp_dict)
    data = pd.DataFrame(userDate)
    # data.to_csv('Users.csv', sep='\t', index=False,header=True)
    return data






def table_email(user_data):
    
    get_pretty_table(user_data)

    email_data = get_pretty_table(userDate=user_data)

    output = build_table(email_data, 'blue_dark')
    print(output)

    output = build_table(email_data, 'blue_dark')
    # #print(output)
    img = '''<img src="https://user-images.githubusercontent.com/100748027/218997643-45cb0b1b-d6cf-439f-a558-32e4b74df9d0.png" alt="img" />'''

    send_html_email.send_mail(img+output, "New Form Submited",
                            str(email_data), customer_email='astha@ekak.in')
    
    # send_mail('Your Context',"argus_device:str","email_data",'astha@ekak.in')


if __name__ =='__main__':
    user_data = {
        'Name': ["Kevin"],
        "Age": ["Age"]

    }
    table_email(user_data=user_data)