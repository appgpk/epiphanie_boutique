from otree.api import *

doc = ''

class C(BaseConstants):
    NAME_IN_URL = 'this_or_that'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 4


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass
    
class Player(BasePlayer):
    like = models.IntegerField()  
    treatment = models.IntegerField()
    choice = models.IntegerField()
    style_left = models.IntegerField(blank=True)
    style_right = models.IntegerField(blank=True)

class MakeChoice(Page):
    form_model = 'player'
    form_fields = ['choice']

    @staticmethod
    def vars_for_template(player: Player):
        if player.participant.vars['treatment'] == 1 : 
            image_path_1 = 'shoes/ballerines/shoes0{}.png'.format(player.round_number)
            image_path_2 = 'shoes/mocassins/shoes0{}.png'.format(player.round_number)
        else : 
            image_path = None
        round = C.NUM_ROUNDS
        return dict(image_path_1=image_path_1, image_path_2=image_path_2, round = round)
        




page_sequence = [MakeChoice]


