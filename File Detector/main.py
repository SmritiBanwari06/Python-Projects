import os

def isSmriti(filename):
    with open(filename,"r") as f:
        fileContent = f.read()

    if "smriti" in fileContent.lower():
        return True
    else:
        return False


if __name__=='__main__':
    dir_contents = os.listdir()
    # print(dir_contents)

    nSmriti = 0
    for items in dir_contents:
        if items.endswith('txt'):
            print(f"Detecting smriti in {items}")

            flag = isSmriti(items)
            if(flag):
                print(f"Smriti found in {items}")
                nSmriti+=1
            else:
                print(f"smriti not found in {items}")

    print("*****Smriti Detector Summary*****")
    print(f"{nSmriti} files found with smriti hidden into them. ")