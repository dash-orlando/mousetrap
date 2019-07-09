import  numpy       as np
import  time
import  pyautogui

pyautogui.FAILSAFE      = False
start                   = time.time()
current                 = 0
limit                   = 10

try:
    while True:
        if current > limit:
            rand_move       = np.random.randint(-200, 200, size=2)
            pyautogui.moveRel(rand_move[0], rand_move[1], duration = 1)
            pyautogui.click()
            start           = time.time()
            current         = 0
            print("...mouse")

        current = time.time() - start
        #print( current )
        
except KeyboardInterrupt:
    print('...trap!')
