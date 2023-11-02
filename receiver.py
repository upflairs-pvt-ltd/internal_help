import socket,time
# creating udp socket object
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# putting target addreess
my_ip="192.168.1.30"
my_port=1199
# sending address
my_address=(my_ip,my_port)
# starting address 
s.bind(my_address)

# lets recv data from users / senders
while 1 : 
    data=s.recvfrom(100)
    # decoding it 
    actual_msg=data[0]
    sender_details=data[1]
    # printing message and address both 
    new_msg=actual_msg.decode('ascii')
    print("_____________________")
    #print("plz wait getting info of sender ")
    time.sleep(1)
    print(new_msg,"  FROM   --->> ",sender_details)
    # saving data into a file 
    with open('sender_details/'+sender_details[0],'a+') as f:
        f.write(new_msg+'\n')


