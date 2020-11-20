import paramiko

def pilih():
	print("#------------- Pilih Node -------------#")
	print("1. Node 1 [IP: " + node1_ip + "]")
	print("2. Node 2 [IP: " + node2_ip + "]")
	print()
	node = int(input("Pilih Node: "))
	return node

def connect(ip, name, pw):	
	pr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	pr.connect(hostname=ip, username=name, password=pw)

pr = paramiko.SSHClient()

node1_ip = "192.168.1.13"
node1_name = "hooman"
node1_pw = "justlearn911!"

node2_ip = "192.168.1.10"
node2_name = "hooman"
node2_pw = "justlearn911!"

node = pilih()
if(node == 1):
	connect(node1_ip, node1_name, node1_pw)
elif(node == 2):
	connect(node2_ip, node2_name, node2_pw)
else:
	print("Masukkan Sesuai Pilihan")
	exit()

while(True):
    stdin,stdout,stderr = pr.exec_command("python3 monitoring.py")
    output = stdout.readlines()
    for i in output:
        print(i, end="")


