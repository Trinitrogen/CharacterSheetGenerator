from PIL import Image, ImageDraw, ImageFont


class Sheet:
    """Class to hold coordinates in Character Sheet"""
    def __init__(self):
        self.str_coords = (105, 390)
        self.dex_coords = (105, 540)
        self.con_coords = (105, 690)
        self.int_coords = (105, 838)
        self.wis_coords = (105, 987)
        self.cha_coords = (105, 1135)

        self.acro_coords = (237, 673)
        self.anim_coords = (237, self.acro_coords[1] + 29)
        self.arca_coords = (237, self.acro_coords[1] + (29 * 2))
        self.athl_coords = (237, self.acro_coords[1] + (29 * 3))
        self.dece_coords = (237, self.acro_coords[1] + (29 * 4))
        self.hist_coords = (237, self.acro_coords[1] + (29 * 5))
        self.insi_coords = (237, self.acro_coords[1] + (29 * 6))
        self.inti_coords = (237, self.acro_coords[1] + (29 * 7))
        self.inve_coords = (237, self.acro_coords[1] + (29 * 8))
        self.medi_coords = (237, self.acro_coords[1] + (29 * 9))
        self.natu_coords = (237, self.acro_coords[1] + (29 * 10))
        self.perc_coords = (237, self.acro_coords[1] + (29 * 11))
        self.perf_coords = (237, self.acro_coords[1] + (29 * 12))
        self.pers_coords = (237, self.acro_coords[1] + (29 * 13))
        self.reli_coords = (237, self.acro_coords[1] + (29 * 14))
        self.slei_coords = (237, self.acro_coords[1] + (29 * 15))
        self.stea_coords = (237, self.acro_coords[1] + (29 * 16))
        self.surv_coords = (237, self.acro_coords[1] + (29 * 17))


class Character:
    """Class to represent character attributes"""
    def __init__(self, stre, dext, cons, inte, wisd, char):
        self.stre = stre
        self.dext = dext
        self.cons = cons
        self.inte = inte
        self.wisd = wisd
        self.char = char


CharacterSheet = Sheet()
Gillian = Character(17,18,19,20,21,22)

im = Image.open('CharacterSheet.png')
drw = ImageDraw.Draw(im)
fnt = ImageFont.truetype('/Library/Fonts/Courier New.ttf', 25)
drw.text(CharacterSheet.str_coords, str(Gillian.stre), font=fnt, fill='black')
drw.text(CharacterSheet.dex_coords, str(Gillian.dext), font=fnt, fill='black')
drw.text(CharacterSheet.con_coords, str(Gillian.cons), font=fnt, fill='black')
drw.text(CharacterSheet.int_coords, str(Gillian.inte), font=fnt, fill='black')
drw.text(CharacterSheet.wis_coords, str(Gillian.wisd), font=fnt, fill='black')
drw.text(CharacterSheet.cha_coords, str(Gillian.char), font=fnt, fill='black')


fnt = ImageFont.truetype('/Library/Fonts/Courier New.ttf', 14)
drw.text(CharacterSheet.acro_coords, str(Gillian.char), font=fnt, fill='black')
drw.text(CharacterSheet.anim_coords, str(Gillian.char), font=fnt, fill='black')
drw.text(CharacterSheet.arca_coords, str(Gillian.char), font=fnt, fill='black')
drw.text(CharacterSheet.athl_coords, str(Gillian.char), font=fnt, fill='black')
drw.text(CharacterSheet.dece_coords, str(Gillian.char), font=fnt, fill='black')
drw.text(CharacterSheet.hist_coords, str(Gillian.char), font=fnt, fill='black')
drw.text(CharacterSheet.inti_coords, str(Gillian.char), font=fnt, fill='black')
drw.text(CharacterSheet.insi_coords, str(Gillian.char), font=fnt, fill='black')
drw.text(CharacterSheet.inve_coords, str(Gillian.char), font=fnt, fill='black')
drw.text(CharacterSheet.medi_coords, str(Gillian.char), font=fnt, fill='black')
drw.text(CharacterSheet.natu_coords, str(Gillian.char), font=fnt, fill='black')
drw.text(CharacterSheet.perc_coords, str(Gillian.char), font=fnt, fill='black')




im.save('Output.png')