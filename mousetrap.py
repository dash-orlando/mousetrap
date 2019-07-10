'''
    mousetrap.py
        Made to annoy IT
'''

import  numpy       as np
import  time
import  pyautogui

pyautogui.FAILSAFE      = False
start                   = time.time()
current                 = 0
limit                   = 10

print(' Releasing Mouse...')
print('┈┈┈┈┈┈┈╱▔╲┈┈┈┈┈┈')
print('┈┈┈┈┈┈▕╲╲╲▏┈┈┈┈┈')
print('┈┈╱▔╲┈┈╲▂╱┈┈┈┈┈┈')
print('┈▕╲╲▕╱▔╱╲╱╲┈┈┈┈┈')
print('┈┈╲▂╱▏╲╲▕▋▋╱▔▇┈┈')
print('┈┈┈┈▕╲╱▔┈┈┈┈▁╱┈┈')
print('┈┈┈┈┈╲▏┈◥▇▇◤┈┈┈┈')
print('┈┈┈┈┈┈╲▂▂▂╱┈┈┈┈┈')

try:
    while True:
        if current > limit:
            rand_move       = np.random.randint(-200, 200, size=2)
            pyautogui.moveRel(rand_move[0], rand_move[1], duration = 1)
            pyautogui.press('f15')
            start           = time.time()
            current         = 0
            print()
            print("...mouse")
            print('┈┈┈┈┈┈┈╱▔╲┈┈┈┈┈┈')
            print('┈┈┈┈┈┈▕╲╲╲▏┈┈┈┈┈')
            print('┈┈╱▔╲┈┈╲▂╱┈┈┈┈┈┈')
            print('┈▕╲╲▕╱▔╱╲╱╲┈┈┈┈┈')
            print('┈┈╲▂╱▏╲╲▕▋▋╱▔▇┈┈')
            print('┈┈┈┈▕╲╱▔┈┈┈┈▁╱┈┈')
            print('┈┈┈┈┈╲▏┈◥▇▇◤┈┈┈┈')
            print('┈┈┈┈┈┈╲▂▂▂╱┈┈┈┈┈')

        current = time.time() - start
        #print( current )
        
except KeyboardInterrupt:
    print()
    print('...trap!')
    print('┈┈┈┈┈┈┈╱▔╲┈┈┈┈┈┈')
    print('┈┈┈┈┈┈▕╲╲╲▏┈┈┈┈┈')
    print('┈┈╱▔╲┈┈╲▂╱┈┈┈┈┈┈')
    print('┈▕╲╲▕╱▔╱╲╱╲┈┈┈┈┈')
    print('┈┈╲▂╱▏╲╲╳ ╳╱ ▇┈┈')
    print('┈┈┈┈▕╲╱▔┈┈┈┈▁╱┈┈')
    print('┈┈┈┈┈╲▏┈◥▇▇◤┈┈┈┈')
    print('┈┈┈┈┈┈╲▂▂▂╱┈┈┈┈┈')
