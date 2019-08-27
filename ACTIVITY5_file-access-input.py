
file=open("hardware.txt","a")

while True:
    newItem = input("Enter new device (or type exit to quit): ")
    if newItem == 'exit':
        print('All done!')
        file.close()
        break
    file.write("\n" + newItem)

file2=open("hardware.txt","r")
for item in file2:
    print(item.strip())
file2.close()

