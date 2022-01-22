from gameplay.cards import cards

point_limit = 1000


class thrower:

    """This class in meant to organize the game"""

    def hilo(self):

        self.cards = cards()
        self.play = False
        self.score = 0
        self.fist_card = 0
        self.next_card = 0
        self.guess = ""

    def start(self):
        "This Starts the game"

        self.playerpoints = 300
        self.play = True

        while self.play and self.playerpoints > 0 and self.playerpoints < point_limit:
            self.get_guess()
            self.do_logic()
            self.do_display()

    def get_guess(self):
        """ This funciton displays the first card and takes the player's guess 
            (high or low card) as an input"""

        self.first_card = self.cards.draw()
        print(f"The card is: {self.first_card}")

        self.guess = input(f"High or Low? [h/l]").lower()

        while self.guess != "h" and self.guess != "1":
            print("Invalid selection, please try again. ")
            self.guess = input(f"High or Low? [h/l]").lower()
        self.next_card = self.cards.draw()

        print(f"Next card was: {self.next_card}")

    def do_logic(self):
        "This function keeps track of the score"

        if self.guess == "1":
            if self.next_card <= self.first_card:
                self.playerpoints += 100
            else:
                self.playerpoints -= 75
        elif self.guess == "h":
            if self.next_card >= self.first_card:
                self.player_points += 100
            else:
                self.playerpoints -= 75
        elif self.playerpoint < 75:
            self.play = False

    def do_display(self):
        """This functions prints the results and if the score isn't 0, it will ask if user wants to play again"""

        print(f"Your socre is: {self.playerpoints}")
        if self.play == False:
            print("Game Over!")
            print(f"Your final score was {self.playerpoints}")
