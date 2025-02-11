from pynput.keyboard import Key, Listener

def keyListener(chars):
    global charsDict
    charsDict = chars
    with Listener(on_release=on_release) as listener:
        listener.join()

def on_release(key):
    try:
        if key.vk in charsDict:
            # print(charsDict[key.vk])
            return charsDict[key.vk]
        else:
            pass
    except:
        pass


global charsDict
# keyListener(charsDict)
