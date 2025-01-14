import sys

import keyboard

while True:
    key_event = keyboard.read_event()

    print(key_event,key_event,key_event)
    # print(var1, var2, var3)

# def keyboardInput(keys: tuple) -> str:
# 	""" Wait for keyboard input (1 stroke). Returns either one of arguments, or with 'q' quits the game.
# 	:param keys: tuple, the keys to check
# 	:return: string, key found
# 	q: quit game
# 	"""
# 	returnKey = ''
# 	keysIndex = 0
# 	key_event = keyboard.read_event()
# 	keyboard.
# 	while True:
# 		keyCheck = keys[keysIndex]
#
# 		if key_event.event_type == keyboard.KEY_UP and key_event.name == 'q':
# 			answer = input ("\bDo you really want to quit game? (y/n and enter)")
# 			if answer == "y":
# 				print("\bQuit game... Bye.")
# 				sys.exit()
# 		else:
# 			for key in keys:
# 				if key_event.event_type == keyboard.KEY_UP and key_event.name == key:
# 					key_event = None
# 					returnKey = key_event.name
# 		break
# 	return returnKey
#
# keyinput = keyboardInput(('a','s','d','f'))
#
# print(keyinput)
