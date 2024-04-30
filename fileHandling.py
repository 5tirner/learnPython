import os
print("Read From A File:\n")
try:
    file = open("file.txt", "r")
    try:
        #save = file.read() read all
       # save1 = file.read(5) read 5 bytes
       print(file.readline()) # read one line
    except Exception as err:
        print(err)
    else:
        print("File Readed Succesfully")
except Exception as err:
    print(f"{err}")
else:
    print("File Opened Succesfully")
    file.close()
print("\nWrite Into A File:\n")
try:
    file = open("file.txt", "w")
    file1 = open("file.txt", "a")
    file2 = open("file.txt", "r")
    try:
        file.write("->This Line Added By Code")
        file1.write("\n-> This Line Append From Another Code")
        print(file2.read())
    except Exception as err:
        print(err)
    else:
        print("Written Succesfully")
except Exception as err:
    print(f"{err}")
else:
    print("File Opened Succesfully")
finally:
    file.close()
    file1.close()
    file2.close()
    if os.path.exists("file.txt"):
        os.remove("file.txt")
    file = open("file.txt1", "x")
    file.close()
