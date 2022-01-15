import boss
import dragon
import battle
import json

# info
def import_info(filename:str)->list:
    with open(filename) as f:
        info = json.load(f)
        dragons = []
    for key in info:
        dragons.append(dragon.Dragon(key[0], key[1], key[2], key[3], key[4], key[5]))
    return dragons

enemy = boss.Boss(1000, 50, 5)  ##可以调高伤害，使角色容易死
dragons = import_info("dragons.json")
# 加高伤害时试出了角色死亡了任然能替换上场的BUG0
# zehpy = dragon.Dragon("Zephy", 200, 50, 70, 4, 1)
# charlotta = dragon.Dragon("Charlotta", 100, 100, 200, 6, 2)
# minessa	= dragon.Dragon("Minessa", 150, 40, -60, 3, 0)
# karikaro = dragon.Dragon("Karikaro", 130, 50, 70, 4, 1)
# laponette = dragon.Dragon("Laponette", 80, 30, -30, 1, 0)
# faria = dragon.Dragon("Faria", 150, 40, 100, 4, 2)


front_dragons = []
back_dragons = dragons[:]
message = "There are:\n"

value = 0
for key in dragons:
    value += 1
    message += f"{value}: {key.name}\t"
message += "\navailable. Input 1 - 6 to choose 3 of them."
print(message)

while len(front_dragons) < 3:
    key = int(input())
    if 1 <= key <= 6:
        front_dragons.append(dragons[key - 1])
        print(f"{dragons[key - 1].name} added.")
    else:
        print(f"Invalid input.")
for key in front_dragons:
    back_dragons.remove(key)

game = battle.BattleField(enemy, front_dragons, back_dragons)


def game_over():
    if game.win:
        print(f"Congratulations, you win!!")
    else:
        print(f"Oh no, you loose")


while not game.over:
    game.ap()
    if game.boss_turn():
        break
    if game.player_turn():
        break

game_over()
