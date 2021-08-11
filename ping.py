import os


with open('ips.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        os.system('ping -n 2 {}'.format(ip))
