from Game import Game
from MainMenu import MainMenu
from SecondMenu import SecondMenu

game = Game("Juego Sorpresa", 800, 600)
main_menu = MainMenu()
second_menu = SecondMenu()
main_menu.second_menu = second_menu
second_menu.main_menu = main_menu

game.run(main_menu)
