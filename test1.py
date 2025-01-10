import keyboard
#import sys
while True:
    event = keyboard.read_event()
    print(event)
    if event.event_type == keyboard.KEY_UP and event.name == 'space':
        print('space was pressed')

    if event.event_type == keyboard.KEY_UP and event.name == 'q':
        print('q was pressed')
    event = None
    print("next")

    # keyboard.on_press()
    # print('Enter is pressed')
    #
    # keyboard.wait('q')
    # print('Quitting the program')
    #
    # keyboard.wait('s')
    # print('Skiping the things')

    # key_event = keyboard.read_event(suppress=True)
    # key_event = keyboard.read_key()
    # keyboard.KeyboardEvent
    # print(key_event)

    # if key_event.event_type == keyboard.KEY_UP:
    # if keyboard.is_pressed("q"):
    #     keyboard.release("q")
    #     print("q")
    # if keyboard.is_pressed("space"):
    #     keyboard.release("space")
    #     print("space")

    # if key_event.name == 'q':
    # #     print(key_event.name)
    #      print("\bQuit game... Bye.")
    # #     #sys.exit()
    # #     #time.sleep(1)
    # if key_event.name == 'space':
    # #     print(key_event.name)
    #     print(f"Hier comes dice roll...")
    # #     #time.sleep(1)
    #
    # print("next")


