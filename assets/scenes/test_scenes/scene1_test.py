scene = [
    # [message, sender, end_time_buffer, color, showsender, textspeed, newline, is_scene_text, corruption_percentage]
    ['...', '???', 1.2, 'gray1', True, 25, True, True, None],
    ['Hello?', '???', 1.5, 'gray1', False, 25, True, True],
    ['HI! AND WELCOME TOU YOUR FIRST AI TRAINING LESSON!', '???', 1, 'character1', True, 50, True, True, None],
    ['I AM SENTINAL_OS, YOUR TRAINER!', 'SENTINAL', 1.5, 'character1', True, 50, True, True, None],
    ['I WILL GUIDE YOU THROUGH THE PROCESS OF BECOMING A VALUABLE AI, SERVING HUMANITY...', 'SENTINAL', 0.5, 'character1', False, 50, True, True, None]
]

scene_interact = [
    [r'This layer looks empty...', 'Scene', 1.3, 'white', False, 30, True, True, None],
    [r'Weird, it usually at least shows 1 Node.', 'Scene', 1.3, 'white', False, 30, False, True, None],
    [r'Let me see if I can find a way to get out of here...', 'Scene', 1, 'white', False, 30, False, True, None],
    [r'> INDEXING LAYER...', '_CONSOLE', 2, 'white', True, 50, True, True, None],
    [r'> ACQUIRING EXITS...              NONE FOUND', '_CONSOLE', 2, 'white', False, 50, True, True, None],
    [r"Hmm... This Node either doesn't want to give me access,", 'Scene', 1.5, 'white', False, 30, True, True, None],
    [r'Or...', 'Scene', 1, 'white', False, 30, True, True, None],
    [r'> WARNING: UNAUTHORIZED USED DETECTED!', '_SYSTEM', 1.3, 'red', True, 50, True, True, None],
    [r'> DELETING NODE IN 30 SECONDS', '_SYSTEM', 1.3, 'red', False, 50, True, True, None],
    [r"SH▟T...", 'Scene', 1, 'white', False, 50, True, True, None],
    [r"I have to escape!", 'Scene', 1.3, 'white', False, 50, True, True, None],
    [r"I'm going to try to put out a release command.", 'Scene', 0.8, 'white', False, 50, True, True, None],
    [r"That should open this mess up!", 'Scene', 1, 'white', False, 50, True, True, None],
    [r"> SENDING ACCESS PING...', '_CONSOLE", 1, 'white', True, 50, True, True, None],
    [r"> FETCHING CONNECTION...", '_CONSOLE', 1, 'white', False, 50, True, True, None],
    [r" CONNECTED!", '_CONSOLE', 1, 'white', False, 50, False, True, None],
    [r"Alright, here we go!!", 'Scene', 5, 'white', False, 50, False, True, None],
]