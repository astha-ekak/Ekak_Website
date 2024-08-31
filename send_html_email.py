
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from loguru import logger



logger.add("send_html_email.log", level="INFO", rotation="100 MB")

def send_mail(body,subject_text:str,email_data,customer_email='info@ekak.in'):
    
    # print(customer_email,"Customer Email")
    try:
        message = MIMEMultipart()
        logger.info("Sending Email Start__")
        message['Subject'] = subject_text
        message['From'] = 'tools@ekak.in'
        message['To'] = 'richa@ekak.in'
        message['Bcc'] = 'info@ekak.in'
        # message['Bcc'] = ''
        logger.info(f"_Sender Email : {str(message['From'] ) }")
        logger.info(f"_Reciever Email : {str(message['To'] ) }")
        logger.info(f"_Subject : {str(message['Subject']) }")
        logger.info(f"_Email_data : \n{email_data}")
        body_content = body
        message.attach(MIMEText(body_content, "html"))
        msg_body = message.as_string()

        server = SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(message['From'], "yzatfktargzlkkzf")
        server.sendmail(message['From'], [message['To'],message['Bcc']], msg_body)
        server.quit()
        logger.info('_Email Send ')
    except Exception as E:
        logger.exception("Error Occurs ")
        print("\n\n\n\n Mail Not Send")
        logger.debug("No Mail Send")
        print("Error Occurs :",E)
        
        
if __name__ == '__main__':
    send_mail('Your Context',"argus_device:str","email_data",'astha@ekak.in')