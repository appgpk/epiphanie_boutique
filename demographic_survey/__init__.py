from otree.api import *

doc = ''

class C(BaseConstants):
    NAME_IN_URL = 'demographic_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


page_sequence = [Introduction]
