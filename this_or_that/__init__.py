
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    # built-in constants
    NAME_IN_URL = 'this_or_that'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    choice = models.IntegerField()
def vars_for_template(player: Player):
    return dict(
            image_path='shoes/shoe{}.jpg'.format(player.round_number)
        )
class MakeChoice(Page):
    form_model = 'player'
page_sequence = [MakeChoice]