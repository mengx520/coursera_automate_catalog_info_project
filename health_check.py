#!/usr/bin/env python3

# check CPU usage, disk space, available memory and name resolution

import psutil, shutil
import socket
import emails
import os,sys
import time


# Report an error if CPU usage is over 80%
def cpu_check():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent < 80.0

# Report an error if available disk space is lower than 20%
def disk_check():
    disk_usage = psutil.disk_usage('/')
    return disk_usage.percent < 80.0

# Report an error if available memory is less than 500MB
def memory_check():
    memory = psutil.virtual_memory()
    THRESHOLD = 500 * 1024 * 1024  
    return memory.available < THRESHOLD

# Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
def hostname_check():
    ip = socket.gethostbyname('localhost')
    return ip == '127.0.0.1'

# send email
# Send report through email
# Once you define the generate_email and send_email methods, call the methods under the main method after creating the PDF report
sender = 'automation@example.com'
receiver = "{}@example.com".format(os.environ['USER'])
body = 'Please check your system and resolve the issue as soon as possible.'

while True:
    if cpu_check() == False:
        subject = 'Error - CPU usage is over 80%'
        message = emails.generate_email(sender, receiver, subject, body)
        emails.send_email(message)

    if disk_check() == False:
        subject = 'Error - Available disk space is less than 20%'
        message = emails.generate_email(sender, receiver, subject, body)
        emails.send_email(message)

    if memory_check() == False:
        subject = 'Error - Available memory is less than 500MB'
        message = emails.generate_email(sender, receiver, subject, body)
        emails.send_email(message)

    if hostname_check() == False:
        subject = 'Error - localhost cannot be resolved to 127.0.0.1'
        message = emails.generate_email(sender, receiver, subject, body)
        emails.send_email(message)
        
    #  check the system statistics every 60 seconds
    time.sleep(60)
