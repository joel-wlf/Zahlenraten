import random

gesint = random.randint(1, 100)

//functions

def leicht():
  aktiv = 0
  while aktiv < 7:
    inpint = input("Welche Zahl könnte gesucht sein?")
    if int(inpint) < gesint:
      print("Die gesuchte Zahl ist größer.")
      aktiv = aktiv + 1
    elif int(inpint) > gesint:
      print("Die gesuchte Zahl ist kleiner.")
      aktiv = aktiv + 1
    elif int(inpint) == gesint:
      print("Super! Du hast gewonnen!")
      aktiv = 0
      break

def schwer():
  aktiv = 0
  while aktiv < 6:
    inpint = input("Welche Zahl könnte gesucht sein?")
    if int(inpint) < gesint:
      print("Die gesuchte Zahl ist größer.")
      aktiv = aktiv + 1
    elif int(inpint) > gesint:
      print("Die gesuchte Zahl ist kleiner.")
      aktiv = aktiv + 1
    elif int(inpint) == gesint:
      print("Super! Du hast gewonnen!")
      aktiv = 0
      break
gew = "nein"
print("Hallo, ich habe mir eine Zahl ausgedacht und du musst sie teilweise erraten.\nMöchtest du den leichten Modus, oder den schweren? ")
modus = input()
if modus == "leicht":
  leicht()
else:
  schwer()