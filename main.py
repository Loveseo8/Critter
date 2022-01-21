# -*- coding: utf8 -*-

class Critter():

    def __init__(self, feeling='great', name='', hunger=0, boredom=0, cleaness=100, communication=100):
        self.feeling = feeling
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.cleaness = cleaness
        self.communication = communication
        self.birth()
        self.talk()

    def __pass_time(self):
        self.boredom += 5
        self.hunger += 5
        self.cleaness -= 5
        self.communication -= 5
        self.mood

    @property
    def mood(self):
        if self.hunger > 100:
            self.hunger = 100
        elif self.hunger < 0:
            self.hunger = 0
        if self.boredom > 100:
            self.boredom = 100
        elif self.boredom < 0:
            self.boredom = 0
        if self.cleaness > 100:
            self.cleaness = 100
        elif self.cleaness < 0:
            self.cleaness = 0
        if self.communication > 100:
            self.communication = 100
        elif self.communication < 0:
            self.communication = 0
        unhappiness = self.boredom + self.hunger - self.cleaness - self.communication
        if 150 < unhappiness < 200:
            self.feeling = "really bad"
        elif 130 < unhappiness < 150:
            self.feeling = "bad"
        elif 100 < unhappiness < 130:
            self.feeling = "could be better"
        elif 60 < unhappiness < 100:
            self.feeling = "normal :/"
        elif 40 < unhappiness < 60:
            self.feeling = "good"
        elif 20 < unhappiness < 40:
            self.feeling = "cool"
        elif 0 <= unhappiness < 20:
            self.feeling = "great"

    def shower(self):
        print()
        print(
            "╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬\n╬╬╬╬╬╬█╬╬╬██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬\n╬╬╬╬╬█╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬\n╬╬╬╬╬█╬╬╬░░╬░░╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬\n╬╬╬╬╬█╬╬╬░░╬░░╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬\n╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬\n╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬\n╬╬╬╬╬█╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬\n╬╬╬╬╬███╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬\n╬╬╬╬╬█╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬\n╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬\n╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬\n╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬\n╬█████████████████████████████████████╬\n╬███╬█░░████░░░█████████░░░████░░█╬███╬\n╬╬█╬╬█████████████████████████████╬╬█╬╬\n╬╬╬╬╬█████░░███████░░██████░░█████╬╬╬╬╬\n╬╬╬╬╬███░░██░░███░░██░░██░░██░░███╬╬╬╬╬\n╬╬╬╬╬╬████░░███████░░██████░░████╬╬╬╬╬╬\n╬╬╬╬╬╬╬█████████████████████████╬╬╬╬╬╬╬\n╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬\n╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬")
        print("Let`s have a shower!")
        self.cleaness += 50
        print("Cleaness -50")
        self.__pass_time()
        print()

    def talk(self):
        print("Hello, my name is", self.name + "!")
        print("Right now I am in a", self.feeling, "mood.\n")
        print("Let`s see my stats:")
        self.status()

    def eat(self):
        print()
        print(
            "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⠄⣿⠄⣿⡇⢸⣿⣿⣿⣿⡏⠄⢻⣿⣿⣿⣿⣿⡿⠋⠁⠄⠈⠙⣿⣿⣿\n⣿⣿⣿⠄⣿⠄⣿⡇⢸⣿⣿⣿⣿⡇⠄⠄⢻⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠸⣿⣿\n⣿⣿⣿⠄⠿⠄⠿⠇⢸⣿⣿⣿⣿⡇⠄⠄⠈⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⣿⣿\n⣿⣿⣿⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⡇⠄⠄⠄⢹⣿⣿⣇⠄⠄⠄⠄⠄⠄⠄⣿⣿\n⣿⣿⣿⣀⠄⠄⠄⢀⣼⣿⣿⣿⣿⡇⠄⠄⠄⢸⣿⣿⣿⣆⠄⠄⠄⠄⠄⣼⣿⣿\n⣿⣿⣿⣿⡇⠄⢸⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⢸⣿⣿⣿⣿⣷⡄⠄⢠⣾⣿⣿⣿\n⣿⣿⣿⣿⡇⠄⢸⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⣾⣿⣿⣿⣿⣿⡇⠄⢸⣿⣿⣿⣿\n⣿⣿⣿⣿⡇⠄⠸⣿⣿⣿⣿⣿⣿⡇⠄⠄⢰⣿⣿⣿⣿⣿⣿⡇⠄⢸⣿⣿⣿⣿\n⣿⣿⣿⣿⠁⠄⠄⣿⣿⣿⣿⣿⣿⡇⠄⠄⢸⣿⣿⣿⣿⣿⣿⠄⠄⠄⣿⣿⣿⣿\n⣿⣿⣿⣿⠄⠄⠄⣿⣿⣿⣿⣿⣿⡇⠄⠄⢸⣿⣿⣿⣿⣿⣿⠄⠄⠄⣿⣿⣿⣿\n⣿⣿⣿⡏⠄⠄⠄⢸⣿⣿⣿⣿⣿⠁⠄⠄⠄⣿⣿⣿⣿⣿⡇⠄⠄⠄⢹⣿⣿⣿\n⣿⣿⣿⡇⠄⠄⠄⢸⣿⣿⣿⣿⣿⠄⠄⠄⠄⣿⣿⣿⣿⣿⡇⠄⠄⠄⢸⣿⣿⣿\n⣿⣿⣿⣿⣄⠄⣠⣾⣿⣿⣿⣿⣿⣧⡀⢀⣼⣿⣿⣿⣿⣿⣷⣄⠄⣠⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("Let`s have a meal!")
        self.hunger -= 50
        print("Hunger -50")
        self.__pass_time()
        print()

    def status(self):
        self.mood
        print()
        print("Right now I am in a", self.feeling, "mood.\n")
        print("hunger:", self.hunger)
        print("boredom:", self.boredom)
        print("cleaness:", self.cleaness)
        print("communication:", self.communication)
        print()

    def play(self):
        print()
        print("──▄▄\n▄▀──▀▄\n█────█\n─▀▄▄▀")
        print("Let`s play!")
        self.boredom -= 50
        print("Boredom -50")
        self.__pass_time()
        print()

    def birth(self):
        print("A new creature has been born!")
        print(
            "▄██▄─────▄██▄\n▀████▄─▄████▀\n─███████████─\n─█─█─────█─█─\n▀█──▀▀▀▀▀──█▀\n──▀▄▄▀▀▀▄▄▀──")
        self.name = input("Give your pet a name: ")

    def walk(self):
        print()
        print(
            "╭╯╯╯╯╮╱╭┻┻┻┻╮╱╭┳┳┳┳╮╱╭╰╮╰╮╮\n┫╰╯╰╯┣╋┫╰╯╰╯┣╋┫╰╯╰╯┣╋┫╰╯╰╯┣╋\n╰━┳┳━╯╱╰━┳┳━╯╱╰━┳┳━╯╱╰━┳┳━╯\n╱╱┛┗╱╱╱╱╱┛┗╱╱╱╱╱┛┗╱╱╱╱╱┛┗╱╱\n")
        print("Let`s go for a walk with friends!")
        self.communication += 50
        print("Communication +50")
        self.__pass_time()
        print()


def main():
    crit = Critter()
    choice = None
    while choice != '0':
        print("0 - Exit\n 1 - Feed\n 2 - See stats\n 3 - Play\n 4 - Shower\n 5 - hang out with friends")
        choice = input("Choose one option: ")
        if choice == "0":
            print()
            print("Bye!")
        elif choice == "1":
            crit.eat()
        elif choice == "2":
            crit.status()
        elif choice == "3":
            crit.play()
        elif choice == "4":
            crit.shower()
        elif choice == "5":
            crit.walk()
        else:
            print("Sorry, there is no such option(")


if __name__ == '__main__':
    main()
    input("\n Press \'Enter\' to exit")
