stat_dict = {
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
    'WeaponName1': 'Short Swd',
    'WeaponBonus1': '5',
    'WeaponDamage1': '1d6+3',
    'WeaponName2': 'Dagger',
    'WeaponBonus2': '5',
    'WeaponDamage2': '1d4+3',
    'WeaponName3': ' ',
    'WeaponBonus3': ' ',
    'WeaponDamage3': ' ',
    'Wpn Name 2': 'Dagger',
    'Wpn2 AtkBonus ': '5',
    'Wpn Name 3': ' ',
    'Wpn3 AtkBonus  ': ' ',
    'Wpn2 Damage ': ' ',
    'CurrentHP': ' ',
    'HPTemp': ' ',
    'Wpn3 Damage ': ' ',
    'AttacksSpellcasting': ' ',
    'CP': ' ',
    'Proficiencies': 'Common, Elvish, TBD. Light Amour, Thiefs Tools, Playing Cards',
    'SP': ' ',
    'EP': ' ',
    'GP': ' ',
    'PP': ' ',
    'Equipment': ' ',
    'Features and Traits': 'Dark Vision, Fey Ansestery',
}


check_dict = {
    'StrengthSaveCheck': '0',
    'DexteritySaveCheck': '1',
    'ConstitutionSaveCheck': '0',
    'WisdomSaveCheck': '0',
    'IntelligenceSaveCheck': '1',
    'CharismaSaveCheck': '0',
    'AcrobaticsCheck': '1',
    'AnimalCheck': '0',
    'ArcanaCheck': '0',
    'AthleticsCheck': '0',
    'DeceptionCheck': '1',
    'HistoryCheck': '0',
    'InsightCheck': '0',
    'IntimidationCheck': '0',
    'InvestigationCheck': '0',
    'MedicineCheck': '0',
    'NatureCheck': '0',
    'PerceptionCheck': '1',
    'PerformanceCheck': '0',
    'PersuasionCheck': '1',
    'ReligionCheck': '0',
    'SleightOfHandCheck': '1',
    'StealthCheck': '1',
    'SurvivalCheck': '0',
}


def InputStats(html):
    for key, value in stat_dict.items():
        search_str = "placeholder=\"" + str(key) + "\""
        replace_str = "placeholder=\"" + str(value) + "\""
        html = html.replace(search_str, replace_str)
    return html


def CheckBoxes(html):
    for key, value in check_dict.items():
        search_str = "placeholder=\"" + str(key) + "\""
        replace_str = "checked=\"checked\""
        if value == '1':
            print('Value of ' + key + ' is ' + str(value))
            html = html.replace(search_str, replace_str)
    return html


if __name__ == '__main__':
    input = open('input.html')
    input_html = input.read()
    output = open('output.html', 'w')
    input_html = InputStats(input_html)
    input_html = CheckBoxes(input_html)
    output.write(input_html)
    output.close()
