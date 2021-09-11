from smtplib import SMTP
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Make the content of index.html a template object
html = Template(Path('index.html').read_text())

# Set up email headers
email = EmailMessage()  # This is going to be our email object
email['from'] = 'Fake Guy'
email['to'] = 'destination@gmail.com'
email['subject'] = 'Congratulations! You just won 1,000,000 dollars!'

email.set_content(html.substitute(name='Pete', number='999,999'), 'html')

# Use smtplib server to log into our gmail to send this email.
try:
    with SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('fake@gmail.com', '********')
        smtp.send_message(email)
        smtp.close()
        print('All good boss!')
except:
    print("Unable to send the email")
