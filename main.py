import boss
import dragon
import battle
import json


def import_info(filename: str) -> list:
    try:
        with open(filename) as f:
            info = json.load(f)
            dragons = []
    except FileNotFoundError:#其实没有好多用，文件内容可能不正确，等等
        print(f"{filename} not found")
        exit()
    else:
        for key in info:
            dragons.append(dragon.Dragon(key[0], key[1], key[2], key[3], key[4], key[5]))
        return dragons


def print_info(dragons: list):
    message = "There are:\n"
    value = 0
    for key in dragons:
        value += 1
        message += f"{value}: {key.name}\tDamage: {key.damage}\tSkill: {key.skill_damage}\n"
    print(message)


def game_over():
    if game.win:
        print(f"Congratulations, you win!!")
    else:
        print(f"Oh no, you loose")


def choose_dragons(front: list, back: list):
    position = []
    temp = back[:]
    while front:
        front.pop()
    while back:
        back.pop()
    # back = []
    # front= []这种写法是不行的，会取消关联
    message = "Enter 1 -6 to choose, 3 in the front, 3 in the back. once at a time\n"
    print(message)

    position = []
    while len(position) < 6:
        try:
            value = int(input())
        except ValueError:
            print("Error: Please input a number.")
        else:
            if value in position:
                print(f"{temp[value-1].name} is already on the list.")
            elif 1 <= value <= 6:
                position.append(value)
            else:
                print("Error: Enter a number 1 - 6")
    message = "You chose: "
    for key in position[:3]:
        front.append(temp[key - 1])
        message += f"{temp[key - 1].name}\t"
    message += "\nat the front, and:\n"
    for key in position[3:6]:
        back.append(temp[key - 1])
        message += f"{temp[key - 1].name}\t"
    message += "\nin the back"
    print(message)




enemy = boss.Boss(1000, 50, 5)  ##可以调高伤害，使角色容易死
dragons = import_info("dragons.json")
print_info(dragons)

front_dragons = []
back_dragons = dragons[:]
choose_dragons(front_dragons, back_dragons)

game = battle.BattleField(enemy, front_dragons, back_dragons)

while not game.over:
    game.ap()
    if game.boss_turn():
        break
    if game.player_turn():
        break

game_over()
