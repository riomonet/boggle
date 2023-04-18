from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import time
from boggle import Boggle

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretsarecool'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['TESTING'] = True
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/boggle')
def render_board ():
    board = get_new_board()
    store_board_in_session(board)
    return render_template('/board.html')

@app.route('/results', methods=['POST'])
def results():

    input_from_form = request.get_json()
    word = input_from_form['word']
    answer = check_word(word)
    return produce_json_response(answer)



@app.route('/game_stats', methods=['POST'])
def game_stats():
    input = request.get_json()

    score = input['score']
    session['num_games'] += 1
       
    if int(session['high_score'])  < score:
          session['high_score'] = score
    return jsonify(high_score = session['high_score'], num_games = session['num_games'])

@app.route('/reset')
def reset():
    return redirect ('/boggle')

def get_new_board ():
    board = boggle_game.make_board();
    return  board

def store_board_in_session(board):

    if not session.get('high_score'):
        session['high_score'] = 0

    if not session.get('num_games'):
        session['num_games'] = 0
 
    session['board'] = board

    return session['board']

def check_word(word):
    return boggle_game.check_valid_word(session['board'], word)

def produce_json_response(answer):
    return jsonify(result = answer)

