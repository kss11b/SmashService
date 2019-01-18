from flask import Flask, render_template, request, redirect, session, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)
app.secret_key = 'shushmans'

def select_random(category_lists, get_argument):
    return random.choice(category_lists[get_argument])

def random_tier(tier_arg="X"):
    tier = str(tier_arg).upper()
    tier_options = ['S', 'A', 'B', 'C', 'D']
    tier_selection = {
        "S" : [
        'Chrom',
        'Lucina',
        'Marth',
        'Mewtwo',
        'Pikachu',
        'Richter',
        'Simon',
        'Snake',
        'Wario',
        'Yoshi',
        'Peach',
        'Pokemon Trainer',
        'Palutena',
        'Pichu',
        ],
        "A" : [
        'Cloud',
        'Diddy Kong',
        'Falco',
        'Ike',
        'Inkling',
        'Ken',
        'King K Rool',
        'Meta Knight',
        'Olimar',
        'Roy',
        'Sheik',
        'Shulk',
        'Sonic',
        'Young Link',
        'Donkey Kong'
        ],
        "B" : [
        'Bayonetta',
        'Bowser',
        'Captain Falcon',
        'Corrin',
        'Fox',
        'Jigglypuff',
        'Link',
        'Lucario',
        'Luigi',
        'Mario',
        'Mii Brawler',
        'Mii Fighter',
        'Mii Gunner',
        'Mr. Game & Watch',
        'Ness',
        'Ridley',
        'Rosalina & Luma',
        'Ryu',
        'Toon Link',
        'Villager',
        'Wolf',
        'Zelda',
        'Zero Suit Samus',
        ],
        "C" : [
        'Dark Samus',
        'Dr. Mario',
        'Duck Hunt Dog',
        'Ganondorf',
        'Greninja',
        'Ice Climbers',
        'King Dedede',
        'Lucas',
        'Megaman',
        'Pit',
        'R.O.B.',
        'Robin',
        'Samus',
        'Incineroar'
        ],
        "D" : [
        'Bowser Jr.',
        'Dark Pit',
        'Kirby',
        'Little Mac',
        'Wii Fit Trainer',
        'Pac-Man',
        'Isabelle'
        ]
    }
    if tier not in tier_options:
        tier_selection = {'ANY' : tier_selection['D'] + tier_selection['C'] + tier_selection['B'] + tier_selection['A'] + tier_selection['S']}
        tier = 'ANY'
    return jsonify({
    'character' : select_random(tier_selection, tier),
    'tier': tier
    })

def stage_selection(category_arg="Tournament"):
    category = str(category_arg)
    category_options = ['Tournament', 'Switch', 'WiiU', '3DS', 'Wii', 'Gamecube', 'N64', 'Smash-4' 'Legacy']
    print(category, category_arg, 'category')
    if category not in category_options:
        category = random.choice(category_options)
    stage_categories = {
    "Tournament": [
        'Battlefield',
        'Final Destination',
        'Smashville',
        'Kalos Pokemon League',
        'Town and City',
        'Wily Castle',
        'Skyloft',
        'Lylat Cruise',
        'Wario Ware',
        'Rainbow Cruise',
        'Frigate Orpheon',
    ],
    "Switch": [
        'Battlefield',
        'Big Battlefield',
        'Dracula’s Castle',
        'Final Destination',
        'New Donk City',
        'Moray Towers',
        'Great Plateau Tower'
    ],
    'WiiU': [
        'Town and City',
        'Umbra Tower Clock',
        'Duck Hunt',
        'Midgar',
        'Coliseum',
        'Flat Zone X',
        'Gamer',
        'Palutena’s Temple',
        'The Great Cave Offensive',
        'Mario Circuit',
        'Wily Castle',
        'Pac-Land',
        'Garden of Hope',
        'Pilotwings',
        'Kalos Pokemon League',
        'Boxing Ring',
        'Windy Hill Zone',
        'Suzaku Castle',
        'Mario Galaxy',
        'Mushroom Kingdom U',
        'Super Mario Maker',
        'Skyloft',
        'Wii Fit Studio',
        'Wrecking Crew',
        'Wuhu Island',
        'Gaur Plain'
    ],
    "3DS": [
        'Tortimer Island',
        'Balloon Fight',
        'Magicant',
        'Mute City SNES',
        'Arena Ferox',
        'Reset Bomb Forest',
        'Dream Land GB',
        'Living Room',
        'Paper Mario',
        'Pictochat 2',
        'Prism Tower',
        'Unova Pokemon League',
        'StreetPass Quest',
        '3D Land',
        'Golden Plains',
        'Gerudo Valley',
        'Spirit Train',
        'omodachi Life'
    ],
    "Wii" : [
        'Smashville',
        '75 m',
        'New Pork City',
        'Electroplankton Hanenbow',
        'Port Town Arena Dive',
        'Castle Siege',
        'Summit',
        'Skyworld',
        'Halberd',
        'Luigi’s Mansion',
        'Figure-8 Circuit',
        'Shadow Moses Island',
        'Frigate Orpheon',
        'Norfair',
        'Distant Planet',
        'Pokemon Stadium 2',
        'Spear Pillar',
        'Green Hill Zone',
        'Lylat Castle',
        'Delfino Plaza',
        'Mario Bros',
        'Mushroomy Kingdom',
        'Bridge of Eldin',
        'Pirate Ship',
        'Warioware, Inc.',
        'Yoshi’s Island'
    ],
    "Gamecube" : [
        'Jungle Japes',
        'Kongo Falls',
        'Fourside',
        'Onett',
        'Big Blue',
        'Fountain of Dreams',
        'Green Greens',
        'Brinstar of Depths',
        'Brinstar',
        'Pokemon Stadium',
        'Corneria',
        'Venom',
        'Mushroom Kingdom 2',
        'Princess Peach’s Castle',
        'Rainbow Cruise',
        'Green Bay',
        'Temple',
        'Yoshi’s Island',
        'Yoshi’s Story'
    ],
    "N64" : [
        'Kongo Jungle',
        'Dream Land',
        'Saffron City',
        'Mushroom Kingdom',
        'Peach’s Castle',
        'Hyrule Castle',
        'Super Happy Tree'
    ]}

    stage_categories['Smash-4'] = stage_categories['WiiU'] + stage_categories['3DS']
    stage_categories['Legacy'] = stage_categories['Gamecube'] + stage_categories['N64']
    stage_categories['All'] = stage_categories['Smash-4'] + stage_categories['Legacy'] + stage_categories['Switch'] + stage_categories['Wii']

    return jsonify(select_random(stage_categories, category))

@app.route('/smash')
def index():
    return render_template("smash.html")

@app.route('/tier/<tier_arg>')
def tier_with_arg(tier_arg):
    return random_tier(tier_arg)

@app.route('/tier')
def tier():
    return random_tier()

@app.route('/stage/<category_arg>')
def stage_with_arg(category_arg):
    return stage_selection(category_arg)

@app.route('/stage')
def stage():
    return stage_selection()

app.run(debug=True)
