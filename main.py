from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from score import Score

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross Road Game")
screen.tracer(0)

player = Player()  # Creating player object
car = CarManager()  # creating car object
score = Score()  # Creating score object

screen.listen()
screen.onkey(key="Up", fun=player.move)

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()

    # Detect collision with car
    for card in car.all_cars:
        if card.distance(player) < 20:
            is_game_on = False
            score.game_over()

    # detect turtle move to the other place
    if player.is_finished_line():
        player.restart()
        car.level_up()
        score.increase_level()

screen.exitonclick()