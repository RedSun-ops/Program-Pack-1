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
  
  
  print("2.0")
  print("You can give me programs : angel071455@protonmail.com")
  print("–----–––")
  print("| " + str(d) + " |")
  print("|••••••|")
  print("|••••••|")
  print("--------")
  print()
  print()
  print()
  print("   -------      -----------        -------------")
  print("   |Py is|      |         |        |           |")
  print("   |Top 1|      |Benchmark|        |           |")
  print("   |-----|      |         |        |           |")
  print("   -------      /_________\\        |           |")
  print("-------------------------------    |          •|")
  print("|         -------------       |    |           |")
  print("|         |     •     |       |    |           |")
  print("|         -------------       |    |           |")
  print("|                             |    |           |")
  print("-------------------------------    -------------")
  A = input("select program (2020TOP, Benchmark, drawer, Door) : ")
  if A == "2020TOP":
    # Top 3 Programming languages on Nov 2020 (tiobe.com)
    Java = 17.25
    C = 16.08
    Python = 10.30
    CPP = 6.19
    CS = 4.8
    Java2021 = 1.32*12
    C2021 = 1.80*12
    Python2021 = 1.92*12
    CPP2021 = 1.36*12
    CS2021 = 1.35*12
    print("Java (Jan 2021) : " + str(Java + Java2021) + "%")
    print("C (Jan 2021) : " + str(C + C2021) + "%")
    print("Python (Jan 2021) : " + str(Python + Python2021) + "%")
    print("C++ (Jan 2021) : " + str(CPP - CPP2021) + "%")
    print("C# (Jan 2021) : " + str(CS + CS2021) + "%")
    print("Learn C or Python!!!!")
    time.sleep(3)
    again()
  if A == "Benchmark":
    Year = input('enter your computer year! : ')
    Bits = input("how much bits you have : ")
    Hz = input("Processor Performance (hz) : ")
    Core = input("Processor Cores : ")
    Drive = input("hard drive or ssd storage (gb) : ")
    Ram = input("RAM size (mb) : ")
    i = 0
    while i <= int(Year):
      print (i)
      i += 15
    output = float(Hz)*int(Year)*float(Bits)*int(Core)*int(Drive)*int(Ram)/1000/2000/50/100000
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
      print("Version : 2.0")
      print("Codename : 2112020")
      time.sleep(3) 
      again()
  if A == "Door":
    print("--------       --------")
    print("|      |       |      |")
    print("|      |       |      |")
    print("|   [ ]|       |   [ ]|")
    print("--------       --------")
    B = input("Select home (1(Your), 2) : ")
    if B == "1":
      again()
    if B == "2":
      print("btp://hello.world")
      print("Hello World")
      NET = input("Site : ")
      if NET == "btp://stat.s":
        print(NET)
        print("-----------------")
        print("Connected : Yes")
        print("User ID : 0000:0001")
        print("Site : " + NET)
        print("OS : " + str(OS) + " " + uname.release)
        print("archeticture : " + uname.processor)
        print("Made by geek for geeks")
        time.sleep(7)
        again()
print("2.0")
print("You can give me programs : angel071455@gmail.com")
print("–----–––")
print("| " + str(d) + " |")
print("|••••••|")
print("|••••••|")
print("--------")
print()
print()
print()
print("   -------      -----------        -------------")
print("   |Py is|      |         |        |           |")
print("   |Top 1|      |Benchmark|        |           |")
print("   |-----|      |         |        |           |")
print("   -------      /_________\\        |           |")
print("-------------------------------    |          •|")
print("|         -------------       |    |           |")
print("|         |     •     |       |    |           |")
print("|         -------------       |    |           |")
print("|                             |    |           |")
print("-------------------------------    -------------")
                                 
                                 
A = input("select program (2020TOP, Benchmark, drawer, Door) : ")
if A == "2020TOP":
  # Top 3 Programming languages on Nov 2020 (tiobe.com)
  Java = 17.25
  C = 16.08
  Python = 10.30
  CPP = 6.19
  CS = 4.8
  Java2021 = 1.32*12
  C2021 = 1.80*12
  Python2021 = 1.92*12
  CPP2021 = 1.36*12
  CS2021 = 1.35*12
  print("Java (Jan 2021) : " + str(Java + Java2021) + "%")
  print("C (Jan 2021) : " + str(C + C2021) + "%")
  print("Python (Jan 2021) : " + str(Python + Python2021) + "%")
  print("C++ (Jan 2021) : " + str(CPP - CPP2021) + "%")
  print("C# (Jan 2021) : " + str(CS + CS2021) + "%")
  print("Learn C or Python!!!!")
  time.sleep(3)
  again()
if A == "Benchmark":
  Year = input('enter your computer year! : ')
  Bits = input("how much bits you have : ")
  Hz = input("Processor Performance (hz) : ")
  Core = input("Processor Cores : ")
  Drive = input("hard drive or ssd storage (gb) : ")
  Ram = input("RAM size (mb) : ")
  i = 0
  while i <= int(Year):
    print (i)
    i += 15
  output = float(Hz)*int(Year)*float(Bits)*int(Core)*int(Drive)*int(Ram)/1000/2000/50/100000
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
    print("Version : 2.0")
    print("Codename : 2112019")
    print("Unstable")
    time.sleep(3)
    again()
if A == "Door":
  print("--------       --------")
  print("|      |       |      |")
  print("|      |       |      |")
  print("|   [ ]|       |   [ ]|")
  print("--------       --------")
  B = input("Select home (1(Your), 2) : ")
  if B == "1":
    again()
  if B == "2":
    print("btp://hello.world")
    print("Hello World")
    NET = input("Site : ")
    if NET == "btp://stat.s":
      print(NET)
      print("-----------------")
      print("Connected : Yes")
      print("User ID : 0000:0001")
      print("Site : " + NET)
      print("OS : " + str(OS) + " " + uname.release)
      print("archeticture : " + uname.processor)
      print("Made by geek for geeks")
      time.sleep(7)
      again()