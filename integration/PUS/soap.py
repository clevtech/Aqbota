__author__ = "Bauyrzhan Ospan"
__copyright__ = "Copyright 2018, Aqbota"
__version__ = "1.0.1"
__maintainer__ = "Bauyrzhan Ospan"
__email__ = "bospan@cleverest.tech"
__status__ = "Development"

import requests
import xml.dom.minidom
import datetime


def pus_data():
    url = "http://pls-test.post.kz/api/service/postamatHierarchy?wsdl"

    headers = {'content-type': 'text/xml'}


    file_name = "./templates/GETDATA.xml"

    with open(file_name, "r") as file:
        req = file.read()
        head = req.split("BARCODE")[0]
        tail = req.split("BARCODE")[1]

    barcode = "KZ030601009KZ"

    body = head+barcode+tail

    print(body)

    response = requests.post(url, data=body.encode('utf-8'), headers=headers)

    pretyy = xml.dom.minidom.parseString(response.content)
    pretty_xml_as_string = pretyy.toprettyxml()
    print(pretty_xml_as_string)


def income():
    url = "http://pls-test.post.kz/api/service/postamat?wsdl"

    headers = {'content-type': 'text/xml'}


    file_name = "./templates/INCOME.xml"

    with open(file_name, "r") as file:
        req = file.read()
        head = req.split("BARCODE")[0]
        mid = req.split("BARCODE")[1].split("INDEX")[0]
        tail = req.split("BARCODE")[1].split("INDEX")[1]

    barcode = "KZ030601009KZ"
    index = "600100"

    body = head+barcode+mid+index+tail

    print(body)

    response = requests.post(url, data=body.encode('utf-8'), headers=headers)

    pretyy = xml.dom.minidom.parseString(response.content)
    pretty_xml_as_string = pretyy.toprettyxml()
    print(pretty_xml_as_string)


def back():
    url = "http://pls-test.post.kz/api/service/postamat?wsdl"

    headers = {'content-type': 'text/xml'}


    file_name = "./templates/BACK.xml"

    with open(file_name, "r") as file:
        req = file.read()
        head = req.split("BARCODE")[0]
        mid = req.split("BARCODE")[1].split("INDEX")[0]
        tail = req.split("BARCODE")[1].split("INDEX")[1]

    barcode = "KZ030601009KZ"
    index = "600100"

    body = head+barcode+mid+index+tail

    print(body)

    response = requests.post(url, data=body.encode('utf-8'), headers=headers)

    pretyy = xml.dom.minidom.parseString(response.content)
    pretty_xml_as_string = pretyy.toprettyxml()
    print(pretty_xml_as_string)

# def

def send_sms(ID, PIN):
    url = "http://89.218.48.181:8080/altsmsgate/altsmsgate.wsdl?"
    headers = {'content-type': 'text/xml'}
    file_name = "./templates/sms.xml"
    with open(file_name, "r") as file:
        req = file.read()
        head = req.split("<!--body-->")[0]
        mid = req.split("<!--body-->")[1]
        mid_ID = mid.split("[ID]")[0]
        mid_date = mid.split("[ID]")[1].split("[date]")[0]
        mid_pin = mid.split("[ID]")[1].split("[date]")[1].split("[pin]")[0]
        mid_tail = mid.split("[ID]")[1].split("[date]")[1].split("[pin]")[1]
        tail = req.split("<!--body-->")[2]
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    body = mid_ID + ID + mid_date + date + mid_pin + PIN + mid_tail
    request = head
    request = request + body
    request = request + tail
    print(request)
    response = requests.post(url, data=request.encode('utf-8'), headers=headers)
    pretyy = xml.dom.minidom.parseString(response.content)
    pretty_xml_as_string = pretyy.toprettyxml()
    print(pretty_xml_as_string)
    return 1


if __name__ == "__main__":
    # pus_data()
    # back()
    send_sms("87778694240", "0605")
