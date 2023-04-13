from PIL import Image, ImageEnhance
import os

size_500 = (500, 500)
"""
image1 = Image.open('films/Blade_runner.png')

new_image = image1.resize(size_500)

#image brightness enhancer
#enhancer = ImageEnhance.Brightness(image1)

#factor = 0.8 #gives original image
#im_output = enhancer.enhance(factor)
#im_output.save('11.png')


new_image.save('12.png')
"""
new = Image.new("RGBA", (1500,1500))

"""
AnotherWorld = Image.open("1.png")
LongestJourney = Image.open("2.png")
MetalGear = Image.open("3.png")
SoulReaver = Image.open("4.png")
CallCthulhu = Image.open("5.png")
DeusEx = Image.open("6.png")
Fallout2 = Image.open("7.png")
FinalFantasy = Image.open("8.png")
QuestGlory = Image.open("9.png")
new.paste(AnotherWorld, (0,0))
new.paste(DeusEx, (500,0))
new.paste(QuestGlory, (1000,0))
new.paste(SoulReaver, (0,500))
new.paste(LongestJourney, (500,500))
new.paste(MetalGear, (1000,500))
new.paste(Fallout2, (0,1000))
new.paste(FinalFantasy, (500,1000))
new.paste(CallCthulhu, (1000,1000))
"""

Bicicle = Image.open("1.png")
BladeRunner = Image.open("12.png")
Ikiru = Image.open("3.png")
Lawrence = Image.open("4.png")
Metropolis = Image.open("5.png")
SeventhSeal = Image.open("11.png")
SoylentGreen = Image.open("7.png")
VideoDrome = Image.open("8.png")
ThirdMan = Image.open("9.png")
new.paste(Metropolis, (0,0))
new.paste(SeventhSeal, (500,0))
new.paste(Lawrence, (1000,0))
new.paste(ThirdMan, (0,500))
new.paste(BladeRunner, (500,500))
new.paste(Bicicle, (1000,500))
new.paste(VideoDrome, (0,1000))
new.paste(Ikiru, (500,1000))
new.paste(SoylentGreen, (1000,1000))

#new.show()
new.save("favorite_films.png")