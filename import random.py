import random
import keyboard, time, os

box = [[0 for j in range(10)] for j in range(10)]
for i in box:
    print(*i)

box[0][0] = 1
head = [0, 0]
food = [random.randint(0, 9), random.randint(0, 9)]
box[food[0]][food[1]] = 2
path = [[0, 0]]
length = 1

def move_up():
    global head, length, food
    if head[0] - 1 < 0 or box[head[0] - 1][head[1]] == 1:
        print("Game Over")
        os._exit(0)
    head[0] -= 1
    update_game()

def move_down():
    global head, length, food
    if head[0] + 1 > 9 or box[head[0] + 1][head[1]] == 1:
        print("Game Over")
        os._exit(0)
    head[0] += 1
    update_game()

def move_left():
    global head, length, food
    if head[1] - 1 < 0 or box[head[0]][head[1] - 1] == 1:
        print("Game Over")
        os._exit(0)
    head[1] -= 1
    update_game()

def move_right():
    global head, length, food
    if head[1] + 1 > 9 or box[head[0]][head[1] + 1] == 1:
        print("Game Over")
        os._exit(0)
    head[1] += 1
    update_game()

def update_game():
    os.system('cls')
    global head, length, food, path, box
    if head == food:
        length += 1
        box[food[0]][food[1]] = 1
        while True:
            food = [random.randint(0, 9), random.randint(0, 9)]
            if food not in path:
                break
        box[food[0]][food[1]] = 2
    if len(path) >= length:
        tail = path.pop(0)
        box[tail[0]][tail[1]] = 0
    path.append(list(head))
    #box[head[0]][head[1]] = 1
    for i in range(len(path)):
        box[path[i][0]][path[i][1]] = 1
    for i in box:
        print(*i)
    keyboard.add_hotkey('up', move_up)
    keyboard.add_hotkey('down', move_down)
    keyboard.add_hotkey('left', move_left)
    keyboard.add_hotkey('right', move_right)
    #time.sleep(0.5)
    

while True:
    keyboard.add_hotkey('up', move_up)
    keyboard.add_hotkey('down', move_down)
    keyboard.add_hotkey('left', move_left)
    keyboard.add_hotkey('right', move_right)
    if keyboard.is_pressed('esc'):
        break
    
