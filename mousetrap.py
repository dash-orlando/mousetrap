import  numpy       as np
import  time
import  pyautogui

pyautogui.FAILSAFE      = False
start                   = time.time()
current                 = 0
limit                   = 10

while True:
    if current > limit:
        rand_move       = np.random.randint(-200, 200, size=2)
        pyautogui.moveRel(rand_move[0], rand_move[1], duration = 1)
        start           = time.time()
        current         = 0

    current = time.time() - start
    print( current )
