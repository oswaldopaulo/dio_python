#TCP client example in python
import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Fail: {}".format(e))
        sys.exit()
    print("Socket Create OK")
    target_host  = input("Enter target host:")
    target_port = input("Enter target port:")

    try:
        s.connect((target_host,int(target_port)))
        print("Connected test 2s: {}:{}".format(target_host,target_port))
        s.shutdown(2)
        print("Test OK, Disconnect after 2s: {}:{}".format(target_host, target_port))
        print("")
    except socket.error as e:
        print("Fail {}".format(e))
        sys.exit()
if __name__ == "__main__":
    main()
