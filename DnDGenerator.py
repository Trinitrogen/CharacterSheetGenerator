import gspread
from oauth2client.service_account import ServiceAccountCredentials

stat_dict = {
    'charname': [0, 0],
    'classlevel': [1, 0],
    'Background': [6, 0],
    'PlayerName': [7, 0],
    'race': [1, 2],
    'alignment': [6, 2],
    'experiencepoints': [7, 2],
    'inspiration': [5, 5],
    'proficiencybonus': [5, 6],
    'Strengthscore': [0, 9],
    'Strengthmod': [0, 10],
    'Dexterityscore': [0, 12],
    'Dexteritymod': [0, 13],
    'Constitutionscore': [0, 15],
    'Constitutionmod': [0, 15],
    'Wisdomscore': [0, 18],
    'Wisdommod': [0, 19],
    'Intelligencescore': [0, 21],
    'Intelligencemod': [0, 22],
    'Charismascore': [0, 24],
    'Charismamod': [0, 25],
    'Passive': [0, 29],
    'StrengthSave': [5, 8],
    'DexteritySave': [5, 9],
    'ConstitutionSave': [5, 10],
    'WisdomSave': [5, 11],
    'IntelligenceSave': [5, 12],
    'CharismaSave': [5, 13],
    'AC': [9, 6],
    'Initiative': [10, 6],
    'Speed': [11, 6],
    'MaxHP': [9, 9],
    'TotalHD': [9, 13],
    'Acrobatics': [5, 16],
    'Animal': [5, 17],
    'Arcana': [5, 18],
    'Athletics': [5, 19],
    'Deception': [5, 20],
    'History': [5, 21],
    'Insight': [5, 22],
    'Intimidation': [5, 23],
    'Investigation': [5, 24],
    'Medicine': [5, 25],
    'Nature': [5, 26],
    'Perception': [5, 27],
    'Performance': [5, 28],
    'Persuasion': [5, 29],
    'Religion': [5, 30],
    'SleightOfHand': [5, 31],
    'Stealth': [5, 32],
    'Survival': [5, 33],
    'WeaponName1': [9, 17],
    'WeaponBonus1': [10, 17],
    'WeaponDamage1': [11, 17],
    'WeaponName2': [9, 18],
    'WeaponBonus2': [10, 18],
    'WeaponDamage2': [11, 18],
    'WeaponName3': [9, 19],
    'WeaponBonus3': [10, 19],
    'WeaponDamage3': [11, 19],
    'CurrentHP': [9, 9],
    'HPTemp': [9, 11],
    'CP': [9, 25],
    'SP': [9, 26],
    'EP': [9, 27],
    'GP': [9, 28],
    'PP': [9, 29]
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
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("Character Sheet").sheet1
    sheet_list = sheet.get_all_values()
    input_html = InputStats(input_html, sheet_list)
    #input_html = CheckBoxes(input_html)
    return input_html


def InputStats(html, sheet_list):
    for key, value in stat_dict.items():
        search_str = "placeholder=\"" + str(key) + "\""
        y_coord = stat_dict.get(key,0)[0]
        x_coord = stat_dict.get(key,0)[1]
        replace_str = "placeholder=\"" + sheet_list[x_coord][y_coord] + "\""
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
