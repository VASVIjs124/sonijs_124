import socket

def get_ip_from_url():
    name = input("Enter site name : ")
    tld = input("Enter top level domain name : ")
    fulladdress = f"www.{name}{tld}"

    try:
    	ipaddress = socket.gethostbyname(fulladdress)
    	print(f"your url is {fulladdress}")
    	print(f"your ip is {ipaddress}")
    except socket.error as e:
        print("Error:",e)

   if__name__=="__main__":
   	get_ip_from_url()
       
    

