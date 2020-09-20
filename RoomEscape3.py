from bangtal import *
# pip install bantal

#Define Scene

scene1 = Scene('room 1', 'Images/배경-1.png')
scene2 = Scene('room 2', 'Images/배경-2.png')
scene3 = Scene('room3', 'Images/배경-3.png')


#Define Object

#scene 1 object

door1 = Object('Images/문-오른쪽-닫힘.png')
door1.locate(scene1, 800, 270)
door1.show()
door1.closed = True

hole = Object('Images/hole.png')
hole.locate(scene1, 150, 120)
hole.setScale(0.5)
hole.show()

flowerpot = Object('Images/화분.png')
flowerpot.posX = 550
flowerpot.posY = 150
flowerpot.movable = True
flowerpot.locate(scene1, flowerpot.posX, flowerpot.posY)
flowerpot.show()

holeup = Object('Images/holeup.png')
holeup.locate(scene1, 800, 100)
holeup.setScale(0.5)
holeup.hide()

key1 = Object('Images/key_yellow.png')
key1.setScale(0.1)
key1.locate(scene1, 920, 150)
key1.hide()

#scene 2 object

door2 = Object('Images/문-왼쪽-열림.png')
door2.locate(scene2, 320, 270)
door2.show()
door2.closed = False

door3 = Object('Images/문-오른쪽-닫힘.png')
door3.locate(scene2, 910, 270)
door3.show()
door3.closed = True
door3.locked = True

switch = Object('Images/스위치.png')
switch.locate(scene2, 880, 440)
switch.show()
switch.lighted = True
switch.count = 0

table = Object('Images/table_normal.png')
table_x, table_y = 630, 40
table.locate(scene2, table_x, table_y)
table.show()
table.broken = False

#error: process double click issue
table_broken = Object('Images/table_broken.png')
table_broken.hide()

key2 = Object('Images/key_black.png')
key2.setScale(0.1)
key2.hide()
key2.locate(scene2, 500, 150)


#scene 3

door4 = Object('Images/문-왼쪽-열림.png')
door4.locate(scene3, 320, 250)
door4.show()
door4.closed = False

door5 = Object('Images/문-오른쪽-닫힘.png')
door5.locate(scene3, 910, 250)
door5.show()
door5.closed = True
door5.locked = True

hint = Object('Images/hint.png')
hint.locate(scene3, 400, 100)
hint.setScale(0.3)
hint.show()



#Define Fucntion

#scene1
def door1_onMouseAction(x, y, action):
    if door1.closed == True:
        if key1.inHand():
            door1.setImage('Images/문-오른쪽-열림.png')
            door1.closed = False
        else:
            showMessage('열쇠가 필요해!!')
    else:
        scene2.enter()

door1.onMouseAction = door1_onMouseAction


def flowerpot_onMouseAction(x, y, action):
    if flowerpot.movable == True:
        if action == MouseAction.DRAG_LEFT:
            flowerpot.posX -= 155
            flowerpot.locate(scene1, flowerpot.posX, flowerpot.posY)
        elif action == MouseAction.DRAG_RIGHT:
            flowerpot.posX += 155
            flowerpot.locate(scene1, flowerpot.posX, flowerpot.posY)

    if flowerpot.posX == 240:
        hole.hide()
        flowerpot.movable = False
        #flowerpot.posY -= 20
        flowerpot.setImage('Images/flowerpot_down.png')
        flowerpot.setScale(0.2)
        flowerpot.locate(scene1, 100, 95)
        holeup.show()
        key1.show()

flowerpot.onMouseAction = flowerpot_onMouseAction


def key1_onMouseAction(x, y, action):
    key1.pick()

key1.onMouseAction = key1_onMouseAction


#scene2
def table_onMouseAction(x, y, action):
    global table_x, table_y
    if table.broken == False:
        if action == MouseAction.DRAG_LEFT:
            table_x-=3
            table_y+=0
            table.locate(scene2, table_x, table_y)
        elif action == MouseAction.DRAG_RIGHT:
            table_x+=3
            table_y-=1
            table.locate(scene2, table_x, table_y)
        elif action == MouseAction.CLICK:
            #table.setImage('Images/table_broken.png')
            table_broken.locate(scene2, table_x, table_y-80)
            table.broken = True
            #sleep(5)
            table.hide()
            table_broken.show()
    #if table.broken == True:
    #    if action == MouseAction.CLICK:
            #table.pick()

table.onMouseAction = table_onMouseAction


def door2_onMouseAction(x, y, action):
    scene1.enter()

door2.onMouseAction = door2_onMouseAction


def table_broken_onMouseAction(x, y, action):
    global table_x, table_y
    if action == MouseAction.CLICK:
        table_broken.hide()
        table_broken.pick()

table_broken.onMouseAction = table_broken_onMouseAction


def door3_onMouseAction(x, y, action):
    if door3.closed == True:
        if key1.inHand():
            door3.setImage('Images/문-오른쪽-열림.png')
            door3.closed = False
        else:
            showMessage('열쇠가 필요해!!')
    else:
        scene3.enter()

door3.onMouseAction = door3_onMouseAction


def switch_onMouseAction(x, y, action):
    switch.lighted = not switch.lighted
    switch.count += 1
    if switch.lighted == True:
        scene2.setLight(1)
    else:
        scene2.setLight(0.25)
        key2.hide()

    if switch.count % 4 == 2:
        key2.show()
switch.onMouseAction = switch_onMouseAction


def key2_onMouseAction(x, y, action):
    key2.pick()
    hint.hide()

key2.onMouseAction = key2_onMouseAction


#scene3
def door4_onMouseAction(x, y, action):
    scene2.enter()

door4.onMouseAction = door4_onMouseAction


def door5_onMouseAction(x, y, action):
    if door5.closed == True:
        if key2.inHand():
            door5.setImage('Images/문-오른쪽-열림.png')
            door5.closed = False
        else:
            showMessage('열쇠가 필요해!!')
    else:
        endGame()

door5.onMouseAction = door5_onMouseAction



#Game Start
startGame(scene1)