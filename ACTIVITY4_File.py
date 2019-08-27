devices=[]
file=open("hardware.txt","r")
for item in file:
    print(item.strip())
    devices.append(item.strip())
file.close()
for device in devices:
    print(device)
