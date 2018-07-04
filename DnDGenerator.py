import gspread
from oauth2client.service_account import ServiceAccountCredentials

stat_dict = {
    'charname': [1, 1],
    'classlevel': [1, 2],
    'Background': [1, 7],
    'PlayerName': [1, 8],
    'race': [3, 2],
    'alignment': [3, 7],
    'experiencepoints': [3, 8],
    'inspiration': [6, 6],
    'proficiencybonus': [7, 6],
    'Strengthscore': [10, 1],
    'Strengthmod': [11, 1],
    'Dexterityscore': [13, 1],
    'Dexteritymod': [14, 1],
    'Constitutionscore': [16, 1],
    'Constitutionmod': [16, 1],
    'Wisdomscore': [19, 1],
    'Wisdommod': [20, 1],
    'Intelligencescore': [22, 1],
    'Intelligencemod': [23, 1],
    'Charismascore': [25, 1],
    'Charismamod': [26, 1],
    'Passive': [30, 1],
    'StrengthSave': [9, 6],
    'DexteritySave': [10, 6],
    'ConstitutionSave': [11, 6],
    'WisdomSave': [12, 6],
    'IntelligenceSave': [13, 6],
    'CharismaSave': [14, 6],
    'AC': [7, 10],
    'Initiative': [7, 11],
    'Speed': [7, 12],
    'MaxHP': [10, 10],
    'TotalHD': [14, 10],
    'Acrobatics': [17, 6],
    'Animal': [18, 6],
    'Arcana': [19, 6],
    'Athletics': [20, 6],
    'Deception': [21, 6],
    'History': [22, 6],
    'Insight': [23, 6],
    'Intimidation': [24, 6],
    'Investigation': [25, 6],
    'Medicine': [26, 6],
    'Nature': [27, 6],
    'Perception': [28, 6],
    'Performance': [29, 6],
    'Persuasion': [30, 6],
    'Religion': [31, 6],
    'SleightOfHand': [32, 6],
    'Stealth': [33, 6],
    'Survival': [34, 6],
    'WeaponName1': [18, 10],
    'WeaponBonus1': [18, 11],
    'WeaponDamage1': [18, 12],
    'WeaponName2': [19, 10],
    'WeaponBonus2': [19, 11],
    'WeaponDamage2': [19, 12],
    'WeaponName3': [20, 10],
    'WeaponBonus3': [20, 11],
    'WeaponDamage3': [20, 12],
    'CurrentHP': [10, 10],
    'HPTemp': [12,10],
    'CP': [26, 10],
    'SP': [27, 10],
    'EP': [28, 10],
    'GP': [29, 10],
    'PP': [30, 10]
}
'''
UNCOMMENT THIS IF NOT USING GOOGLE SHEETS
stat_dict = {
    'charname': [1, 1],
    'classlevel': [2, 1],
    'Background': [7, 1],
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
'''

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

def GenerateHTML():
    input = open('input.html')
    input_html = input.read()
    input_html = InputStats(input_html)
    #input_html = CheckBoxes(input_html)
    return input_html


def InputStats(html):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("Character Sheet").sheet1
    for key, value in stat_dict.items():
        search_str = "placeholder=\"" + str(key) + "\""
        y_coord = stat_dict.get(key,0)[0]
        x_coord = stat_dict.get(key,0)[1]
        replace_str = "placeholder=\"" + sheet.cell(y_coord,x_coord).value + "\""
        html = html.replace(search_str, replace_str)
    return html


def CheckBoxes(html):
    for key, value in check_dict.items():
        search_str = "placeholder=\"" + str(key) + "\""
        replace_str = "checked=\"checked\""
        if value == '1':
            html = html.replace(search_str, replace_str)
    return html


if __name__ == '__main__':
    output = open('output.html', 'w')

    output.write(GenerateHTML())
    output.close()
