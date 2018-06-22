input_html = open('input.html')
html = input_html.read()
output = open('output.html', 'w')

#    'placeholder=\"charname\"': 'placeholder=\"Trinitrogen\"',


data_dict = {
    'charname': 'Trinitrogen',
    'classlevel': 'Rogue 1',
    'Background': 'Criminal',
    'PlayerName': ' ',
    'race': 'Half-Elf',
    'alignment': 'Chaotic Neutral',
    'experiencepoints': '90',
    'inspiration': ' ',
    'proficiencybonus': '2',
    'Strengthscore': '11',
    'Strengthmod': '+0',
    'Dexterityscore': '17',
    'Dexteritymod': '+3',
    'Constitutionscore': '9',
    'Constitutionmod': '-1',
    'Wisdomscore': '10',
    'Wisdommod': '0',
    'Intelligencescore': '8',
    'Intelligencemod': '-1',
    'Charismascore': '13',
    'Charismamod': '+1',
    'Passive': '10',
    'StrengthSave': '0',
    'DexteritySave': '5',
    'ConstitutionSave': '-1',
    'WisdomSave': '0',
    'IntelligenceSave': '1',
    'CharismaSave': '1',
    'AC': '14',
    'Initiative': '+3',
    'Speed': '30',
    'MaxHP': '7',
    'TotalHD': '1d8',
    'PersonalityTraits ': 'Always Calm',
    'Ideals': 'Freedom',
    'Bonds': 'Guilty',
    'HD': ' ',
    'Flaws': 'Innocent',
    'Acrobatics': '5',
    'Animal': '0',
    'Arcana': '-1',
    'Athletics': '2',
    'Deception': '5',
    'History': '-1',
    'Insight': '0',
    'Intimidation': '1',
    'Investigation': '1',
    'Medicine': '0',
    'Nature': '-1',
    'Perception': '2',
    'Performance': '1',
    'Persuasion': '3',
    'Religion': '-1',
    'SleightOfHand': '5',
    'Stealth': '7',
    'Survival': '0',
    'Wpn Name': 'Short Swd',
    'Wpn1 AtkBonus': '5',
    'Wpn1 Damage': '1d6+3',
    'Wpn Name 2': 'Dagger',
    'Wpn2 AtkBonus ': '5',
    'Wpn Name 3': ' ',
    'Wpn3 AtkBonus  ': ' ',
    'Wpn2 Damage ': '1d4+3',
    'CurrentHP': ' ',
    'HPTemp': ' ',
    'Wpn3 Damage ': ' ',
    'AttacksSpellcasting': ' ',
    'CP': ' ',
    'ProficienciesLang': 'Common, Elvish, TBD. Light Amor, Theifs Tools, Playing Cards',
    'SP': ' ',
    'EP': ' ',
    'GP': ' ',
    'PP': ' ',
    'Equipment': ' ',
    'Features and Traits': 'Dark Vision, Fey Ansestery',
}

for key, value in data_dict.items():
    search_str = "placeholder=\"" + str(key) + "\""
    replace_str = "placeholder=\"" + str(value) + "\""
    if html.find(search_str) != -1:
        print("Replacing " + key + " with value " + str(value))
        html = html.replace(search_str,replace_str)
    else:
        print("False")

output.write(html)
output.close()