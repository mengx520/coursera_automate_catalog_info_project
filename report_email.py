#!/usr/bin/env python3
import os, datetime
import reports
import emails

# Processed Update on <Today's date>
date_time = datetime.datetime.now().strftime('%Y-%m-%d')

path = "/home/student-01-536256626c85/supplier-data/descriptions/"
files = os.listdir(path)

# process the text data from the supplier-data/descriptions

def generate_pdf(path):
    pdf = ''
    for file in files:
        if '.txt' in file:
            with open(path + file, 'r') as f:
                data = f.readlines()
                name = data[0].strip()
                weight = data[1].strip()
                pdf += 'name: ' + name + '<br/>' + 'weight: ' + weight + '<br/><br/>'
    return pdf

# the main method which will process the data and call the generate_report method from the reports module
# You will need to pass the following arguments to the reports.generate_report method: the text description processed from the text files as the paragraph argument, the report title as the title argument, and the file path of the PDF to be generated as the attachment argument (use ‘/tmp/processed.pdf')
if __name__ == "__main__":
    title = "Processed Updated on  " + date_time
    paragraph = generate_pdf(path)
    reports.generate_report('/tmp/processed.pdf', title, paragraph)

# Send report through email
# Once you define the generate_email and send_email methods, call the methods under the main method after creating the PDF report
sender = 'automation@example.com'
receiver = "{}@example.com".format(os.environ['USER'])
subject = 'Upload Completed - Online Fruit Store'
body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email'
attachment = '/tmp/processed.pdf'

#generate email for the online fruit store report and pdf attachment
message = emails.generate_email(sender, receiver, subject, body, attachment)
emails.send_email(message)