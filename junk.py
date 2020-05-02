from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

#def on_release(key):
#    print('{0} release'.format(key))
#    if key == Key.esc:
#        # Stop listener
#        return False

# Collect events until released
with Listener(
        on_press=on_press) as listener:
        #on_release=on_release) as listener:
    listener.join()