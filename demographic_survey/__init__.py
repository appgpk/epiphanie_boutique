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
    age = models.IntegerField(label="Quel est votre âge ?",
        choices=[
            [1, "Moins de 18 ans"],
            [2, "18 – 24 ans"],
            [3, "25 – 34 ans"],
            [4, "35 – 44 ans"],
            [5, "45 – 54 ans"],
            [6, "55 ans et plus"],
            [7, "Je préfère ne pas répondre"],
        ],
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

    phone_number = models.StringField(
        label="Quel est votre numéro de téléphone ? (Cette information est nécessaire pour vous contacter en cas de gain, mais elle ne sera pas utilisée à d’autres fins.)",
        blank=False
    )

    purchase_factors = models.LongStringField(
    label="Selon vous, quels sont les principaux facteurs qui influencent votre décision d’acheter ou non une paire de chaussures ?",
    blank=True)

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
    first_choice = models.IntegerField()  
    second_choice = models.IntegerField()  


class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
        
class Demographics1(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'city', 'shoe_size', 'phone_number']
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
    form_fields = ['first_choice', 'second_choice']

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player, timeout_happened):
        a = player.first_choice
        b = player.second_choice
        pair = tuple(sorted([a, b]))   # ex: (1,3) peu importe l'ordre

        treatment_map = {
            (1,2): 1,
            (1,3): 2,
            (1,4): 3,
            (1,5): 4,
            (2,3): 5,
            (2,4): 6,
            (2,5): 7,
            (3,4): 8,
            (3,5): 9,
            (4,5): 10,
        }
        player.treatment = treatment_map.get(pair, 0)
        player.participant.vars['treatment'] = player.treatment



            



page_sequence = [Introduction, Demographics1, Ranking]

""""    budget = models.StringField(
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
    """
