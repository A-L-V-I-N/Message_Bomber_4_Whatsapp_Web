from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

print("*************************************************************")
print("                   MSG Bomber 4 whatsapp_web                 ")
print("                          Version 1.0                        ")
print("                         Made By Alvin                       ")
print("         'Enjoy spamming others and getting blocked!'        ")
print("                                                             ")     
print("*************************************************************")
limit = int(input("[+] Enter the limit(number) >> "))  
message = input("[+] Enter the message >> ")
print("[+] Bombing activated, take the cursor into whatsapp_web :)")
time.sleep(8)

while limit > 0:
	for letter in message:
		keyboard.press(letter)
		keyboard.release(letter)
	keyboard.press(Key.enter)	
	keyboard.release(Key.enter)
	limit = limit - 1
# Uncomment the line below to give a slight delay in sending messages(in case any crash occours)
#	time.sleep(0.5) 

