import random

class Game():
    def __init__(self):
        self.doors = self.generate_doors()
        self.player_choice = self.doors.pop(random.randint(0, 2))

    def generate_doors(self):
        doors = [False, False, False]
        doors[random.randint(0,2)] = True
        return doors

    def reveal_door(self):
        self.doors.remove(False)

    def switch(self):
        if self.player_choice: self.player_choice = False
        else: self.player_choice = True

def play_door_switch():
    game_one = Game()
    game_one.reveal_door()
    game_one.switch()
    return game_one.player_choice

def play_no_switching():
    game_one = Game()
    return game_one.player_choice

def calculate_percentage(total_games, wins):
    return (wins / total_games) * 100

def repeat_play(amount):
    i = 0
    wins_switching = 0
    wins_not_switching = 0
    while i < amount:
        if play_door_switch(): wins_switching += 1
        if play_no_switching(): wins_not_switching += 1
        i += 1
    win_percentage_switching = calculate_percentage(amount, wins_switching)
    win_percentage_not_switching = calculate_percentage(amount, wins_not_switching)
    return (
        f"Switching doors: {win_percentage_switching}% chance of winning.\n"
        f"Not switching:   {win_percentage_not_switching}% chance of winning."
    )

if __name__ == "__main__":
    print(repeat_play(int(input("Amount of simulations: "))))

