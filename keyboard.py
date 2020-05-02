import keyboard

while True:
    if keyboard.read_key() == "q":
        print("break")
        break
    elif keyboard.is_pressed('a'):
        print("winner")
    else:
        print("Loser")
        
