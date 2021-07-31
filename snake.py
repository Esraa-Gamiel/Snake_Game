import random
import curses

# create a screen
s = curses.initscr()
# disable the cursor
curses.curs_set(0)

# the screen dimentions
h,w=s.getmaxyx

# create a window inside the screen
win=curses.newwin(h,w,0,0)

# enable using computer keypad
 win.keypad(1)

 # setting the time for the screen to refresh it self
win.timeout(100)

# setting the intial snake position
snk_x=w//4
snk_y=h//4
snake=[[snk_y , snk_x],[snk_y  , snk_x -1],[snk_y  , snk_x -2]]

#setting the initial food position
food= [h//2,w//2]
win.addch(food[0], food[1], curses.ACS_PI) # the food shape
# the snake movement direction
key=curses.KEY_RIGHT

while True:
    # how to deal with the keypad inputs
    next_key=win.getch()
    key=key if next_key ==-1 else next_key
    if snake[0][0] in [0,h] or snake[0][1] in [0,w] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    new_head=[snake[0][0],snake[0][1]]
    if key== curses.KEY_DOWN:
        new_head[0]+=1
    elif key== curses.KEY_UP:
        new_head[0]-=1
    elif key== curses.KEY_RIGHT:
        new_head[0]+=1
    elif key== curses.KEY_LEFT:
        new_head[0]-=1
    # change the snake position
    snake.insert(0,new_head)

    if snake[0]==food:
        food=None
        while food is None:
            nf=[random.randint(1,h-1),random.randint(1,w-1)]
            food=nf if nf not in snake else None
        win.addch(food[0],food[1], curses.ACS_PI)
    else:
        tail=snake.pop()
        win.addch(tail[0],tail[1]," ")
    
    win.addch(snake[0][0],snake[0][1], curses.ACS_CKBOARD)
    
