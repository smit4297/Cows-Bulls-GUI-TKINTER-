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
        self.score = 1
        self.number_len = None
        self.secret_number = None
        self.previous_guesses = []

    def new_score(self):
        '''
        start new score
        '''
        self.score = 1
        self.number_len = None
        self.update_secret_number()

    def generate_random(self):
        range_start = 10 ** (int(self.number_len) - 1)
        range_end = (10 ** int(self.number_len)) - 1
        while True:
            number = random.randint(range_start, range_end)
            if len(str(number)) == len(set(list(str(number)))):
                return str(number)

    def update_secret_number(self):
        '''
        generates new secret number at the beginning of new game
        '''
        self.secret_number = None


def start_new_game():
    '''
    Checks the current state and starts new game
    '''

    GUI.reset_gui()
    STATE.new_score()


def submit_guess(game_state):
    '''
    update gui according the input of user when clicked on guess button.
    '''
    guessed_number = GUI.player_tip.get()
    print(game_state.secret_number)
    if game_state.number_len == None:
        GUI.game_result.config(text="Please Enter Number Of Digits Before Guessing...")
        return
    if guessed_number == "":
        GUI.game_result.config(text='Please Guess The Number To Proceed')
        return
    if len(guessed_number) != len(game_state.secret_number):
        ROOT.bell()
        GUI.game_result.config(text=f'Number length must be {len(game_state.secret_number)}')
        return
    if len(set(guessed_number)) != len(game_state.secret_number):
        ROOT.bell()
        GUI.game_result.config(text=f'All digits must be unique')
        return
    GUI.game_result.config(text='')  #reset all error statements
    game_state.score += 1
    GUI.update_score(game_state.score)
    game_state.previous_guesses.append(guessed_number)
    cows = Cow(game_state.secret_number, guessed_number)
    bulls = Bull(game_state.secret_number, guessed_number)
    if str(cows) == str(len(game_state.secret_number)):
        GUI.game_result.config(
            text=f"Finally, You Did IT\nYour previous guesses are : {game_state.previous_guesses[0:-1]}")
    GUI.update_bulls_cows([str(cows), str(bulls)])


def generate_secret_code(game_state):
    digit_length = GUI.digits.get()
    #if will raise an exception if i click on okay without writing anything
    try:
        if int(digit_length) >= 1 and int(digit_length) <= 10:
            GUI.number_of_digits = int(digit_length)
            game_state.number_len = digit_length
            game_state.secret_number = game_state.generate_random()
            print(game_state.secret_number)
            GUI.game_result.config(text=f"Secret Number of {digit_length} digit Has Been Generated")
        else:
            GUI.game_result.config(text="0 < Number of digits < 11")
    except:
        GUI.game_result.config(text="Please Enter The Number Of Digits To Proceed")


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
    GUI.okay_button.bind('<Button-1>',
                         lambda event, game_state=STATE:
                         generate_secret_code(STATE))
    ROOT.mainloop()
