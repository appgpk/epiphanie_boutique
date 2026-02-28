from otree.api import *

doc = ''

class C(BaseConstants):
    NAME_IN_URL = 'this_or_that'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass
    
class Player(BasePlayer):
    like = models.IntegerField()  

class MakeChoice(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        image_path = 'shoes/shoe{}.jpg'.format(player.round_number)
        return dict(image_path=image_path)
     def live_method(player: Player, data):
        if 'like' in data:
            player.like = data['like']

page_sequence = [MakeChoice]
