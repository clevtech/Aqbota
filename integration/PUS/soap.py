__author__ = "Bauyrzhan Ospan"
__copyright__ = "Copyright 2018, Aqbota"
__version__ = "1.0.1"
__maintainer__ = "Bauyrzhan Ospan"
__email__ = "bospan@cleverest.tech"
__status__ = "Development"

import requests
import xml.dom.minidom
import datetime
from pprint import pprint


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


def send_sms(phones, pins, place):

    url = "http://92.46.190.22:8080/altsmsgate/altsmsgate.wsdl"
    headers = {'content-type': 'text/xml'}
    file_name = "./templates/sms.xml"
    text = "Vam postupila posylka v Robopochtaliyon: Astana, Mangilik El prospekt, " \
           "C4.6. Kod dostupa [pin]. Srok dlya zabora posylki 30 minut."
    text = "Робот почтальон приехал доставить Вам посылку. Он ждет вас в [place] до [time]." \
           " Введите [pin] для получения доступа."
    body = "<sch:Sms>" \
            "<sch:SmsText>[text]</sch:SmsText>" \
            "<sch:TelegramText>[text]</sch:TelegramText>" \
            "<sch:PostKzText>[text]</sch:PostKzText>" \
            "<sch:PhoneNumber>[phone]</sch:PhoneNumber>" \
            "</sch:Sms>"

    with open(file_name, "r") as file:
        req = file.read()

    time = (datetime.datetime.now() + datetime.timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M")


    bodies = ""

    for i in range(len(phones)):
        text0 = text
        text1 = text0.replace("[time]", time)\
            .replace("[pin]", pins[i]).replace("[place]", place)
        body = body.replace("[text]", text1).replace("[phone]", phones[i])
        bodies += body

    request = req.replace("[body]", bodies)
    print("Sended request is:")
    print()
    pprint(request)
    print()
    response = requests.post(url, data=request.encode('utf-8'), headers=headers)
    pretyy = xml.dom.minidom.parseString(response.content)
    pretty_xml_as_string = pretyy.toprettyxml()
    print()
    print("Responce is: ")
    print()
    print(pretty_xml_as_string)
    return 1


def check_sms():
    url = "http://92.46.190.22:8080/altsmsgate/altsmsgate.wsdl"
    headers = {'content-type': 'text/xml'}
    file_name = "./templates/checksms.xml"
    with open(file_name, "r") as file:
        req = file.read()
        response = requests.post(url, data=req.encode('utf-8'), headers=headers)
        pretyy = xml.dom.minidom.parseString(response.content)
        pretty_xml_as_string = pretyy.toprettyxml()
        print(pretty_xml_as_string)

if __name__ == "__main__":
    # pus_data()
    # back()
    send_sms(["77778694240"], ["0605"], "Astana HUB")
