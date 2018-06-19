import os
import pdfrw

CharacterSheetPath = 'CharacterSheet.pdf'
OutputPath = 'Output.pdf'

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)


data_dict = {
    'ClassLevel': 'Rogue 1',
    'Background': 'Criminal',
    'PlayerName': ' ',
    'CharacterName': 'Gillian Moser',
    'Race ': 'Half-Elf',
    'Alignment': 'Chaotic Neutral',
    'XP': '90',
    'Inspiration': ' ',
    'STR': '11',
    'ProfBonus': '2',
    'AC': '14',
    'Initiative': '+3',
    'Speed': '30',
    'PersonalityTraits ': 'Always Calm',
    'STRmod': '+0',
    'ST Strength': '0',
    'DEX': '17',
    'Ideals': 'Freedom',
    'DEXmod ': '+3',
    'Bonds': 'Guilty',
    'CON': '9',
    'HDTotal': '1d8',
    'CONmod': '-1',
    'HD': ' ',
    'Flaws': 'Innocent',
    'INT': '8',
    'ST Dexterity': '5',
    'ST Constitution': '-1',
    'ST Intelligence': '1',
    'ST Wisdom': '0',
    'ST Charisma': '1',
    'Acrobatics': '5',
    'Animal': '0',
    'Athletics': '2',
    'Deception ': '5',
    'History ': '-1',
    'Wpn Name': 'Short Swd',
    'Wpn1 AtkBonus': '5',
    'Wpn1 Damage': '1d6+3',
    'Insight': '0',
    'Intimidation': '1',
    'Wpn Name 2': 'Dagger',
    'Wpn2 AtkBonus ': '5',
    'Wpn Name 3': ' ',
    'Wpn3 AtkBonus  ': ' ',
    'INTmod': '-1',
    'Wpn2 Damage ': '1d4+3',
    'Investigation ': '1',
    'WIS': '10',
    'Arcana': '-1',
    'Perception ': '2',
    'WISmod': '0',
    'CHA': '13',
    'Nature': '-1',
    'Performance': '1',
    'Medicine': '0',
    'Religion': '-1',
    'Stealth ': '7',
    'Persuasion': '3',
    'HPMax': '7',
    'HPCurrent': ' ',
    'HPTemp': ' ',
    'Wpn3 Damage ': ' ',
    'SleightofHand': '5',
    'CHamod': '1',
    'Survival': '0',
    'AttacksSpellcasting': ' ',
    'Passive': '10',
    'CP': ' ',
    'ProficienciesLang': 'Common, Elvish, TBD. Light Amor, Theifs Tools, Playing Cards',
    'SP': ' ',
    'EP': ' ',
    'GP': ' ',
    'PP': ' ',
    'Equipment': ' ',
    'Features and Traits': 'Dark Vision, Fey Ansestery',
}

'''
    'CharacterName': 'Gillian Moser',
    'ClassLevel': 'Rogue 1',
    'Race ': 'Half-Elf',
    'Alignment': 'Chaotic Neutral',
    'AC': '14',
    'Initiative': '3',
    'Speed': '30',
    'HPMax': '7',
    'HDTotal': '1',
    'HD': '1D6',
    'XP': '90',
    'STR': '17',
    'STRmod': '+1',
    'DEX': '18',
    'DEXmod ': '+1',
    'CON': '15',
    'CONmod': '+1',
    'INT': '10',
    'INTmod': '+1',
    'WIS': '9',
    'WISmod': '+1',
    'CHA': '8',
    'CHamod': '+1'
'''

if __name__ == '__main__':
    write_fillable_pdf(CharacterSheetPath, OutputPath, data_dict)
