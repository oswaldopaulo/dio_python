import ipaddress

ips = '192.168.0.0/26'
rede = ipaddress.ip_network(ips, strict=False)

for ip in rede:
    print(ip)