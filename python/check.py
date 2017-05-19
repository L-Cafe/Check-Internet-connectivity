import os
import telnetlib
import socket

def reboot_router():
    routerHost = os.environ["routerAddress"]
    routerUser = os.environ["routerUsername"]
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
        print(ex)
        return False

if checkInternet():
    print("The specified host seems to be reachable from here.")
else:
    print("Host is unreachable. Internet connection might be down. Rebooting router.") # TODO: Wait for 5 seconds and check again.
    reboot_router()                                                                    # TODO: Check if the router is reachable. Otherwise, exit and do nothing.
