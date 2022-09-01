import pymysql
from PyPDF2 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import random
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def Connect():
    #conn = pymysql.connect(host='127.0.0.1', user='root', password='', database='covid_vaccine')
    conn=pymysql.connect(host='13.232.35.56',user='shivani',password='shivani@123',database='shivani')
    return conn

def createPDF(name,age,gender,aadhaar,vaccineName,date,hospitalName,email):
    try:
        buffer = BytesIO()

        # create a new PDF with Reportlab
        p = canvas.Canvas(buffer, pagesize=A4)
        p.drawString(x=310, y=610, text=name)
        p.drawString(x=310, y=587, text=str(age))
        p.drawString(x=310, y=567, text=gender)
        p.drawString(x=355, y=541, text=str(aadhaar), wordSpace=2)
        p.drawString(x=310, y=518, text=str(random.randint(9856321452, 9856321485)), wordSpace=2)
        p.drawString(x=310, y=431, text=vaccineName, wordSpace=2)
        p.drawString(x=310, y=405, text=str(date), wordSpace='5')
        p.drawString(x=310, y=327, text=hospitalName)
        p.showPage()
        p.save()

        # move to the beginning of the StringIO buffer
        buffer.seek(0)
        newPdf = PdfFileReader(buffer)

        #######DEBUG NEW PDF created#############
        # pdf1 = buffer.getvalue()
        # open('pdf1.pdf', 'wb').write(pdf1)
        #########################################
        # read your existing PDF
        existingPdf = PdfFileReader(open('resources/certTemplate.pdf', 'rb'))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = existingPdf.getPage(0)
        page.mergePage(newPdf.getPage(0))
        output.addPage(page)
        # finally, write "output" to a real file
        outputStream = open('certificate.pdf', 'wb')
        output.write(outputStream)
        outputStream.close()
        flag = sendEmail(email=email)
        if flag:
            return True
        else:
            return False
    except:
        return False


def sendEmail(email):
    try:
        subject = "An email with attachment from Python"
        body = "This is an email with attachment sent from Python"
        sender_email = "teampython40@gmail.com"
        receiver_email = email
        password = 'covid@123'

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        filename = "certificate.pdf"  # In same directory as script

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        return True
    except:
        return False