
def game(story, goto):
    for sentence in story:
        print(sentence)
        input()
    select = int(input("Please select?"))
    if select == 1:
        next_stage = goto[0]
    elif select == 2:
        next_stage = goto[1]
    elif select == 3:
        next_stage = goto[2]
    return next_stage


def start(t, m):
    x = 1
    while x != 0:
        x = game(t[x], m[x])
    print("Game over")


game_t = [[], ["hello"], ["continue"], ["end"]]
game_m = [[], [0, 2, 0], [0, 3, 0], [0, 0, 0]]

start(game_t, game_m)
