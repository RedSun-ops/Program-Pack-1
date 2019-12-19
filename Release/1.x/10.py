import platform
import datetime
import sys
import time 
uname = platform.uname()
now = datetime.datetime.now()
now2 = str(now)
OS = str(sys.platform)
d = str(now2[0] + now2[1] + now2[2] + now2[3])
if OS == "win32":
  print("You have Windows or ReactOS! (90% of users)")
if OS == "cygwin":
  print("You Have Windows/Cygwin")
if OS == "darwin":
  print("You Have Mac OS (10% of users)")
if OS == "os2":
  print("You have OS/2 (Who generally use this operating system?)")
if OS == "linux":
  print("You have linux or android (via dcoder or qpython)")
else:
  print("You are using a different operating system!")
def again():
  uname = platform.uname()
  now = datetime.datetime.now()
  now2 = str(now)
  d = str(now2[0] + now2[1] + now2[2] + now2[3])
  OS = str(sys.platform)
  if OS == "win32":
    print("You have Windows or ReactOS! (90% of users)")
  if OS == "cygwin":
    print("You Have Windows/Cygwin")
  if OS == "darwin":
    print("You Have Mac OS (10% of users)")
  if OS == "os2":
    print("You have OS/2 (Who generally use this operating system?)")
  if OS == "linux":
    print("You have linux or android (via dcoder or qpython)")
  else:
    print("You are using a different operating system!")
  
  
  print("1.0")
  print("Release! Yay!!!!!!!")
  print("–----–––")
  print("| " + str(d) + " |")
  print("|••••••|")
  print("|••••••|")
  print("--------")
  print()
  print()
  print("                               ")
  print("   -------      -----------    ")
  print("   |Py is|      |         |    ")
  print("   |Top 1|      |Benchmark|    ")
  print("   |-----|      |         |    ")
  print("   -------      /_________\\   ")
  print("-------------------------------")
  print("|         -------------       |")
  print("|         |     •     |       |")
  print("|         -------------       |")
  print("|                             |")
  print("-------------------------------")
  A = input("select program (2020TOP, Benchmark, drawer) : ")
  if A == "2020TOP":
    # Top 3 Programming languages on Nov 2020 (tiobe.com)
    Java = 16.24
    C = 16.03
    Python = 9.84
    Java2020 = 6
    C2020 = 1.64*12
    Python2020 = 2.16*12
    print("Java (Nov 2020) : " + str(Java - Java2020) + "%")
    print("C (Nov 2020) : " + str(C + C2020) + "%")
    print("Python (Nov 2020) : " + str(Python + Python2020) + "%")
    print("Learn Python or C!!!!")
    time.sleep(3)
    again()
  if A == "Benchmark":
    Year = input('enter your computer year! : ')
    Bits = input("how much bits you have : ")
    Hz = input("Processor Performance (hz) : ")
    i = 0
    while i <= int(Year):
      print (i)
      i += 15
    output = float(Hz)*int(Year)*float(Bits)/1000/2000/50
    print(output)
    time.sleep(3)
    again()
  if A == "drawer":
    print("--------------------------------")
    print("|    ---------      ---------- |")
    print("|    | 12345 |      |  About | |")
    print("|    | ••••• |      |        | |")
    print("|    | ••••• |      |        | |")
    print("|    ---------      |        | |")
    print("|                   ---------- |")
    print("--------------------------------")
    print("                ◯               ")
    DrawerA = input("Select program (Calculator) : ")
    if DrawerA == "Calculator":
      B = input("Enter First Number : ")
      C = input("[+, -, *, /, ^] : ")
      D = input("Enter Second Number : ")
      if C == "+":
        E = int(B) + int(D)
        print(E)
      if C == "-":
        E = int(B) - int(D)
        print(E)
      if C == "*":
        E = int(B) * int(D)
        print(E)
      if C == "/":
        E = int(B) / int(D)
        print(E)
      if C == "^":
        E = int(B) ** int(D)
        print(E)
      time.sleep(5)
      again()
    if DrawerA == "About":
      print("About : ")
      print()
      print("Version : 1.0")
      print("Codename : 119122019")
      print("OS : " + str(OS) + " " + uname.release)
      print("archeticture : " + uname.processor)
      print("Stable")
      time.sleep(3)
      again()
print("1.0")
print("Release! Yay!!!!!!!")
print("–----–––")
print("| " + str(d) + " |")
print("|••••••|")
print("|••••••|")
print("--------")
print()
print()
print()
print("   -------      -----------    ")
print("   |Py is|      |         |    ")
print("   |Top 1|      |Benchmark|    ")
print("   |-----|      |         |    ")
print("   -------      /_________\\   ")
print("-------------------------------")
print("|         -------------       |")
print("|         |     •     |       |")
print("|         -------------       |")
print("|                             |")
print("-------------------------------")
A = input("select program (2020TOP, Benchmark, drawer) : ")
if A == "2020TOP":
  # Top 3 Programming languages on Nov 2020 (tiobe.com)
  Java = 16.24
  C = 16.03
  Python = 9.84
  Java2020 = 6
  C2020 = 1.64*12
  Python2020 = 2.16*12
  print("Java (Nov 2020) : " + str(Java - Java2020) + "%")
  print("C (Nov 2020) : " + str(C + C2020) + "%")
  print("Python (Nov 2020) : " + str(Python + Python2020) + "%")
  print("Learn Python or C!!!!")
  time.sleep(3)
  again()
if A == "Benchmark":
  Year = input('enter your computer year! : ')
  Bits = input("how much bits you have : ")
  Hz = input("Processor Performance (hz) : ")
  i = 0
  while i <= int(Year):
    print (i)
    i += 15
  output = float(Hz)*int(Year)*float(Bits)/1000/2000/50
  print(output)
  time.sleep(3)
  again()
if A == "drawer":
  print("--------------------------------")
  print("|    ---------      ---------- |")
  print("|    | 12345 |      |  About | |")
  print("|    | ••••• |      |        | |")
  print("|    | ••••• |      |        | |")
  print("|    ---------      |        | |")
  print("|                   ---------- |")
  print("--------------------------------")
  print("                ◯               ")
  DrawerA = input("Select program (Calculator, About) : ")
  if DrawerA == "Calculator":
    B = input("Enter First Number : ")
    C = input("[+, -, *, /, ^] : ")
    D = input("Enter Second Number : ")
    if C == "+":
      E = int(B) + int(D)
      print(E)
    if C == "-":
      E = int(B) - int(D)
      print(E)
    if C == "*":
      E = int(B) * int(D)
      print(E)
    if C == "/":
      E = int(B) / int(D)
      print(E)
    if C == "^":
      E = int(B) ** int(D)
      print(E)
    time.sleep(5)
    again()
  if DrawerA == "About":
    print("About : ")
    print()
    print("Version : 1.0")
    print("Codename : 119122019")
    print("OS : " + str(OS) + " " + uname.release)
    print("archeticture : " + uname.processor)
    print("Stable")
    time.sleep(3)
    again()
