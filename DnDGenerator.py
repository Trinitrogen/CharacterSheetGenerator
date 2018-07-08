import gspread
from oauth2client.service_account import ServiceAccountCredentials


stat_dict = {
    'charname': [0, 0],
    'classlevel': [0, 8],
    'Background': [0, 12],
    'PlayerName': [0, 16],
    'race': [0, 4],
    'alignment': [2, 12],
    'experiencepoints': [2, 16],
    'inspiration': [5, 6],
    'proficiencybonus': [8, 6],
    'Strengthscore': [6, 1],
    'Strengthmod': [6, 3],
    'Dexterityscore': [7, 1],
    'Dexteritymod': [7, 3],
    'Constitutionscore': [8, 1],
    'Constitutionmod': [8, 3],
    'Intelligencescore': [9, 1],
    'Intelligencemod': [9, 3],
    'Wisdomscore': [10, 1],
    'Wisdommod': [10, 3],
    'Charismascore': [11, 1],
    'Charismamod': [11, 3],
    'Passive': [22, 0],
    'StrengthSave': [15, 1],
    'DexteritySave': [16, 1],
    'ConstitutionSave': [17, 1],
    'IntelligenceSave': [18, 1],
    'WisdomSave': [19, 1],
    'CharismaSave': [20, 1],
    'AC': [5, 10],
    'Initiative': [5, 14],
    'Speed': [5, 18],
    'MaxHP': [8, 10],
    'TotalHD': [8, 18],
    'Acrobatics': [13, 8],
    'Animal': [14, 8],
    'Arcana': [15, 8],
    'Athletics': [16, 8],
    'Deception': [17, 8],
    'History': [18, 8],
    'Insight': [19, 8],
    'Intimidation': [20, 8],
    'Investigation': [21, 8],
    'Medicine': [22, 8],
    'Nature': [23, 8],
    'Perception': [24, 8],
    'Performance': [25, 8],
    'Persuasion': [26, 8],
    'Religion': [27, 8],
    'SleightOfHand': [28, 8],
    'Stealth': [29, 8],
    'Survival': [30, 8],
    'WeaponName1': [14 , 13],
    'WeaponBonus1': [14, 16],
    'WeaponDamage1': [14, 19],
    'WeaponName2': [15, 13],
    'WeaponBonus2': [15, 16],
    'WeaponDamage2': [15, 19],
    'WeaponName3': [16, 13],
    'WeaponBonus3': [16, 16],
    'WeaponDamage3': [16, 19],
    'CurrentHP': [8, 10],
    'HPTemp': [8, 14],
    'CP': [24, 14],
    'SP': [25, 14],
    'EP': [26, 14],
    'GP': [27, 14],
    'PP': [28, 14],
    'Proficiencies': [25, 0],
    'Equipment': [23, 17],
    'Personality': [5, 23],
    'Ideals': [12, 23],
    'Bonds': [19, 23],
    'Flaws': [26, 23],
    'Features': [33, 23],
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
    '''Entry function in which all functions are called to build output html'''
    input = open('input.html')
    input_html = input.read()
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("Character Sheet - Gillian").sheet1
    sheet_list = sheet.get_all_values()
    input_html = InputStats(input_html, sheet_list)
    return input_html


def InputStats(html, sheet_list):
    '''Pulls single cell data from Google Sheet and inputs into output html'''
    for key, value in stat_dict.items():
        search_str = "placeholder=\"" + str(key) + "\""
        row = stat_dict.get(key, 0)[0]
        column = stat_dict.get(key, 0)[1]
        replace_str = "placeholder=\"" + sheet_list[row][column] + "\""
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
