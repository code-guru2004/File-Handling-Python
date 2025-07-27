from pathlib import Path
import os

def readExistingFile():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"==> {i+1} : 📁 {items}")

def createFile():
    print("-->🔴 CREATE FILE ")
    try:
        print("-->Your previous files 📂")
        readExistingFile()
        name = input("Enter your file name: ")
        path = Path(name)
        if not path.exists() and path.is_file():
            with open(path,'w') as fs:
                data = input(f"What you want to write in this file (path: {path}): ")
                fs.write(data)
            print("File created successfully 😊")
        else:
            print("❌ File already exists")
    except Exception as err:
        print("❌ Failed to create file")


def readFile():
    print("-->🔴 READ FILE ")
    try:
        readExistingFile()
        fileToRead = input("Enter the file name to be read : ")
        path = Path(fileToRead)
        if path.exists() and path.is_file():
            with open(path,'r') as fs:
                data = fs.read()
                print(" -- File content -- ")
                print(data)
        else:
            print("❌ File does not exists")
    except Exception as err:
        print("❌ Failed to read file")

def updateFile():
    print("-->🔴 UPDATE FILE ")
    try:
        readExistingFile()
        fileToRead = input("Enter the file name to be update : ")
        path = Path(fileToRead)
        if path.exists() and path.is_file():
            print("-- Options --")
            print("1. Update the file name")
            print("2. Overwrite the existing file")
            print("3. Change with existing content")
            choice = int(input("Enter any of the above options : "))
            if choice == 1:
                newName = input("--> Enter the file name: ")
                newPath = Path(newName)
                path.rename(newPath)
                print("✅ Rename successfully")
            elif choice ==2:
                with open(path,'w') as fs:
                    data = input("File content you want to overwrite : ")
                    fs.write(data)
                    print("✅ Overwrite successfully")
            elif choice == 3:
                with open(path,'a') as fs:
                    data = input("File content you want to overwrite : ")
                    fs.write(f' {data}')
                    print("✅ Content Update successfully")
            else:
                print("‼️ Invalid option")
        else:
            print("❌ Failed to read file")
    except Exception as err:
        print("❌ Failed to update file")

def deleteFile():
    print("-->🔴 DELETE FILE ")
    try:
        readExistingFile()
        file = input("Enter the file name : ")
        path = Path(file)
        if path.exists() and path.is_file() :
            os.remove(path)
            print("✅ Deleted successfully")
    except Exception as err:
        print("❌ Failed to update file")

print("Press-1️⃣  for CREATE a file")
print("Press-2️⃣  for READ a file")
print("Press-3️⃣  for UPDATE a file")
print("Press-4️⃣  for DELETE a file")

# readExistingFile()
press = int(input("Enter what you want : "))
if press == 1:
    createFile()
elif press == 2:
    readFile()
elif press == 3:
    updateFile()
elif press == 4:
    deleteFile()
else:
    print("❌ You choose wrong option")
