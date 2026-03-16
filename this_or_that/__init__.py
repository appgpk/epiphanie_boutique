from otree.api import *

doc = ''

class C(BaseConstants):
    NAME_IN_URL = 'this_or_that'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5
    STYLE_IMAGES = {
    1: ['shoes/ballerines/shoes01.png',
        'shoes/ballerines/shoes02.png',
        'shoes/ballerines/shoes03.png',
        'shoes/ballerines/shoes04.png',
        'shoes/ballerines/shoes05.png'],
        
    2: ['shoes/mocassins/shoes01.png',
        'shoes/mocassins/shoes02.png',
        'shoes/mocassins/shoes03.png',
        'shoes/mocassins/shoes04.png'],
        
    3: ['shoes/mules/high/wedge/shoes01.png',
        'shoes/mules/high/wedge/shoes02.png',
        'shoes/mules/low_kitten/kitten/shoes01.png',
        'shoes/mules/low_kitten/kitten/shoes02.png',
        'shoes/mules/low_kitten/kitten/shoes03.png',
        'shoes/mules/low_kitten/kitten/shoes04.png',
        'shoes/mules/low_kitten/kitten/shoes05.png',
        'shoes/mules/low_kitten/kitten/shoes06.png',
        'shoes/mules/low_kitten/stiletto/shoes01.png',
        'shoes/mules/low_kitten/stiletto/shoes02.png',
        'shoes/mules/low_kitten/stiletto/shoes03.png',
        'shoes/mules/low_kitten/stiletto/shoes04.png',
        'shoes/mules/low_kitten/stiletto/shoes05.png',
        'shoes/mules/low_kitten/stiletto/shoes-6.png',
        'shoes/mules/medium/block/shoes01.png',
        'shoes/mules/medium/block/shoes02.png',
        'shoes/mules/medium/block/shoes03.png',
        'shoes/mules/medium/block/shoes04.png',
        'shoes/mules/medium/block/shoes05.png',
        'shoes/mules/medium/block/shoes06.png',
        'shoes/mules/medium/block/shoes07.png',
        'shoes/mules/medium/block/shoes08.png',
        'shoes/mules/medium/block/shoes09.png',
        'shoes/mules/medium/block/shoes10.png',
        'shoes/mules/medium/block/shoes11.png',
        'shoes/mules/medium/block/shoes12.png',
        'shoes/mules/medium/block/shoes13.png',
        'shoes/mules/medium/block/shoes14.png',
        'shoes/mules/medium/spool/shoes01.png',
        'shoes/mules/medium/spool/shoes02.png',
        'shoes/mules/medium/stiletto/shoes01.png',
        'shoes/mules/medium/stiletto/shoes02.png',
        'shoes/mules/medium/stiletto/shoes03.png',
        'shoes/mules/medium/stiletto/shoes04.png',
        'shoes/mules/medium/stiletto/shoes05.png',
        'shoes/mules/medium/stiletto/shoes06.png',
        'shoes/mules/medium/stiletto/shoes07.png',
        'shoes/mules/medium/stiletto/shoes08.png',
        'shoes/mules/medium/stiletto/shoes09.png'],
        
    4: ['sandals/flat/category-0/shoes01.png',
        'sandals/flat/category-0/shoes02.png',
        'sandals/flat/category-0/shoes03.png',
        'sandals/flat/category-0/shoes04.png',
        'sandals/flat/category-0/shoes05.png',
        'sandals/flat/category-0/shoes06.png',
        'sandals/flat/category-0/shoes07.png',
        'sandals/flat/category-0/shoes08.png',
        'sandals/flat/category-0/shoes09.png',
        'sandals/flat/category-0/shoes10.png',
        'sandals/flat/category-0/shoes11.png',
        'sandals/flat/category-0/shoes12.png',
        'sandals/flat/category-0/shoes13.png',
        'sandals/flat/category-0/shoes14.png',
        'sandals/flat/category-0/shoes15.png',
        'sandals/flat/category-0/shoes16.png',
        'sandals/flat/category-0/shoes17.png',
        'sandals/flat/category-0/shoes18.png',
        'sandals/flat/category-0/shoes19.png',
        'sandals/flat/category-0/shoes20.png',
        'sandals/flat/category-0/shoes21.png',
        'sandals/flat/category-0/shoes22.png',
        'sandals/flat/category-0/shoes23.png',
        'sandals/flat/category-0/shoes24.png',
        'sandals/flat/category-1/shoes01.png',
        'sandals/flat/category-1/shoes02.png',
        'sandals/flat/category-1/shoes03.png',
        'sandals/flat/category-1/shoes04.png',
        'sandals/flat/category-1/shoes05.png',
        'sandals/flat/category-1/shoes06.png',
        'sandals/flat/category-1/shoes07.png',
        'sandals/flat/category-1/shoes08.png',
        'sandals/flat/category-1/shoes09.png',
        'sandals/flat/category-1/shoes10.png',
        'sandals/flat/category-1/shoes11.png',
        'sandals/flat/category-1/shoes12.png',
        'sandals/flat/category-2/shoes01.png',
        'sandals/flat/category-2/shoes02.png',
        'sandals/flat/category-2/shoes03.png',
        'sandals/flat/category-2/shoes04.png',
        'sandals/flat/category-2/shoes05.png',
        'sandals/flat/category-2/shoes06.png',
        'sandals/flat/category-2/shoes07.png',
        'sandals/flat/category-2/shoes08.png',
        'sandals/flat/category-2/shoes09.png',
        'sandals/flat/category-2/shoes10.png',
        'sandals/flat/category-2/shoes11.png',
        'sandals/flat/category-2/shoes12.png',
        'sandals/flat/category-2/shoes13.png',
        'sandals/flat/category-2/shoes14.png',
        'sandals/high/spool/shoes01.png',
        'sandals/high/spool/shoes02.png',
        'sandals/high/spool/shoes03.png',
        'sandals/high/spool/shoes04.png',
        'sandals/high/spool/shoes05.png',
        'sandals/high/spool/shoes06.png',
        'sandals/high/stiletto/shoes01.png',
        'sandals/high/stiletto/shoes02.png',
        'sandals/high/stiletto/shoes03.png',
        'sandals/high/stiletto/shoes04.png',
        'sandals/high/stiletto/shoes05.png',
        'sandals/high/stiletto/shoes06.png',
        'sandals/high/stiletto/shoes07.png',
        'sandals/high/stiletto/shoes08.png',
        'sandals/high/stiletto/shoes09.png',
        'sandals/high/stiletto/shoes10.png',
        'sandals/high/stiletto/shoes11.png',
        'sandals/high/stiletto/shoes12.png',
        'sandals/high/stiletto/shoes13.png',
        'sandals/high/stiletto/shoes14.png',
        'sandals/high/stiletto/shoes15.png',
        'sandals/high/stiletto/shoes16.png',
        'sandals/high/stiletto/shoes17.png',
        'sandals/high/stiletto/shoes18.png',
        'sandals/high/stiletto/shoes19.png',        
        'sandals/medium/block/shoes01.png',
        'sandals/medium/block/shoes02.png',
        'sandals/medium/block/shoes03.png',
        'sandals/medium/block/shoes04.png',
        'sandals/medium/block/shoes05.png',
        'sandals/medium/block/shoes06.png',
        'sandals/medium/block/shoes07.png',
        'sandals/medium/block/shoes08.png',
        'sandals/medium/spool/shoes01.png',
        'sandals/medium/spool/shoes02.png',
        'sandals/medium/spool/shoes03.png',
        'sandals/medium/spool/shoes04.png',
        'sandals/medium/spool/shoes05.png',
        'sandals/medium/spool/shoes06.png',
        'sandals/medium/spool/shoes07.png'],
        
    5: ['slingback/flat/category-1/shoes01.png',
        'slingback/flat/category-1/shoes02.png',
        'slingback/flat/category-2/shoes01.png',
        'slingback/flat/category-2/shoes02.png',
        'slingback/flat/category-2/shoes03.png',
        'slingback/flat/category-2/shoes04.png',
        'slingback/flat/category-2/shoes05.png',
        'slingback/flat/category-2/shoes06.png',
        'slingback/flat/category-2/shoes07.png',
        'slingback/flat/category-2/shoes08.png',
        'slingback/flat/category-2/shoes09.png',
        'slingback/flat/category-2/shoes10.png',
        'slingback/flat/category-2/shoes11.png',
        'slingback/flat/category-2/shoes12.png',
        'slingback/flat/category-2/shoes13.png',
        'slingback/high/block/shoes01.png',
        'slingback/high/block/shoes02.png',
        'slingback/high/block/shoes03.png',
        'slingback/high/stiletto/shoes01.png',
        'slingback/high/stiletto/shoes02.png',
        'slingback/high/stiletto/shoes03.png',
        'slingback/high/stiletto/shoes04.png',
        'slingback/high/stiletto/shoes05.png',
        'slingback/high/stiletto/shoes06.png',
        'slingback/low_kitten/block/shoes01.png',
        'slingback/low_kitten/block/shoes02.png',
        'slingback/low_kitten/block/shoes03.png',
        'slingback/low_kitten/block/shoes04.png',
        'slingback/low_kitten/kitten/shoes01.png',
        'slingback/low_kitten/kitten/shoes02.png',
        'slingback/low_kitten/kitten/shoes03.png',
        'slingback/low_kitten/kitten/shoes04.png',
        'slingback/low_kitten/kitten/shoes05.png',
        'slingback/low_kitten/kitten/shoes06.png',
        'slingback/low_kitten/spool/shoes01.png',
        'slingback/low_kitten/spool/shoes02.png',
        'slingback/low_kitten/spool/shoes03.png',
        'slingback/low_kitten/spool/shoes04.png',
        'slingback/low_kitten/spool/shoes05.png',
        'slingback/low_kitten/spool/shoes06.png',
        'slingback/low_kitten/spool/shoes07.png',
        'slingback/low_kitten/spool/shoes08.png',
        'slingback/low_kitten/spool/shoes09.png',
        'slingback/low_kitten/spool/shoes10.png',
        'slingback/low_kitten/spool/shoes11.png',
        'slingback/low_kitten/spool/shoes12.png',
        'slingback/low_kitten/spool/shoes13.png',
        'slingback/low_kitten/spool/shoes14.png',
        'slingback/medium/stiletto/category-1/shoes01.png',
        'slingback/medium/stiletto/category-1/shoes02.png',
        'slingback/medium/stiletto/category-1/shoes03.png',
        'slingback/medium/stiletto/category-1/shoes04.png',
        'slingback/medium/stiletto/category-1/shoes05.png',     
        'slingback/medium/stiletto/category-2/shoes01.png',
        'slingback/medium/stiletto/category-2/shoes02.png',
        'slingback/medium/stiletto/category-2/shoes03.png',        
        'slingback/medium/block/category-0/shoes01.png',
        'slingback/medium/block/category-0/shoes02.png',
        'slingback/medium/block/category-0/shoes03.png',
        'slingback/medium/block/category-0/shoes04.png',
        'slingback/medium/block/category-1/shoes01.png',
        'slingback/medium/block/category-1/shoes02.png',
        'slingback/medium/block/category-1/shoes03.png',
        'slingback/medium/block/category-1/shoes04.png',
        'slingback/medium/block/category-1/shoes05.png',
        'slingback/medium/block/category-1/shoes06.png',
        'slingback/medium/block/category-1/shoes07.png',
        'slingback/medium/block/category-2/shoes01.png',
        'slingback/medium/block/category-2/shoes02.png',
        'slingback/medium/block/category-2/shoes03.png',
        'slingback/medium/block/category-2/shoes04.png',
        'slingback/medium/block/category-2/shoes05.png',
        'slingback/medium/block/category-2/shoes06.png',
        'slingback/medium/block/category-2/shoes07.png',
        'slingback/medium/block/category-2/shoes08.png',
        'slingback/medium/block/category-2/shoes09.png',
        'slingback/medium/block/category-2/shoes10.png',      
        'slingback/medium/block/category-3/shoes01.png',
        'slingback/medium/block/category-3/shoes02.png',
        'slingback/medium/block/category-3/shoes03.png',
        'slingback/medium/block/category-3/shoes04.png',
        'slingback/medium/very-high/stiletto/category-1/shoes01.png',
        'slingback/medium/very-high/stiletto/category-1/shoes02.png',    
        'slingback/medium/very-high/stiletto/category-2/shoes01.png',
        'slingback/medium/very-high/stiletto/category-2/shoes02.png',
        'slingback/medium/very-high/stiletto/category-2/shoes03.png',
        'slingback/medium/very-high/stiletto/category-2/shoes04.png',
        'slingback/medium/very-high/stiletto/category-2/shoes05.png',
        'slingback/medium/very-high/stiletto/category-2/shoes06.png',
        'slingback/medium/very-high/stiletto/category-2/shoes07.png'],
}

PAIRS_TREATMENT_1 = [
    (1, 3),
    (1, 4),
    (1, 5),
    (2, 3),
    (2, 4),
    (2, 5),
]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


    
class Player(BasePlayer):
    treatment = models.IntegerField(initial=1)

    choice = models.IntegerField(
        choices=[
            [1, 'Je préfère le style de gauche'],
            [2, 'Je préfère le style de droite'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label=' ',
    )

    style_left = models.IntegerField(blank=True)
    style_right = models.IntegerField(blank=True)


class MakeChoice(Page):
    form_model = 'player'
    form_fields = ['choice']

    @staticmethod
    def vars_for_template(player: Player):
        treatment = player.treatment

        if treatment == 1:
            style_a, style_b = PAIRS_TREATMENT_1[player.round_number - 1]
        else:
            style_a, style_b = None, None

        if style_a is not None and style_b is not None:
            if not player.style_left and not player.style_right:
                if random.choice([True, False]):
                    player.style_left = style_a
                    player.style_right = style_b
                else:
                    player.style_left = style_b
                    player.style_right = style_a

        return dict(
            left_images=STYLE_IMAGES.get(player.style_left, []),
            right_images=STYLE_IMAGES.get(player.style_right, []),
            round_number=player.round_number,
            num_rounds=C.NUM_ROUNDS,
        )


page_sequence = [MakeChoice]
