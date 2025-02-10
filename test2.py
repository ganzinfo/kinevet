from pynput.keyboard import Key, Listener

# def on_press(key):
#     print('{0} pressed'.format(
#         key))



def keyListener(charsDict):

    with Listener(on_release=on_release) as listener:
        listener.join()

def on_release(key):
    try:
        if key.vk in charsDict:
            print(charsDict[key.vk])
        else:
            print("none")
        # if key == Key.esc:
            # Stop listener
    except:
        pass
    # return False

charsDict = {48:'0',49:'1',50:'2',51:'3',52:'4',96:'0',97:'1',98:'2',99:'3',100:'4',81:'q'}
keyListener(charsDict)
# def on_release(key):
#     print('{0} release'.format(
#         key))
#     if key == Key.esc:
#         # Stop listener
#         return False

# Collect events until released



# with Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# import sys
#
# import keyboard
#
# # while True:
# #     keyboard.add_hotkey('alt+p', start, suppress=True, trigger_on_release=True)
# #     while not exit:
# #         # put something here, you can't have an empty loop
# #     keyboard.remove_hotkey('alt+p')
# def processKey():
#     if keyboard.is_pressed('alt+p'):
#         print("alt p")
#     elif keyboard.is_pressed('alt+p'):
#         print("alt o")
#
# # keyboard.add_hotkey('ctrl + shift + o', print, args=('Hotkey', 'Detected'))
# keyboard.add_hotkey('alt+p', processKey(), suppress=True, trigger_on_release=True)
# keyboard.add_hotkey('alt+o', processKey(), suppress=True, trigger_on_release=True)
#
# keyboard.wait('esc')
#
#     # keyboard.unhook_all_hotkeys()
#
#     # key_event = keyboard.read_event()
#     #
#     # print(key_event,key_event,key_event)
#     # print(var1, var2, var3)
#
# # def keyboardInput(keys: tuple) -> str:
# # 	""" Wait for keyboard input (1 stroke). Returns either one of arguments, or with 'q' quits the game.
# # 	:param keys: tuple, the keys to check
# # 	:return: string, key found
# # 	q: quit game
# # 	"""
# # 	returnKey = ''
# # 	keysIndex = 0
# # 	key_event = keyboard.read_event()
# # 	keyboard.
# # 	while True:
# # 		keyCheck = keys[keysIndex]
# #
# # 		if key_event.event_type == keyboard.KEY_UP and key_event.name == 'q':
# # 			answer = input ("\bDo you really want to quit game? (y/n and enter)")
# # 			if answer == "y":
# # 				print("\bQuit game... Bye.")
# # 				sys.exit()
# # 		else:
# # 			for key in keys:
# # 				if key_event.event_type == keyboard.KEY_UP and key_event.name == key:
# # 					key_event = None
# # 					returnKey = key_event.name
# # 		break
# # 	return returnKey
# #
# # keyinput = keyboardInput(('a','s','d','f'))
# #
# # print(keyinput)
