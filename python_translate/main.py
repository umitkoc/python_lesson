from time import sleep
from os import listdir, remove
from googletrans import Translator

#############################################################
print("""
                          @MTKC
    -y:Yes
    -n:NO
    Please confirm by pressing Enter after answering
Note: Pressing H or any other keys closes the process!
""")


############################################################
def approve(i):
    with open("demo.txt", "r", encoding="utf-8") as file:
        word = file.read()
        file.close()
        with open(i, "w", encoding="utf-8") as data:
            data.write(word)
            data.close()
            return True


def Translate(list):
    for i in list:
        with open(i, "r", encoding="utf-8") as file:
            with open("demo.txt", "w", encoding="utf-8") as _data:
                s = 0
                _word = ""
                print("your files are being translated ....")
                m = 0
                translator = Translator()
                step = 0
                while True:
                    word = file.readline()
                    if word != "":
                        _word += word
                    else:
                        break
                    if s > 5:
                        print(m)
                        m += 1
                        data = translator.translate(_word, src="en", dest="tr").text
                        _data.write(data)
                        _word = ""
                        s = 0
                        if m > 200:
                            step += 1
                            translator = Translator()
                            print(f"{10} holding seconds ---->{step}")
                            m = 0
                            sleep(10)
                    s += 1
                data = translator.translate(_word, src="en", dest="tr").text
                _data.write(data)
            _data.close()
        file.close()
        approve = approve(i)
        if approve:
            print(i + " :file ok!")


#######################################
def Files():
    files = listdir(".")
    list = []
    print("Reviewing files...")
    sleep(2)
    for file in files:
        if file.endswith(".srt") or file.endswith(".txt"):
            list.append(file)
            print(file)
    sleep(2)
    answer = input("Should these files be translated into TR? [y/n]")
    if answer.lower() == 'y':
        Translate(list)
    else:
        print("Logout...")
        sleep(2)
        exit(0)


###############################################
def Answer():
    answer = input("start examining his/her files?[y/n]")
    print(answer)
    if answer.lower() == 'y':
        Files()
    else:
        print("Logout...")
        sleep(2)
        exit(0)


def Run():
    Answer()
    sleep(3)
    files = listdir(".")
    for file in files:
        if file == "demo.txt":
            remove(file)
            print("Your transaction is done ☻")
            sleep(3)
            break


Run()
