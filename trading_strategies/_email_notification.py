import os
from datetime import datetime

import smtplib
from email.message import EmailMessage
import mimetypes

def send_email(self, order_response: dict) -> None:
    try:
        email_config = self.config['email']

        msg = EmailMessage()
        msg['From'] = email_config['sender']
        msg['To'] = email_config['receiver']
        date = datetime.now().strftime("%Y%m%d")

        # Decide the subject and the content
        if order_response['success']:
            msg['Subject'] = "[{}] {} - Success {}".format(email_config['subject'], self.config['quote_token'] + self.config['base_token'], date)
            msg.set_content("Congratuations! The order is created.\nOrder info:\nSymbol: {}\tPrice: {}\tOrder id: {}".format(
                order_response['response']['symbol'], order_response['response']['price'], order_response['response']['orderId']))
        else:
            msg['Subject'] = "[{}] {} - Fail {}".format(email_config['subject'], self.config['quote_token'] + self.config['base_token'], date)
            msg.set_content("Order is not created, please check the log file.")

        # Attach the log file
        with open(self._log_path, 'rb') as f:
            file_data = f.read()
            maintype, subtype = mimetypes.guess_type(self._log_path)[0].split('/')
            msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=os.path.basename(self._log_path))

        # Send the email
        with smtplib.SMTP_SSL(email_config['smtp_server'], email_config['smtp_port']) as server:
            server.login(email_config['sender'], email_config['app_password'])
            server.send_message(msg)

        self.logger.info("Email sent successfully.")

    except Exception as error:
        self.logger.error(f"Failed to send email: {error}")

if __name__ == '__main__':
    pass