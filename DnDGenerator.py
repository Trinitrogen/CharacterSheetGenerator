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

check_dict = {
    'StrengthSaveCheck': [15, 3],
    'DexteritySaveCheck': [16, 3],
    'ConstitutionSaveCheck': [17, 3],
    'IntelligenceSaveCheck': [18, 3],
    'WisdomSaveCheck': [19, 3],
    'CharismaSaveCheck': [20, 3],
    'AcrobaticsCheck': [13, 7],
    'AnimalCheck': [14, 7],
    'ArcanaCheck': [15, 7],
    'AthleticsCheck': [16, 7],
    'DeceptionCheck': [17, 7],
    'HistoryCheck': [18, 7],
    'InsightCheck': [19, 7],
    'IntimidationCheck': [20, 7],
    'InvestigationCheck': [21, 7],
    'MedicineCheck': [22, 7],
    'NatureCheck': [23, 7],
    'PerceptionCheck': [24, 7],
    'PerformanceCheck': [25, 7],
    'PersuasionCheck': [26, 7],
    'ReligionCheck': [27, 7],
    'SleightOfHandCheck': [28, 7],
    'StealthCheck': [29, 7],
    'SurvivalCheck': [30, 7],
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
    input_html = CheckBoxes(input_html, sheet_list)
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


def CheckBoxes(html, sheet_list):
    '''Flips Checkboxes to check state if character has proficiency'''
    for key, value in check_dict.items():
        row = check_dict.get(key, 0)[0]
        column = check_dict.get(key, 0)[1]
        if sheet_list[row][column] == 'Yes':
            search_str = "placeholder=\"" + str(key) + "\""
            replace_str = "checked=\"checked\""
            html = html.replace(search_str, replace_str)
    return html


if __name__ == '__main__':
    output = open('output.html', 'w')

    output.write(GenerateHTML())
    output.close()
