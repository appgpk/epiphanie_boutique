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
    age = models.IntegerField(
        label="Quel est votre âge ?",
        min=10, max=99,
        blank=True
    )

    gender = models.StringField(
        label="Quel est votre genre ?",
        choices=["Femme", "Homme", "Autre", "Je préfère ne pas répondre"],
        blank=True
    )

    city = models.StringField(
        label="Dans quelle ville habitez-vous ?",
        blank=True
    )

    shoe_size = models.IntegerField(
        label="Quelle est votre pointure ?",
        blank=True
    )

    budget = models.StringField(
        label="Quel budget mettez-vous en général pour une paire de chaussures ?",
        choices=[
            "Moins de 5 000 FCFA",
            "5 000 – 10 000 FCFA",
            "10 000 – 15 000 FCFA",
            "15 000 – 25 000 FCFA",
            "Plus de 25 000 FCFA",
            "Je préfère ne pas répondre",
        ],
        blank=True
    )

    frequency = models.StringField(
        label="À quelle fréquence achetez-vous des chaussures ?",
        choices=[
            "1 fois par an",
            "2–3 fois par an",
            "1 fois par mois",
            "Plus d’1 fois par mois",
            "Je préfère ne pas répondre",
        ],
        blank=True
    )

class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
        
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'city', 'shoe_size', 'budget', 'frequency']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

page_sequence = [Introduction, Demographics]
