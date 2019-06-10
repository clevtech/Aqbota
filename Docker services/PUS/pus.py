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
import re
from pymongo import MongoClient
import secrets


def save_db(log, name):
    # client = MongoClient('mongodb://database:27017/')
    # db = client['PUS']
    # collection = db[name]
    # collection.insert_one(log)
    print("===========================================")
    print("Сохранил в логи следующее: ")
    pprint(log)
    print("===========================================")
    print()


def take_db(barcode, name):
    client = MongoClient('mongodb://database:27017/')
    db = client['PUS']
    collection = db[name]
    result = collection.find_one({"barcode": barcode})
    return result


def printxml(res):
    pretyy = xml.dom.minidom.parseString(res.content)
    pretty_xml_as_string = pretyy.toprettyxml()
    print(pretty_xml_as_string)


def pus_data(barcode, address):
    url = "http://pls-test.post.kz/api/service/postamatHierarchy?wsdl"
    url2 = "http://pls-test.post.kz/api/service/postamat?wsdl"

    headers = {'content-type': 'text/xml'}

    file_name = "./templates/GETDATA.xml"
    file_name2 = "./templates/chech_money.xml"

    with open(file_name, "r") as file:
        req = file.read()
        req = req.replace("BARCODE", barcode)
        print("=================================================")
        print("Отправляю запрос для получения данных о посылке на url: " + str(url))
        print()
        pprint(req)
        print("--------------------------------------------------")

    response = requests.post(url, data=req.encode('utf-8'), headers=headers)

    print("=================================================")
    print("Принял ответ от сервера: ")
    print()
    printxml(response)
    print("--------------------------------------------------")


    with open(file_name2, "r") as file:
        req = file.read()
        req = req.replace("BARCODE", barcode)
        print("=================================================")
        print("Отправляю запрос для получения данных о наложке на url: " + str(url2))
        print()
        pprint(req)
        print("--------------------------------------------------")

    response2 = requests.post(url2, data=req.encode('utf-8'), headers=headers)
    print("=================================================")
    print("Принял ответ от сервера: ")
    print()
    printxml(response2)
    print("--------------------------------------------------")

    cash_check = re.findall("<ns2:amount>(.*?)</ns2:amount>", str(response2.content))
    if cash_check:
        if cash_check[0] != "0":
            cash_check = False
        else:
            cash_check = True
    else:
        cash_check = True

    log = {
        "address": address,
        'barcode': barcode,
        "client": re.findall("<Rcpn>(.*?)</Rcpn>", str(response.content.decode("utf-8")))[0],
        "time": datetime.datetime.now(),
        "phone": re.findall("<RcpnPhone>(.*?)</RcpnPhone>", str(response.content.decode("utf-8")))[0],
        "cash check": cash_check
    }

    save_db(log, "data")

    if cash_check:
        return log["phone"]
    else:
        return False


def income(barcode):
    url = "http://pls-test.post.kz/api/service/postamat?wsdl"

    headers = {'content-type': 'text/xml'}

    file_name = "./templates/INCOME.xml"

    with open(file_name, "r") as file:
        req = file.read()
        req = req.replace("BARCODE", barcode)
        print("=================================================")
        print("Отправляю запрос на хранение посылки на url: " + str(url))
        print()
        pprint(req)
        print("--------------------------------------------------")

    response = requests.post(url, data=req.encode('utf-8'), headers=headers)
    print("=================================================")
    print("Принял ответ от сервера: ")
    print()
    printxml(response)
    print("--------------------------------------------------")


    status = re.findall("<ns3:code>(.*?)</ns3:code>", str(response.content.decode("utf-8")))[0]

    info = re.findall("<ns3:name>(.*?)</ns3:name>", str(response.content.decode("utf-8")))[0]

    pin = ''.join(secrets.choice("0123456789") for i in range(4))

    log = {
        "status": status,
        "info": info,
        "barcode": barcode,
        "time": datetime.datetime.now(),
        "pin": pin
    }

    save_db(log, "income")

    return status, info, pin


def given(barcode):
    url = "http://pls-test.post.kz/api/service/postamat?wsdl"

    headers = {'content-type': 'text/xml'}

    file_name = "./templates/given.xml"

    with open(file_name, "r") as file:
        req = file.read()
        req = req.replace("BARCODE", barcode)
        print("=================================================")
        print("Отправляю запрос на выдачу посылки на url: " + str(url))
        print()
        pprint(req)
        print("--------------------------------------------------")

    response = requests.post(url, data=req.encode('utf-8'), headers=headers)
    print("=================================================")
    print("Принял ответ от сервера: ")
    print()
    printxml(response)
    print("--------------------------------------------------")

    status = re.findall("<ns3:code>(.*?)</ns3:code>", str(response.content.decode("utf-8")))[0]

    info = re.findall("<ns3:name>(.*?)</ns3:name>", str(response.content.decode("utf-8")))[0]

    log = {
        "status": status,
        "info": info,
        "barcode": barcode,
        "time": datetime.datetime.now()
    }

    save_db(log, "given")

    return status, info


def back(barcode):
    url = "http://pls-test.post.kz/api/service/postamat?wsdl"

    headers = {'content-type': 'text/xml'}

    file_name = "./templates/given.xml"

    with open(file_name, "r") as file:
        req = file.read()
        req = req.replace("BARCODE", barcode)
        print("=================================================")
        print("Отправляю запрос на возврат посылки на url: " + str(url))
        print()
        pprint(req)
        print("--------------------------------------------------")

    response = requests.post(url, data=req.encode('utf-8'), headers=headers)
    print("=================================================")
    print("Принял ответ от сервера: ")
    print()
    printxml(response)
    print("--------------------------------------------------")

    status = re.findall("<ns3:code>(.*?)</ns3:code>", str(response.content.decode("utf-8")))[0]

    info = re.findall("<ns3:name>(.*?)</ns3:name>", str(response.content.decode("utf-8")))[0]

    log = {
        "status": status,
        "info": info,
        "barcode": barcode,
        "time": datetime.datetime.now()
    }

    printxml(response)

    save_db(log, "back")

    return status, info


def send_sms(phones, pins, place, barcode):

    url = "http://92.46.190.22:8080/altsmsgate/altsmsgate.wsdl"
    headers = {'content-type': 'text/xml'}
    file_name = "./templates/sms.xml"
    text = "Робот почтальон приехал доставить Вам посылку [barcode]. Он ждет вас в [place] до [time]." \
           " Введите [pin] для получения доступа на дисплее робота."
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
            .replace("[pin]", pins[i]).replace("[place]", place).replace("[barcode]", barcode[i])
        body2 = body.replace("[text]", text1).replace("[phone]", phones[i])
        bodies += body2

    request = req.replace("[body]", bodies)
    print("Sended request is:")
    print()
    pprint(request)
    print()
    response = requests.post(url, data=request.encode('utf-8'), headers=headers)

    print("=================================================")
    print("Отправляю запрос смс посылки на url: " + str(url))
    print()
    pprint(req)
    print("--------------------------------------------------")
    print("=================================================")
    print("Принял ответ от сервера: ")
    print()
    printxml(response)
    print("--------------------------------------------------")

    ids = re.findall("SmsId>([0-9]+)</ns2:AltSms", str(response.content.decode("utf-8")))
    statuses = re.findall("AltSmsStatus>(.*?)</ns2:AltSmsStatus", str(response.content.decode("utf-8")))

    smses = []

    log = {
        "place": place,
        "sms": [],
        "time": datetime.datetime.now()
    }

    try:
        for i in range(len(phones)):
            smses.append({"phone": phones[i], "pin": pins[i], "barcode": barcode[i], "status": statuses[i]})
    except:
        for i in range(len(phones)):
            smses.append({"phone": phones[i], "pin": pins[i], "barcode": barcode[i], "status": None})

    log["sms"] = smses

    save_db(log, "sms")


def send_sms_save(phones, pins, place, barcode):

    url = "http://92.46.190.22:8080/altsmsgate/altsmsgate.wsdl"
    headers = {'content-type': 'text/xml'}
    file_name = "./templates/sms.xml"
    text = "Ваша посылка [barcode] передана роботу-курьеру на хранение, " \
           "в ближайшее время ожидайте доставку по адресу [place]"
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
        text1 = text0.replace("[place]", place).replace("[barcode]", barcode[i])
        body2 = body.replace("[text]", text1).replace("[phone]", phones[i])
        bodies += body2

    request = req.replace("[body]", bodies)
    print("Sended request is:")
    print()
    pprint(request)
    print()
    response = requests.post(url, data=request.encode('utf-8'), headers=headers)

    print("=================================================")
    print("Отправляю запрос смс хранения на url: " + str(url))
    print()
    pprint(req)
    print("--------------------------------------------------")
    print("=================================================")
    print("Принял ответ от сервера: ")
    print()
    printxml(response)
    print("--------------------------------------------------")

    ids = re.findall("SmsId>([0-9]+)</ns2:AltSms", str(response.content.decode("utf-8")))
    statuses = re.findall("AltSmsStatus>(.*?)</ns2:AltSmsStatus", str(response.content.decode("utf-8")))

    smses = []

    log = {
        "place": place,
        "sms": [],
        "time": datetime.datetime.now()
    }

    try:
        for i in range(len(phones)):
            smses.append({"phone": phones[i], "pin": pins[i], "barcode": barcode[i], "status": statuses[i]})
    except:
        for i in range(len(phones)):
            smses.append({"phone": phones[i], "pin": pins[i], "barcode": barcode[i], "status": None})

    log["sms"] = smses

    save_db(log, "sms_save")


if __name__ == "__main__":
    print("Начало теста: " + str(datetime.datetime.now()))
    print("########################################")
    print()
    print()
    print("########################################")
    print("Проверка посылки")
    print("########################################")
    print()
    print()
    phone = pus_data("KZ030601009KZ", "Astana HUB")
    print()
    print()
    print("########################################")
    print("Хранение посылки")
    print("########################################")
    print()
    print()
    status, info, pin = income("KZ030601009KZ")
    print()
    print()
    print("########################################")
    print("СМС о хранении посылки")
    print("########################################")
    print()
    print()
    send_sms_save(["77771111111"], [pin], "Astana HUB", ["KZ030601009KZ"])
    print()
    print()
    print("########################################")
    print("СМС о доставке посылки")
    print("########################################")
    print()
    print()
    send_sms(["77771111111"], [pin], "Astana HUB", ["KZ030601009KZ"])
    print()
    print()
    print("########################################")
    print("Вручение посылки клиенту")
    print("########################################")
    print()
    print()
    given("KZ030601009KZ")
    print()
    print()
    print("########################################")
    print("Тест сценария возврата курьеру: хранение посылки")
    print("########################################")
    print()
    print()
    income("KZ030601009KZ")
    print()
    print()
    print("########################################")
    print("Тест сценария возврата курьеру: возврат")
    print("########################################")
    print()
    print()
    back("KZ030601009KZ")
    print()
    print()
    print("########################################")
    print("Конец теста: " + str(datetime.datetime.now()))
    print("########################################")
    print()
    print()
