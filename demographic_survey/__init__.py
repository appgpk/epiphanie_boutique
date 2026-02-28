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
    age = models.IntegerField(label="Quel est votre âge ?")
    gender = models.StringField(
        label="Quel est votre genre ?",
        choices=["Femme", "Homme", "Autre"]
    )
    city = models.StringField(
        label="Dans quelle ville habitez-vous ?"
    )

    shoe_size = models.IntegerField(
        label="Quelle est votre pointure ?"
    )

    buy_shoes = models.StringField(
        label="À quelle fréquence achetez-vous des chaussures ?",
        choices=[
            "1 fois par an",
            "2–3 fois par an",
            "plus de 3 fois par an"
        ]
    )

class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


page_sequence = [Introduction]
