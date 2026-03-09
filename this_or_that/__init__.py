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
    treatment = models.IntegerField()  

class MakeChoice(Page):
    form_model = 'player'
    form_fields = ['like']

    @staticmethod
    def vars_for_template(player: Player):
        if player.participant.treatment == 1 : 
            image_path = 'shoes/shoe{}.jpg'.format(player.round_number)
        else : 
            image_path = 
        round = C.NUM_ROUNDS
        return dict(image_path=image_path, round = round)
        




page_sequence = [MakeChoice]
