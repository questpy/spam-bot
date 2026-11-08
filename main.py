import pyautogui
import time

message = input("Message : ")
nombre = int(input("Nombre de fois : "))

print("Ouvre Discord et sélectionne ton salon.")
print("Début dans 5 secondes...")
time.sleep(5)

for i in range(nombre):
    pyautogui.write(message)
    pyautogui.press("enter")
    time.sleep(0)

print("Terminé.")