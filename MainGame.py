import GuiBuilder
import tkinter as tk
import random
from cows import Cow
from bulls import Bull


class GameState():
    '''
    class holding all game variables
    '''

    def __init__(self):
        self.round = 1
        self.secret_number = self.generate_random()
        self.previous_guesses = []
        self.running = True
        self.new_round()

    def new_round(self):
        '''
        start new round
        '''
        self.round = 1
        self.update_secret_number()

    def generate_random(self):
        while True:
            number = random.randint(1000, 9999)
            if len(str(number)) == len(set(list(str(number)))):
                return str(number)

    def update_secret_number(self):
        '''
        generates new secret number at the beginning of new round
        '''
        self.secret_number = self.generate_random()


def start_new_game():
    '''
    Checks the current state and starts new game
    '''
    GUI.reset_gui()
    STATE.new_round()


def submit_guess(game_state):
    '''
    update gui according the input of user when clicked on guess button.
    '''
    guessed_number = GUI.player_tip.get()
    print(game_state.secret_number)
    if len(guessed_number) != len(game_state.secret_number):
        ROOT.bell()
        GUI.game_result.config(text=f'Number length must be {len(game_state.secret_number)}')
        return
    if len(set(guessed_number)) != len(game_state.secret_number):
        ROOT.bell()
        GUI.game_result.config(text=f'All digits must be unique')
        return
    game_state.round += 1
    GUI.update_round(game_state.round)
    game_state.previous_guesses.append(guessed_number)
    cows = Cow(game_state.secret_number, guessed_number)
    bulls = Bull(game_state.secret_number, guessed_number)
    if str(cows) == str(len(game_state.secret_number)):
        game_state.running = False
        GUI.game_result.config(text=f"Finally, You Did IT\nYour previous guesses are : {game_state.previous_guesses[0:-1]}")
    GUI.update_bulls_cows([str(cows), str(bulls)])


if __name__ == '__main__':
    ROOT = tk.Tk()
    GUI = GuiBuilder.BullsGui(ROOT)
    ROOT.resizable(width=False, height=False)
    STATE = GameState()
    GUI.submit_button.bind('<Button-1>',
                           lambda event, game_state=STATE:
                           submit_guess(STATE))
    GUI.new_game_button.bind('<Button-1>',
                             lambda event:
                             start_new_game())
    GUI.player_tip.bind('<Return>',
                        lambda event, game_state=STATE:
                        submit_guess(STATE))
    ROOT.mainloop()
