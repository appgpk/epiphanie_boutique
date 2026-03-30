from otree.api import *
import random

doc = ''

# ── Constantes globales (hors classe) ────────────────────────────────────────

STYLE_IMAGES = {
    1: ['shoes_v2/ballerines/shoes01.png',
        'shoes_v2/ballerines/shoes02.png',
        'shoes_v2/ballerines/shoes03.png',
        'shoes_v2/ballerines/shoes04.png'],

    2: ['shoes_v2/mocassins/shoes01.png',
        'shoes_v2/mocassins/shoes02.png',
        'shoes_v2/mocassins/shoes03.png'],

    3: ['shoes_v2/mules/high/wedge/shoes01.png',
        'shoes_v2/mules/low_kitten/kitten/shoes01.png',
        'shoes_v2/mules/low_kitten/stiletto/shoes01.png',
        'shoes_v2/mules/low_kitten/stiletto/shoes02.png',
        'shoes_v2/mules/medium/block/shoes01.png',
        'shoes_v2/mules/medium/block/shoes02.png',
        'shoes_v2/mules/medium/block/shoes03.png',
        'shoes_v2/mules/medium/block/shoes04.png',
        'shoes_v2/mules/medium/spool/shoes01.png',
        'shoes_v2/mules/medium/stiletto/shoes01.png',
        'shoes_v2/mules/medium/stiletto/shoes02.png',
        'shoes_v2/mules/medium/stiletto/shoes03.png'],

    4: ['shoes_v2/sandals/flat/category-0/shoes01.png',
        'shoes_v2/sandals/flat/category-0/shoes02.png',
        'shoes_v2/sandals/flat/category-1/shoes01.png',
        'shoes_v2/sandals/flat/category-1/shoes02.png',
        'shoes_v2/sandals/flat/category-1/shoes03.png',
        'shoes_v2/sandals/flat/category-2/shoes01.png',
        'shoes_v2/sandals/flat/category-2/shoes02.png',
        'shoes_v2/sandals/flat/category-2/shoes03.png',
        'shoes_v2/sandals/flat/category-2/shoes04.png',
        'shoes_v2/sandals/flat/category-2/shoes05.png',
        'shoes_v2/sandals/high/spool/shoes01.png',
        'shoes_v2/sandals/high/spool/shoes02.png',
        'shoes_v2/sandals/high/stiletto/shoes01.png',
        'shoes_v2/sandals/high/stiletto/shoes02.png',
        'shoes_v2/sandals/high/stiletto/shoes03.png',
        'shoes_v2/sandals/high/stiletto/shoes04.png',
        'shoes_v2/sandals/high/stiletto/shoes05.png',
        'shoes_v2/sandals/medium/block/shoes01.png',
        'shoes_v2/sandals/medium/block/shoes02.png',
        'shoes_v2/sandals/medium/spool/shoes01.png',
        'shoes_v2/sandals/medium/spool/shoes02.png'],

    5: ['shoes_v2/slingback/flat/shoes01.png',
        'shoes_v2/slingback/flat/shoes02.png',
        'shoes_v2/slingback/flat/shoes03.png',
        'shoes_v2/slingback/flat/shoes04.png',
        'shoes_v2/slingback/high/block/shoes01.png',
        'shoes_v2/slingback/high/stiletto/shoes01.png',
        'shoes_v2/slingback/high/stiletto/shoes02.png',
        'shoes_v2/slingback/low_kitten/block/shoes01.png',
        'shoes_v2/slingback/low_kitten/kitten/shoes01.png',
        'shoes_v2/slingback/low_kitten/kitten/shoes02.png',
        'shoes_v2/slingback/low_kitten/spool/shoes01.png',
        'shoes_v2/slingback/low_kitten/spool/shoes02.png',
        'shoes_v2/slingback/low_kitten/spool/shoes03.png',
        'shoes_v2/slingback/low_kitten/spool/shoes04.png',
        'shoes_v2/slingback/medium/stiletto/shoes01.png',
        'shoes_v2/slingback/medium/stiletto/shoes02.png',
        'shoes_v2/slingback/medium/block/shoes01.png',
        'shoes_v2/slingback/medium/block/shoes02.png',
        'shoes_v2/slingback/medium/block/shoes03.png',
        'shoes_v2/slingback/medium/block/shoes04.png',
        'shoes_v2/slingback/medium/block/shoes05.png',
        'shoes_v2/slingback/medium/block/shoes06.png',
        'shoes_v2/slingback/medium/block/shoes07.png',
       ],
}

TREATMENT_MAP = {
    1:  {'top2': [1, 2], 'others': [3, 4, 5]},
    2:  {'top2': [1, 3], 'others': [2, 4, 5]},
    3:  {'top2': [1, 4], 'others': [2, 3, 5]},
    4:  {'top2': [1, 5], 'others': [2, 3, 4]},
    5:  {'top2': [2, 3], 'others': [1, 4, 5]},
    6:  {'top2': [2, 4], 'others': [1, 3, 5]},
    7:  {'top2': [2, 5], 'others': [1, 3, 4]},
    8:  {'top2': [3, 4], 'others': [1, 2, 5]},
    9:  {'top2': [3, 5], 'others': [1, 2, 4]},
    10: {'top2': [4, 5], 'others': [1, 2, 3]},
}

STYLE_NAMES = {
    1: 'Ballerines',
    2: 'Mocassins',
    3: 'Mules',
    4: 'Sandals',
    5: 'Slingback',
}


# ── Fonction globale ──────────────────────────────────────────────────────────
import random
def generate_pairs_for_treatment(treatment, n_pairs_per_comparison=4):
    mapping = TREATMENT_MAP[treatment]
    top2 = mapping['top2']
    others = mapping['others']
    pairs = []

    for preferred in top2:
        for other in others:
            images_1 = STYLE_IMAGES[preferred][:]
            images_2 = STYLE_IMAGES[other][:]

            random.shuffle(images_1)
            random.shuffle(images_2)

            for path1, path2 in zip(images_1[:n_pairs_per_comparison],
                                    images_2[:n_pairs_per_comparison]):
                pairs.append({
                    'style_1': preferred,
                    'path_1': path1,
                    'style_2': other,
                    'path_2': path2,
                })

    random.shuffle(pairs)
    return pairs

# ── Classes oTree ─────────────────────────────────────────────────────────────

class C(BaseConstants):
    NAME_IN_URL      = 'this_or_that'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS       = 50

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment    = models.IntegerField()
    choice       = models.IntegerField()
    image_path_1 = models.StringField()
    image_path_2 = models.StringField()
    style_1      = models.IntegerField(blank=True)
    style_2      = models.IntegerField(blank=True)


# ── Pages ─────────────────────────────────────────────────────────────────────
class MakeChoice(Page):
    form_model  = 'player'
    form_fields = ['choice']

    def is_displayed(player):
        # Initialiser les paires au premier affichage
        if 'pairs' not in player.participant.vars:
            treatment = player.participant.vars.get('treatment')
            if treatment is None:
                return False  # sécurité
            pairs = generate_pairs_for_treatment(treatment)
            player.participant.vars['pairs']               = pairs
            player.participant.vars['current_pair_index'] = 0

        idx   = player.participant.vars.get('current_pair_index', 0)
        pairs = player.participant.vars.get('pairs', [])
        return idx < len(pairs)

    def vars_for_template(player):
        idx  = player.participant.vars['current_pair_index']
        pairs = player.participant.vars['pairs']

        if not pairs or idx >= len(pairs):
            return {}

        pair = pairs[idx]
        player.image_path_1 = pair['path_1']
        player.image_path_2 = pair['path_2']
        player.style_1      = pair['style_1']
        player.style_2      = pair['style_2']

        return {
            'image_path_1': pair['path_1'],
            'image_path_2': pair['path_2'],
            'style_1_name': STYLE_NAMES[pair['style_1']],
            'style_2_name': STYLE_NAMES[pair['style_2']],
            'current':      idx + 1,
            'total':        len(pairs),
        }

    def before_next_page(player, timeout_happened):
        player.participant.vars['current_pair_index'] += 1
        
class End(Page):
    def is_displayed(player):
        # Show only when all pairs have been answered
        idx = player.participant.vars.get('current_pair_index', 0)
        pairs = player.participant.vars.get('pairs', [])
        return idx >= len(pairs)

page_sequence = [MakeChoice, End]
