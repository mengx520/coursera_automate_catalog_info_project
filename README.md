# Automate updating catalog information
https://www.coursera.org/learn/automating-real-world-tasks-python/home/week/4

### Introduction
Develop a system for and online fruit store that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. Gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.
Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs).

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong.

What you'll do
- Write a script that summarizes and processes sales data into different categories
- Generate a PDF using Python
- Automatically send a PDF by email
- Write a script to check the health status of the system

### write a Python script named changeImage.py to process the supplier images. You will be using the PIL library to update all images within ~/supplier-data/images directory to the following specifications:

> Size: Change image resolution from 3000x2000 to 600x400 pixel
> Format: Change image format from .TIFF to .JPEG

### write a script named supplier_image_upload.py that takes the jpeg images from the supplier-data/images directory that you've processed previously and uploads them to the web server fruit catalog
To add fruit images and their descriptions from the supplier on the fruit catalog web-server, create a new Python script that will automatically POST the fruit images and their respective description in JSON format.Write a Python script named run.py to process the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory. The script should turn the data into a JSON dictionary by adding all the required fields, including the image associated with the fruit (image_name), and uploading it to http://[linux-instance-external-IP]/fruits using the Python requests library.

*The final JSON object should be similar to*
```
{"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"}
```
### Generate a PDF report and send it through email
Once the images and descriptions have been uploaded to the fruit store web-server, you will have to generate a PDF file to send to the supplier, indicating that the data was correctly processed. To generate PDF reports, you can use the ReportLab library. The content of the report should look like this:
```
[blank line]

name: Apple

weight: 500 lbs

[blank line]

name: Avocado

weight: 200 lbs

[blank line]
```
### Create a script reports.py to generate PDF report to supplier 
### Using the reportlab Python library, define the method generate_report to build the PDF reports processed.pdf.
### Create another script named report_email.py to process supplier fruit description data from supplier-data/descriptions directory
Import all the necessary libraries(os, datetime and reports) that will be used to process the text data from the supplier-data/descriptions directory into the format below:
```
name: Apple

weight: 500 lbs

[blank line]

name: Avocado

weight: 200 lbs

[blank line]
```
### Send report through email
Once the PDF is generated, you need to send the email using the emails.generate_email() and emails.send_email() methods.
- Create emails.py
- Define generate_email and send_email methods by importing necessary libraries.

### Health check
write a Python script named health_check.py that will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:
- Report an error if CPU usage is over 80%
- Report an error if available disk space is lower than 20%
- Report an error if available memory is less than 500MB
- Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"

Complete the script to check the system statistics every 60 seconds, and in event of any issues detected among the ones mentioned above, an email should be sent with the following content:
```
From: automation@example.com
To: username@example.com
```
