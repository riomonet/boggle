from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

class FlaskTests(TestCase):


    """NEED TO TEST EACH ROUTE ONCE
    /boogle
    /results
    /game_stats

    """

    
    # #example for testing a gameboard
    # def test_render_game_board(self):
    #     with app.test_client() as client:
    #         res = client.get('/render_game_board')
    #         html = res.get_data(as_text=True)
    #         self.assertIn('<h1>Board</h1>',html)

            
    # def test_store_game_board_in_session(self):
    #     with app.test_client() as client:
    #         res = client.get('/render_board')
    #         html = res.get_data(as_text=True)


    def test_board_template(self):
        
        return


            
            






        


