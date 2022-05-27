password = "‎𓏵𝖄𝕬𝕸𝕬𝕿𝕺𓏵"
nickname = "nnnnnn"
#___________________________
#___________________________

import os
import time
import hmac
from hashlib import sha1
try:
	import string, random, requests, secmail, pyshorteners
	from aminofix import Client
	from bs4 import BeautifulSoup
	from time import sleep
	import time
	from aminofix.lib.util.exceptions import ActionNotAllowed, IncorrectVerificationCode
except:
	os.system("pip install amino.fix -U")
	os.system("pip install secmail")
	os.system("pip install requests")
	os.system("pip install bs4")
	os.system("pip install pyshorteners")


def captcha(url):
    return requests.post("https://captcha-do-mega.herokuapp.com/", data={"text": url}).json()['captcha']


def gerar_email():
    def gerar_aleatorio(size=16, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    email = "mhat-" + gerar_aleatorio() + "@wwjmp.com"
    return email


def deviceId():
    identifier = os.urandom(20)
    return ("42" + identifier.hex() + hmac.new(bytes.fromhex("02B258C63559D8804321C5D5065AF320358D366F"), b"\x42" + identifier, sha1).hexdigest()).upper()


def get_link(email):
    try:
        mail = secmail.SecMail()
        sleep(2.5)
        inbox = mail.get_messages(email)
        for Id in inbox.id:
            msg = mail.read_message(email=email, id=Id).htmlBody
            bs = BeautifulSoup(msg, 'html.parser')
            images = bs.find_all('a')[0]
            url = (images['href'])
            if url is not None:
                return url
    except:
        pass


def encurtar_link(link):
    ps = pyshorteners.Shortener()
    return ps.tinyurl.short(fr"{link}")


def log(cli: Client, email, password, device):
    try:
        cli.login(email, password)
        cli.join_community("252508015")
        cli.join_community("232923843")
        SID = f"{cli.sid}"
        with open("accounts.json", 'a') as x:
            acc = f'\n{{\n"email": "{email}",\n"password": "{password}",\n"device": "{device}",\n"SID": "{SID}"\n}},'
            x.write(acc)
            X=open("emails.txt","a")
            X.write(f"{email}\n")
            print(">> Save account! <<")

    except Exception as b:
        print(b)


def reset_dj():
    with open("device.json", 'w') as x:
        x.close()


def threadit(password):
    print("\n[WARNING] You can create 5 accounts per VPN")
    contador = 0

    while True:
        reset_dj()
        try:
            if contador == 500:
                print("Change the VPN to continue creating accounts!")
                
                os.system("clear")

            email = gerar_email()
            device = deviceId()
            print(f"\nGenerating email {email}...")
            client = Client(device)
            client.request_verify_code(email)
            link = get_link(email)
            print(link)
            codigo = captcha(link)
            print(codigo)
            client.register(nickname=nickname, email=email, password=password, verificationCode=codigo, deviceId=device)

            log(client, email, password, device)
            contador += 1

        except IncorrectVerificationCode:
            print("Incorrect code")

        except ActionNotAllowed:
            cx=input("\tchange vpn:")
            os.system("clear")
            

        except Exception as g:
            print(g)
      
      
threadit(password)
