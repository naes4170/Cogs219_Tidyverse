from psychopy import visual, event, core # import the bits of PsychoPy we'll need for this walkthrough
import os

#open a window
win = visual.Window([800,800],color="grey", units='pix', checkTiming=False) 

#path
script_dir=os.path.dirname(os.path.abspath(__file__))

#grassy field
field_path = os.path.join(script_dir,"stimuli","images","GrassyField.png")
field = visual.ImageStim(win,image=field_path,size=[800,800])

#create an image
bulbie_path=os.path.join(script_dir,"stimuli","images","bulbasaur.png")
bulbie = visual.ImageStim(win,image=bulbie_path,size=[200,200])

# create a mouse
mouse = event.Mouse(win=win)

#show the image
field.draw()
bulbie.draw()
win.flip()

#make bulbie draggable
max_time = 10
dragging_timer = core.Clock()
dragging_timer.reset()

while dragging_timer.getTime() <= max_time:
    while mouse.isPressedIn(bulbie):
        bulbie.pos = mouse.getPos()
        field.draw()
        bulbie.draw()
        win.flip()
        if dragging_timer.getTime() > max_time:
            break

print(dragging_timer.getTime())

win.close() #close the window
core.quit() #quit out of the program

