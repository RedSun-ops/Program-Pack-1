print("Program pack 1.0")
A = input("Select a program : ")
if A == "2020TOP":
  print("   ------------------")
  print("   | --------  ---- |")
  print("   | | 2020 |  ---- |")
  print("   | --------  ---- |")
  print("   | -Python--IS--- |")
  print("   | --TOP-----1--- |")
  print("   | -------------- |")
  print("   | -------------- |")
  print("   |                |")
  print("   ------------------")
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
  print("Thanks to tiobe for info!")
  input()
elif A == "Benchmark":
  print("    -----------    ")
  print("    |         |    ")
  print("    |Benchmark|    ")
  print("    |         |    ")
  print("    /         \    ")
  print("   /           \   ")
  print("   -------------    ")
  Year = input('enter your computer year! : ')
  Bits = input("how much bits you have : ")
  Hz = input("Processor Performance (hz) : ")
  output = float(Hz)*int(Year)*float(Bits)/1000/2000/50
  print(output)
  input()
elif A == "Resistor":
  print(" \\              / ")
  print("  \\            / ")
  print("   -------------")
  print("   |           |")
  print("   |  ( ||| )  |")
  print("   |  |     |  |")
  print("   -------------")
  print("Hello!")
  print("1,2,3th : BL(Black) , BR(Brown) , R(Red) , O(Orange) , Y(Yellow) , G(Green) , B(Blue) , V(Violet) , Grey , W(White)")
  print("Multiplier : BL(Black) , BR(Brown) , R(Red) , O(Orange) , G(Green) , B(Blue) , V(Violet) , Grey , W(White) , GO(Gold) , S(Silver)")
  A = input("1th : ")
  if A == "BL":
   One = 0
  if A == "BR":
   One = 1
  if A == "R":
   One = 2
  if A == "O":
   One = 3
  if A == "Y":
   One = 4
  if A == "G":
   One = 5
  if A == "B":
   One = 6
  if A == "V":
   One = 7
  if A == "Grey":
   One = 8
  if A == "W":
   One = 9
  B = input("2th : ")
  if B == "BL":
   Two = 0
  if B == "BR":
   Two = 1
  if B == "R":
   Two = 2
  if B == "O":
   Two = 3
  if B == "Y":
   Two = 4
  if B == "G":
   Two = 5
  if B == "B":
   Two = 6
  if B == "V":
   Two = 7
  if B == "Grey":
   Two = 8
  if B == "W":
   Two = 9
  M = input("3th : ")
  if M == "BL":
   Multiplier = 1
  if M == "BR":
   Multiplier = 10
  if M == "R":
   Multiplier = 100
  if M == "O":
   Multiplier = 1000
  if M == "Y":
   Multiplier = 10000
  if M == "G":
   Multiplier = 100000
  if M == "B":
   Multiplier = 1000000
  if M == "V":
   Multiplier = 10000000
  if M == "Grey":
   Multiplier = 100000000
  if M == "W":
   Multiplier = 1000000000
  if M == "GO":
   Multiplier = 0.1
  if M == "S":
   Multiplier = 0.01
  R1 = str(One) + str(Two)
  Ohm = int(R1) * int(Multiplier)
  KOhm = int(Ohm) / 1000
  MOhm = int(KOhm) / 1000
  print(str(Ohm) + " Ohm")
  print(str(KOhm) + " KOhm")
  print(str(MOhm) + " MOhm")
  input()
elif A == "VirtualMemoryTextEditor":
  print("---------")
  print("| □  □ |")
  print("---------")
  print(" ■■■■ ")
  string = input("Text : ")
  length = len(string)
  if length > 128:
    print("Error : Not enough memory")
    input()
  if length <= 128:
    freememory = 128 - length
    print(str(freememory) + " Bytes Free")
    print("File      Size")
    print("Text.txt  " + str(length) + "B")
    command = input("Print Data From Text.txt (y/n)?")
    if command == "y":
      print(str(string))
      input()
    if command == "n":
      print("Goodbye!")
      input()
  
