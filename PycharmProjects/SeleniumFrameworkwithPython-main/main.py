# import pdfkit
#
# #define path to wkhtmltopdf.exe
# path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
#
# #define html file path
# file_path = "Reports/Reports.html"
# # _html = '''<html><body><h1>Hello world</h1></body></html>'''
# # pdfkit.from_string(_html), file_path)
#
# #point pdfkit configuration to wkhtmltopdf.exe
# config = pdfkit.configuration(wkhtmltopdf = path_to_wkhtmltopdf)
#
# #convert html file to pdf
# pdfkit.from_file(file_path, output_path= 'report.pdf', configuration = config)


# import smtplib,ssl
# import pandas as pd
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
# from email import encoders
# # from flask.json import tag
# # from github3.repos import tag
# import os
# from email.message import EmailMessage
# import pytest
#
#
# @pytest.mark.trylast
# def send_email(username,password,to_recipients,email_subject,email_body,extra_headers=None):
#     send_from=username
#     message = EmailMessage()
#     msg = MIMEMultipart()
#     msg['From'] = send_from
#     msg['To'] = to_recipients
#     date_str = pd.Timestamp.today().strftime('%Y-%m-%d')
#     msg['Subject'] = f'{email_subject} - {date_str}'
#
#
#     attach_file_name = './/Reports//Reports.html'
#     with open(attach_file_name,'rb') as f:
#         attach_file = MIMEApplication(f.read())
#
#     attach_file.add_header('Content-Disposition', f"attachment; filename={attach_file_name}")
#     msg.attach(attach_file)
#     body = email_body
#     body = MIMEText(body)
#     msg.attach(body)
#     msg.attach(attach_file)
#
#     # send_email(msg, 'accounts/punters.html')
#     # email_string = msg.as_string()
#
#     context = ssl.create_default_context()
#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.ehlo()  # Can be omitted
#         server.starttls(context=context)
#         server.ehlo()  # Can be omitted
#         server.login(send_from,password)
#         server.sendmail(send_from,to_recipients,msg.as_string())
#
# df = pd.read_csv(".//TestData/file3.csv")
# emails = [email for email in df["contact.businessEmail"]]
# names = [firstname+" "+lastname for firstname,lastname in zip(df["contact.firstName"],df["contact.lastName"])]
#
# for recipient,name in zip(emails,names):
#     send_email(username='rajesh.chintala@kanerika.com',password='ujjonjkjotivypzh',to_recipients=recipient,email_subject="Punters reports",
#            email_body="Hey "+name+", \n\n This is punters page html reports." )
#            #  email_body = "Hey "+name+", \n\n "+attachement+"")