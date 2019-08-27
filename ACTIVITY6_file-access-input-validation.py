while True:
    file=open("hardware.txt","a")
    devices=[]
    file2=open("hardware.txt","r")
    for item in file2:
        devices.append(item.strip())

    newItem = input("Enter new device (or type exit to quit): ")
    if newItem == 'exit':
        print('All done!')
        file.close()
        break
    found = False
    for device in devices:
        if device == newItem:
            found=True
            print("Item existing! Cannot be added.")
    if found == False:
        file.write(newItem +"\n")
    file.close()
    file2.close()

file2=open("hardware.txt","r")
for item in file2:
    print(item.strip())
file2.close
