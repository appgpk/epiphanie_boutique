from otree.api import *

doc = ''

class C(BaseConstants):
    NAME_IN_URL = 'demographic_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10

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
            [1,"Moins de 5 000 FCFA"],
            [2,"5 000 – 10 000 FCFA"],
            [3,"10 000 – 15 000 FCFA"],
            [4,"15 000 – 25 000 FCFA"],
            [5,"Plus de 25 000 FCFA"],
            [6,"Je préfère ne pas répondre"],
        ],
        blank=True
    )

    frequency = models.StringField(
        label="À quelle fréquence achetez-vous des chaussures ?",
        choices=[
            [1,"1 fois par an"],
            [2,"2–3 fois par an"],
            [3,"1 fois par mois"],
            [4,"Plus d’1 fois par mois"],
            [5,"Je préfère ne pas répondre"],
        ],
        blank=True
    )
    purchase_factors = models.LongStringField(
    label="Selon vous, quels sont les principaux facteurs qui influencent votre décision d’acheter ou non une paire de chaussures ?",
    blank=True)

    price_too_expensive = models.IntegerField(
        label="À partir de quel prix considérez-vous qu’une paire de chaussures devient trop chère ?",
        choices=[
            [1, "5 000 FCFA"],
            [2, "10 000 FCFA"],
            [3, "15 000 FCFA"],
            [4, "20 000 FCFA"],
            [5, "Plus de 20 000 FCFA"],
            [6, "Je préfère ne pas répondre"],
        ],
        blank=True
    )
    purchase_barrier = models.LongStringField(
    label="Quel est le principal facteur qui peut vous empêcher d’acheter une paire de chaussures qui vous plaît ? "
          "(Par exemple : le prix, la qualité, la pointure, le style, la durabilité, etc.)",
    blank=True
)

    purchase_priority = models.LongStringField(
        label="Qu’est-ce qui est le plus important pour vous lorsque vous choisissez une paire de chaussures ? "
              "(Par exemple : le confort, le prix, la qualité, le design, la marque, etc.)",
        blank=True
    )
    rank1 = models.IntegerField(
        label= " ",
        choices=[1,2,3]
    )

    rank2 = models.IntegerField(
        label= " ",
        choices=[1,2,3]
    )

    rank3 = models.IntegerField(
        label= " ",
        choices=[1,2,3]
    )
    treatment = models.IntegerField()
    like = models.IntegerField()  


class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
        
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'city', 'shoe_size', 'budget', 'frequency', 'purchase_factors', 'price_too_expensive', 'purchase_barrier', 'purchase_priority']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Ranking(Page):
    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank3']

    @staticmethod    
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def error_message(player, values):
        print("Submitted values:", values)
        ranks = [values['rank1'], values['rank2'], values['rank3']]
        print("Ranks:", ranks)
        print("Unique ranks:", set(ranks))

        if len(set(ranks)) != 3:
            return "Chaque modèle doit avoir un rang unique."
            
    @staticmethod
    def before_next_page(player, timeout_happened):

        if player.rank1 == 1:
            player.participant.treatment = 1

        elif player.rank2 == 1:
            player.participant.treatment = 2

        elif player.rank3 == 1:
            player.participant.treatment = 3


class MakeChoice(Page):
    form_model = 'player'
    form_fields = ['like']

    @staticmethod
    def vars_for_template(player: Player):
        image_path = 'shoes/shoe{}.jpg'.format(player.round_number)
        round = C.NUM_ROUNDS
        return dict(image_path=image_path, round = round)
page_sequence = [Introduction, Demographics, Ranking]
