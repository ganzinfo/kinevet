from pynput.keyboard import Key, Listener

def on_press(key):
    pass
    # print('{0} pressed'.format(
    #     key))


def on_release(key):
#hasattr(key,'char')
    if key.char == 'q':
        print('q')
    elif key.char == 'c':
        print('c')

    print('{0} release'.format(
        key))

    if key == Key.esc:
        # Stop listener
        return False

def listen(keys):# Collect events until released
    keys = keys
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


args=('1','2','3')

listen(args)