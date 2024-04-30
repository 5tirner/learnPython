import math
try:
    file = open("file.txt")
    try:
        file.write("Hello")
    except:
        print("Can't Write On `file.txt`")
    else:
        print("Data Saved At `file.txt`")
    finally:
        file.close()
        print("Process Of Written On `file.txt` Done.")
except:
    print("Failed To Open `file.txt`")
else:
    print("`file.txt` Opened Succesfully")
finally:
    print("Process Is Done.")

def isIntData(d):
    if not type(d) is int:
        raise Exception("Not An Integer")
    else:
        print(math.sqrt(d))
try:
    isIntData("ho")
except:
    print("Not An INT")