import microbit
import random

# definition of functions
..........
..........
..........

# settings
target_x = 2
target_y = 2
nb_submarines = 4
submarine_life = 2

# create board and place submarines
..........

# show where target is right now
microbit.display.set_pixel(target_x, target_y, 9)
    
# loop until game is over
game_is_over = False
while not game_is_over:
    # loop until an action is chosen (fire or sonar)
    order = ''
    while ..........:
        # check if a button is pressed, the micro:bit is moved, etc.
        ..........
         
        # wait a few milliseconds before checking again
        microbit.sleep(500)
   
    # execute order (fire or sonar)
    ..........
    
    # wait a few seconds and clear screen
    microbit.sleep(2500)
    microbit.display.clear()
    
    # check if game is not over
    game_is_over = ..........
    
    if not game_is_over:
	    # update position of submarines
	    ..........
	    
	    # update direction of submarines
	    ..........

# tell that the game is over
microbit.display.scroll(.........., delay=100)