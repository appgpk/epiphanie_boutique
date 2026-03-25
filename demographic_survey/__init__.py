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
        blank=False
    )

    gender = models.StringField(
        label="Quel est votre genre ?",
        choices=["Femme", "Homme", "Autre", "Je préfère ne pas répondre"],
        blank=False
    )

    city = models.StringField(
        label="Dans quelle ville habitez-vous ?",
        blank=False
    )

    shoe_size = models.IntegerField(
        label="Quelle est votre pointure ?",
        blank=False
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
        blank=False
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
        blank=False
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
        blank=False
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
        choices=[1,2,3,4,5]
    )

    rank2 = models.IntegerField(
        label= " ",
        choices=[1,2,3,4,5]
    )

    rank3 = models.IntegerField(
        label= " ",
        choices=[1,2,3,4,5]
    )
    
    rank4 = models.IntegerField(
        label= " ",
        choices=[1,2,3,4,5]
    )
    
    rank5 = models.IntegerField(
        label= " ",
        choices=[1,2,3,4,5]
    )
    
    treatment = models.IntegerField()


class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
        
class Demographics1(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'city', 'shoe_size', 'budget', 'frequency', 'price_too_expensive' ]
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Demographics2(Page):
    form_model = 'player'
    form_fields = ['purchase_factors', 'purchase_barrier', 'purchase_priority']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
        
class Ranking(Page):
    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank3', 'rank4', 'rank5']

    @staticmethod    
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def error_message(player, values):
        print("Submitted values:", values)
        ranks = [values['rank1'], values['rank2'], values['rank3'], values['rank4'],  values['rank5']]
        print("Ranks:", ranks)
        print("Unique ranks:", set(ranks))

        if len(set(ranks)) != 5:
            return "Chaque modèle doit avoir un rang unique."

    @staticmethod
    def before_next_page(player, timeout_happened):
        if (player.rank1 == 1 and player.rank2 == 2) or (player.rank1 == 2 and player.rank2 == 1):
            player.treatment = 1
        
        elif (player.rank1 == 1 and player.rank3 == 2) or (player.rank1 == 2 and player.rank3 == 1):
            player.treatment = 2
        
        elif (player.rank1 == 1 and player.rank4 == 2) or (player.rank1 == 2 and player.rank4 == 1):
            player.treatment = 3
        
        elif (player.rank1 == 1 and player.rank5 == 2) or (player.rank1 == 2 and player.rank5 == 1):
            player.treatment = 4
        
        elif (player.rank2 == 1 and player.rank3 == 2) or (player.rank2 == 2 and player.rank3 == 1):
            player.treatment = 5
        
        elif (player.rank2 == 1 and player.rank4 == 2) or (player.rank2 == 2 and player.rank4 == 1):
            player.treatment = 6
        
        elif (player.rank2 == 1 and player.rank5 == 2) or (player.rank2 == 2 and player.rank5 == 1):
            player.treatment = 7
        
        elif (player.rank3 == 1 and player.rank4 == 2) or (player.rank3 == 2 and player.rank4 == 1):
            player.treatment = 8
        
        elif (player.rank3 == 1 and player.rank5 == 2) or (player.rank3 == 2 and player.rank5 == 1):
            player.treatment = 9
        
        elif (player.rank4 == 1 and player.rank5 == 2) or (player.rank4 == 2 and player.rank5 == 1):
            player.treatment = 10

        player.participant.vars['treatment'] = player.treatment



            



page_sequence = [Introduction, Demographics1, Demographics2, Ranking]
