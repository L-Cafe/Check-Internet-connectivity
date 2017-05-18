import os
import telnetlib
import socket

def reboot_router():
    routerHost = os.environ["routerAddress"]
    routerUser = os.environ["routerUser"]
    routerPassword = os.environ["routerPassword"]

    tn = telnetlib.Telnet(routerHost)

    tn.read_until(b"Login: ")
    tn.write(routerUser.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(routerPassword.encode('ascii') + b"\n")

    tn.write(b"reboot\n")

    print(tn.read_all().decode('ascii'))
    return

def checkInternet():
    checkHost = "8.8.8.8"
    checkPort = 53
    checkTimeout = 30
    try:
        socket.setdefaulttimeout(checkTimeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((checkHost, checkPort))
        return True
    except Exception as ex:
        print(ex.message)
        return False

if checkInternet():
    pass
else:
    reboot_router()