import argparse
import imghdr
import os.path
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# from lib2to3.pgen2 import driver
from pathlib import Path
from turtle import pd
import os
import sys





from utilites.customlogger import LogGen
from utilites.readProperities import ReadConfig

driver = None


import pytest
from selenium import webdriver
# driver = None
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
# from py.xml import html

# from webdriver_manager.chrome import ChromeDriverManager
# # from webdriver_manager.core import driver
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager


@pytest.fixture()
def setup(request, browser):
    global driver
    # driver = webdriver.Chrome(executable_path=r'C:\Users\admin\PycharmProjects\SeleniumFrameworkwithPython-main\utilites\chromedriver.exe')
    # return driver

    if browser == 'chrome':
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = webdriver.Chrome()
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox()
        # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        #driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    elif browser == 'ie':
        driver = webdriver.Ie()
        # driver = webdriver.Ie(IEDriverManager().install())
        print("Launching ie browser.........")
    elif browser == 'edge':
        driver = webdriver.Edge()
        # driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching edge browser.........")
    else:
        print("provide valid browser")
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #     #driver = driver=webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\PytestHybridframework\\utilites\\chromedriver.exe')
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    # parser.addoption("--browser")
    # argparse.addoption("--browser")
    parser = argparse.ArgumentParser(
         description='Description of my argument parser.')
    parser.add_argument(
        '--browser',
        action=argparse.BooleanOptionalAction,
        default=False,
        help='Description of your feature.',
    )
@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

#######################pytest html report ###########################
# it hooks for adding environment info to html report
def pytest_configure (config):
    config._metadata['Project Name'] = 'Punters'
    config._metadata['Module Name'] = 'customer'
    config._metadata['Tester'] = 'Rajesh'

# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    # metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)

logger = LogGen.loggen()
baseUrl = ReadConfig.getApplicationUrl()
# @pytest.fixture()
# def chrome_driver_init(request, setup):
    # logger.info("**********************************Testing homepage title***********************************")
    # driver = setup
    # driver.get(baseUrl)
    # driver.maximize_window()
    # request.cls.driver = driver
    #
    # yield driver
    # driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.Punters.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
#         # if report.failed or xfail and "page" in item.funcargs:
#             # # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
#             # # file_name = str(int(round(time.time() * 1000))) + ".png"
            file_name = report.nodeid.replace("::", "_") + ".png"
#             # _capture_screenshot(file_name)
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            # driver.WebElement.screenshot(destinationFile)

            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.html(html))
            # extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extra = extra

@pytest.fixture(scope="function")
def set_up_tear_down(page) -> None:

    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("https://www.punters.com")
    yield page

@pytest.fixture()
def set_up_tear_down_no_login(page):
    page.set_viewport_size({"width": 1536, "height": 834})
    page.goto("https://www.punters.com")
    yield page


@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "Punters Report"



# import smtplib,ssl
# import pandas as pd
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
# from email import encoders
# # from flask.json import tag
# # from github3.repos import tag
# import os
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


# import pdfkit
# import random as rd
#    # pdf = rd.randint(23,100)
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
# pdfkit.from_file(file_path, output_path= 'TestData/pdf/Report.pdf', configuration = config)

