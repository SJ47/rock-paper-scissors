from flask import render_template, request, redirect, url_for
from app import app
from app.models.game import Game
from app.models.player import Player

@app.route("/")
def index():
    title = "Instructions"
    return render_template("index.html", title=title)

# Route for MVP portion of homework
@app.route("/<player1_choice>/<player2_choice>")
def get_player_choices(player1_choice, player2_choice):
    title = "MVP Section"

    player1 = Player("Fred", player1_choice)
    player2 = Player("Barney", player2_choice)

    # Check for the winner
    # check_for_winner = Game()
    # winner = check_for_winner.select_winner(player1, player2)
    winner = Game.select_winner(player1, player2)

    # Return the result
    return render_template("result.html", title=title, player1=player1, player2=player2, winner=winner)


# Routes for extensions and further extensions of homework
@app.route("/play")
def play_game():
    title = "Play Game"
    return render_template("play_game.html", title=title)


@app.route("/play", methods=["POST"])
def get_player1_name():
    title = "Play Game"
    player1=Player(request.form["player1_name"], request.form["player1_selection"])

    # Get computer player choice
    # game = Game()
    # Get random choice - accessing class method directly without instantiating an object
    random_choice = Game.select_computer_random_choice()
    player2 = Player("Computer", random_choice)
    
    # Check for the winner - accessing class method directly without instantiating an object
    # check_for_winner = Game()
    winner = Game.select_winner(player1, player2)

    # return redirect(url_for("play_game", player1_name=player1_name))
    return render_template("play_game.html", title=title, player1_name=player1.name, player1_choice=player1.choice, player2_name=player2.name, player2_choice=player2.choice, winner=winner)
    # return render_template("play_game.html", title=title, player1=player1, player2=player2, winner=winner)
