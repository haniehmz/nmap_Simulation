import socket
import timeit
import json

def is_port_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        
        s.close()
        return True
    except:
        return False
    
def get_service_name (port):
    try:
        service=socket.getservbyport(port)
    except:
        service="unknown"
    return service


def check_ports(ip, start_port, end_port):
    open_ports = []
    service_name=[]
    for port in range(start_port, end_port + 1):
        if is_port_open(ip, port):
            service_name.append(get_service_name(port))
            open_ports.append(port)
    return open_ports ,service_name

def measure_latency(ip, port, num_requests):
    latencies = []
    for _ in range(num_requests):
        start_time = timeit.default_timer()
        if is_port_open(ip, port):
            end_time = timeit.default_timer()
            latency = end_time - start_time
            latencies.append(latency)
    if latencies:
        average_latency = sum(latencies) / len(latencies)
        return average_latency
    else:
        return None

def get_post(req):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect(('localhost', 8080))
        s.sendall(req.encode())
        response = s.recv(1024).decode()
        s.close()
        return response
        





hostIP = input("enter IP: ")
startport = int(input("enter start port: "))
endport = int(input("enter end port: "))
while True:
  
  print("chose an option: ")
  print("1) Checking whether the host is online or offline")
  print("2) Report of ports that are open")
  print("3) Ports response delay time")
  print("4) get")
  print("5) post")
  print("6) exit")
  answer=int(input())
  if answer==1:
    p,s=check_ports(hostIP,startport,endport)

    if len(p)>0:
      print(f'host {hostIP} is online.')
    elif len(p)==0:
      print(f'host {hostIP} is ofline.')
      
  elif answer==2:
    p,s=check_ports(hostIP,startport,endport)
    i=0
    if len(p)==0:
       print("no socket is open")
    else:   
      while i!=len(p):
        print(f"Port: {p[i]} , service: {s[i]}")
        i=i+1

  elif answer==3:
       porttime= int(input("enter port: ")) 
       num_requests= int(input("enter number of request: "))
       avg_latency = measure_latency(hostIP, porttime, num_requests)
       if avg_latency is not None:
         print(f"latency of port {porttime} is {avg_latency:.6f} second")
       else:
         print(f"port {porttime} is close.")

  elif answer==4:
     req=input("enter id in (GET user_id): ")
     t=get_post(req)
     print(t)
   
  elif answer==5:
      req= input("enter id in (POST user_name user age): ")
      t=get_post(req)
      print(t)
      
  elif answer==6:
    break





