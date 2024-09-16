import tkinter as tk
from tkinter import ttk
import math
class Component:
    def __init__(self, scrap, hqm, metal, cloth):
        self.scrap = scrap
        self.hqm = hqm
        self.metal = metal
        self.cloth = cloth
sheetMetal = Component(8,1,100,0)
roadSign = Component(5,1,0,0)
metalSpring = Component(10,1,0,0)
metalPipe = Component(5,1,0,0)
metalBlade = Component(2,0,15,0)
propaneTank = Component(1,0,50,0)
metalGear = Component(10,0,13,0)
semiBody = Component(15,2,75,0)
smgBody = Component(15,2,0,0)
rifleBody = Component(25,2,0,0)
techTrash = Component(20,1,0,0)
camEra = Component(40,4,0,0)
lapTop = Component(60,4,50,0)
sewingKit = Component(0,0,0,50)
rope = Component(0,0,0,15)
tarp = Component(0,0,0,50)
def multiAllResources(a,b):
    return(a*b)
def testtest(a):
    return(a)
def addAllResources(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o):
    return(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o)
def createMessageSafeZone(a,b,c,d):
    return("If you recycled your components inside a safe zone you would recieve: " + str(a) + " Scrap, " + str(b) + " HQM, " + str(c) + " Metal Frags, and " + str(d) + " Cloth.")
def createMessageNoSafeZone(a,b,c,d):
    return("If you recycled outside a safe zone you would recieve: " + str(a) + " Scrap, " + str(b) + " HQM, " + str(c) + " Metal Frags, and " + str(d) + " Cloth.")
def totalConvertInSafeZone():
    sheetMetalScrapCount = multiAllResources(sheetMetal.scrap,sheetMetalCount.get())
    sheetMetalHqmCount = multiAllResources(sheetMetal.hqm,sheetMetalCount.get())
    sheetMetalMetalCount = multiAllResources(sheetMetal.metal,sheetMetalCount.get())
    sheetMetalClothCount = multiAllResources(sheetMetal.cloth,sheetMetalCount.get())
    
    roadSignScrapCount = multiAllResources(roadSign.scrap,roadSignCount.get())
    roadSignHqmCount = multiAllResources(roadSign.hqm,roadSignCount.get())
    roadSignMetalCount = multiAllResources(roadSign.metal,roadSignCount.get())
    roadSignClothCount = multiAllResources(roadSign.cloth,roadSignCount.get())
    
    metalSpringScrapCount = multiAllResources(metalSpring.scrap,metalSpringCount.get())
    metalSpringHqmCount = multiAllResources(metalSpring.hqm,metalSpringCount.get())
    metalSpringMetalCount = multiAllResources(metalSpring.metal,metalSpringCount.get())
    metalSpringClothCount = multiAllResources(metalSpring.cloth,metalSpringCount.get())
    
    metalPipeScrapCount = multiAllResources(metalPipe.scrap,metalPipeCount.get())
    metalPipeHqmCount = multiAllResources(metalPipe.hqm,metalPipeCount.get())
    metalPipeMetalCount = multiAllResources(metalPipe.metal,metalPipeCount.get())
    metalPipeClothCount = multiAllResources(metalPipe.cloth,metalPipeCount.get())
    
    metalBladeScrapCount = multiAllResources(metalBlade.scrap,metalBladeCount.get())
    metalBladeHqmCount = multiAllResources(metalBlade.hqm,metalBladeCount.get())
    metalBladeMetalCount = multiAllResources(metalBlade.metal,metalBladeCount.get())
    metalBladeClothCount = multiAllResources(metalBlade.cloth,metalBladeCount.get())
    
    propaneTankScrapCount = multiAllResources(propaneTank.scrap,propaneTankCount.get())
    propaneTankHqmCount = multiAllResources(propaneTank.hqm,propaneTankCount.get())
    propaneTankMetalCount = multiAllResources(propaneTank.metal,propaneTankCount.get())
    propaneTankClothCount = multiAllResources(propaneTank.cloth,propaneTankCount.get())
    
    metalGearScrapCount = multiAllResources(metalGear.scrap,metalGearCount.get())
    metalGearHqmCount = multiAllResources(metalGear.hqm,metalGearCount.get())
    metalGearMetalCount = multiAllResources(metalGear.metal,metalGearCount.get())
    metalGearClothCount = multiAllResources(metalGear.cloth,metalGearCount.get())

    semiBodyScrapCount = multiAllResources(semiBody.scrap,semiBodyCount.get())
    semiBodyHqmCount = multiAllResources(semiBody.hqm,semiBodyCount.get())
    semiBodyMetalCount = multiAllResources(semiBody.metal,semiBodyCount.get())
    semiBodyClothCount = multiAllResources(semiBody.cloth,semiBodyCount.get())

    smgBodyScrapCount = multiAllResources(smgBody.scrap,smgBodyCount.get())
    smgBodyHqmCount = multiAllResources(smgBody.hqm,smgBodyCount.get())
    smgBodyMetalCount = multiAllResources(smgBody.metal,smgBodyCount.get())
    smgBodyClothCount = multiAllResources(smgBody.cloth,smgBodyCount.get())

    rifleBodyScrapCount = multiAllResources(rifleBody.scrap,rifleBodyCount.get())
    rifleBodyHqmCount = multiAllResources(rifleBody.hqm,rifleBodyCount.get())
    rifleBodyMetalCount = multiAllResources(rifleBody.metal,rifleBodyCount.get())
    rifleBodyClothCount = multiAllResources(rifleBody.cloth,rifleBodyCount.get())

    techTrashScrapCount = multiAllResources(techTrash.scrap,techTrashCount.get())
    techTrashHqmCount = multiAllResources(techTrash.hqm,techTrashCount.get())
    techTrashMetalCount = multiAllResources(techTrash.metal,techTrashCount.get())
    techTrashClothCount = multiAllResources(techTrash.cloth,techTrashCount.get())
    
    camEraScrapCount = multiAllResources(camEra.scrap,camEraCount.get())
    camEraHqmCount = multiAllResources(camEra.hqm,camEraCount.get())
    camEraMetalCount = multiAllResources(camEra.metal,camEraCount.get())
    camEraClothCount = multiAllResources(camEra.cloth,camEraCount.get())
    
    lapTopScrapCount = multiAllResources(lapTop.scrap,lapTopCount.get())
    lapTopHqmCount = multiAllResources(lapTop.hqm,lapTopCount.get())
    lapTopMetalCount = multiAllResources(lapTop.metal,lapTopCount.get())
    lapTopClothCount = multiAllResources(lapTop.cloth,lapTopCount.get())

    sewingKitScrapCount = multiAllResources(sewingKit.scrap,sewingKitCount.get())
    sewingKitHqmCount = multiAllResources(sewingKit.hqm,sewingKitCount.get())
    sewingKitMetalCount = multiAllResources(sewingKit.metal,sewingKitCount.get())
    sewingKitClothCount = multiAllResources(sewingKit.cloth,sewingKitCount.get())

    ropeScrapCount = multiAllResources(rope.scrap,ropeCount.get())
    ropeHqmCount = multiAllResources(rope.hqm,ropeCount.get())
    ropeMetalCount = multiAllResources(rope.metal,ropeCount.get())
    ropeClothCount = multiAllResources(rope.cloth,ropeCount.get())


    totalPreSafeZoneScrap = round(
        multiAllResources(
            addAllResources(sheetMetalScrapCount,
                            roadSignScrapCount,
                            metalSpringScrapCount,
                            metalPipeScrapCount,
                            metalBladeScrapCount,
                            propaneTankScrapCount,
                            metalGearScrapCount,
                            semiBodyScrapCount,
                            smgBodyScrapCount,
                            rifleBodyScrapCount,
                            techTrashScrapCount,
                            camEraScrapCount,
                            lapTopScrapCount,
                            sewingKitScrapCount,
                            ropeScrapCount
                            ), 0.8))
    totalPreSafeZoneHqm = round(
        multiAllResources(
            addAllResources(sheetMetalHqmCount,
                            roadSignHqmCount,
                            metalSpringHqmCount,
                            metalPipeHqmCount,
                            metalBladeHqmCount,
                            propaneTankHqmCount,
                            metalGearHqmCount,
                            semiBodyHqmCount,
                            smgBodyHqmCount,
                            rifleBodyHqmCount,
                            techTrashHqmCount,
                            camEraHqmCount,
                            lapTopHqmCount,
                            sewingKitHqmCount,
                            ropeHqmCount
                            ), 0.8))
    totalPreSafeZoneMetal = round(
        multiAllResources(
            addAllResources(sheetMetalMetalCount,
                            roadSignMetalCount,
                            metalSpringMetalCount,
                            metalPipeMetalCount,
                            metalBladeMetalCount,
                            propaneTankMetalCount,
                            metalGearMetalCount,
                            semiBodyMetalCount,
                            smgBodyMetalCount,
                            rifleBodyMetalCount,
                            techTrashMetalCount,
                            camEraMetalCount,
                            lapTopMetalCount,
                            sewingKitMetalCount,
                            ropeMetalCount
                            ), 0.8))
    totalPreSafeZoneCloth = round(
        multiAllResources(
            addAllResources(sheetMetalClothCount,
                            roadSignClothCount,
                            metalSpringClothCount,
                            metalPipeClothCount,
                            metalBladeClothCount,
                            propaneTankClothCount,
                            metalGearClothCount,
                            semiBodyClothCount,
                            smgBodyClothCount,
                            rifleBodyClothCount,
                            techTrashClothCount,
                            camEraClothCount,
                            lapTopClothCount,
                            sewingKitClothCount,
                            ropeClothCount), 0.8))
    
    
    totalPreSafeZoneMessage = createMessageSafeZone(totalPreSafeZoneScrap, totalPreSafeZoneHqm, totalPreSafeZoneMetal, totalPreSafeZoneCloth)
    
    
    output_string_safe.set(totalPreSafeZoneMessage)




def totalConvertNotInSafeZone():
    sheetMetalScrapCount = multiAllResources(sheetMetal.scrap,sheetMetalCount.get())
    sheetMetalHqmCount = multiAllResources(sheetMetal.hqm,sheetMetalCount.get())
    sheetMetalMetalCount = multiAllResources(sheetMetal.metal,sheetMetalCount.get())
    sheetMetalClothCount = multiAllResources(sheetMetal.cloth,sheetMetalCount.get())
    
    roadSignScrapCount = multiAllResources(roadSign.scrap,roadSignCount.get())
    roadSignHqmCount = multiAllResources(roadSign.hqm,roadSignCount.get())
    roadSignMetalCount = multiAllResources(roadSign.metal,roadSignCount.get())
    roadSignClothCount = multiAllResources(roadSign.cloth,roadSignCount.get())
    
    metalSpringScrapCount = multiAllResources(metalSpring.scrap,metalSpringCount.get())
    metalSpringHqmCount = multiAllResources(metalSpring.hqm,metalSpringCount.get())
    metalSpringMetalCount = multiAllResources(metalSpring.metal,metalSpringCount.get())
    metalSpringClothCount = multiAllResources(metalSpring.cloth,metalSpringCount.get())
    
    metalPipeScrapCount = multiAllResources(metalPipe.scrap,metalPipeCount.get())
    metalPipeHqmCount = multiAllResources(metalPipe.hqm,metalPipeCount.get())
    metalPipeMetalCount = multiAllResources(metalPipe.metal,metalPipeCount.get())
    metalPipeClothCount = multiAllResources(metalPipe.cloth,metalPipeCount.get())
    
    metalBladeScrapCount = multiAllResources(metalBlade.scrap,metalBladeCount.get())
    metalBladeHqmCount = multiAllResources(metalBlade.hqm,metalBladeCount.get())
    metalBladeMetalCount = multiAllResources(metalBlade.metal,metalBladeCount.get())
    metalBladeClothCount = multiAllResources(metalBlade.cloth,metalBladeCount.get())
    
    propaneTankScrapCount = multiAllResources(propaneTank.scrap,propaneTankCount.get())
    propaneTankHqmCount = multiAllResources(propaneTank.hqm,propaneTankCount.get())
    propaneTankMetalCount = multiAllResources(propaneTank.metal,propaneTankCount.get())
    propaneTankClothCount = multiAllResources(propaneTank.cloth,propaneTankCount.get())
    
    metalGearScrapCount = multiAllResources(metalGear.scrap,metalGearCount.get())
    metalGearHqmCount = multiAllResources(metalGear.hqm,metalGearCount.get())
    metalGearMetalCount = multiAllResources(metalGear.metal,metalGearCount.get())
    metalGearClothCount = multiAllResources(metalGear.cloth,metalGearCount.get())

    semiBodyScrapCount = multiAllResources(semiBody.scrap,semiBodyCount.get())
    semiBodyHqmCount = multiAllResources(semiBody.hqm,semiBodyCount.get())
    semiBodyMetalCount = multiAllResources(semiBody.metal,semiBodyCount.get())
    semiBodyClothCount = multiAllResources(semiBody.cloth,semiBodyCount.get())

    smgBodyScrapCount = multiAllResources(smgBody.scrap,smgBodyCount.get())
    smgBodyHqmCount = multiAllResources(smgBody.hqm,smgBodyCount.get())
    smgBodyMetalCount = multiAllResources(smgBody.metal,smgBodyCount.get())
    smgBodyClothCount = multiAllResources(smgBody.cloth,smgBodyCount.get())

    rifleBodyScrapCount = multiAllResources(rifleBody.scrap,rifleBodyCount.get())
    rifleBodyHqmCount = multiAllResources(rifleBody.hqm,rifleBodyCount.get())
    rifleBodyMetalCount = multiAllResources(rifleBody.metal,rifleBodyCount.get())
    rifleBodyClothCount = multiAllResources(rifleBody.cloth,rifleBodyCount.get())

    techTrashScrapCount = multiAllResources(techTrash.scrap,techTrashCount.get())
    techTrashHqmCount = multiAllResources(techTrash.hqm,techTrashCount.get())
    techTrashMetalCount = multiAllResources(techTrash.metal,techTrashCount.get())
    techTrashClothCount = multiAllResources(techTrash.cloth,techTrashCount.get())
    
    camEraScrapCount = multiAllResources(camEra.scrap,camEraCount.get())
    camEraHqmCount = multiAllResources(camEra.hqm,camEraCount.get())
    camEraMetalCount = multiAllResources(camEra.metal,camEraCount.get())
    camEraClothCount = multiAllResources(camEra.cloth,camEraCount.get())
    
    lapTopScrapCount = multiAllResources(lapTop.scrap,lapTopCount.get())
    lapTopHqmCount = multiAllResources(lapTop.hqm,lapTopCount.get())
    lapTopMetalCount = multiAllResources(lapTop.metal,lapTopCount.get())
    lapTopClothCount = multiAllResources(lapTop.cloth,lapTopCount.get())

    sewingKitScrapCount = multiAllResources(sewingKit.scrap,sewingKitCount.get())
    sewingKitHqmCount = multiAllResources(sewingKit.hqm,sewingKitCount.get())
    sewingKitMetalCount = multiAllResources(sewingKit.metal,sewingKitCount.get())
    sewingKitClothCount = multiAllResources(sewingKit.cloth,sewingKitCount.get())

    ropeScrapCount = multiAllResources(rope.scrap,ropeCount.get())
    ropeHqmCount = multiAllResources(rope.hqm,ropeCount.get())
    ropeMetalCount = multiAllResources(rope.metal,ropeCount.get())
    ropeClothCount = multiAllResources(rope.cloth,ropeCount.get())


    totalPreSafeZoneScrap = round(
        multiAllResources(
            addAllResources(sheetMetalScrapCount,
                            roadSignScrapCount,
                            metalSpringScrapCount,
                            metalPipeScrapCount,
                            metalBladeScrapCount,
                            propaneTankScrapCount,
                            metalGearScrapCount,
                            semiBodyScrapCount,
                            smgBodyScrapCount,
                            rifleBodyScrapCount,
                            techTrashScrapCount,
                            camEraScrapCount,
                            lapTopScrapCount,
                            sewingKitScrapCount,
                            ropeScrapCount
                            ), 1.2))
    totalPreSafeZoneHqm = round(
        multiAllResources(
            addAllResources(sheetMetalHqmCount,
                            roadSignHqmCount,
                            metalSpringHqmCount,
                            metalPipeHqmCount,
                            metalBladeHqmCount,
                            propaneTankHqmCount,
                            metalGearHqmCount,
                            semiBodyHqmCount,
                            smgBodyHqmCount,
                            rifleBodyHqmCount,
                            techTrashHqmCount,
                            camEraHqmCount,
                            lapTopHqmCount,
                            sewingKitHqmCount,
                            ropeHqmCount
                            ), 1.2))
    totalPreSafeZoneMetal = round(
        multiAllResources(
            addAllResources(sheetMetalMetalCount,
                            roadSignMetalCount,
                            metalSpringMetalCount,
                            metalPipeMetalCount,
                            metalBladeMetalCount,
                            propaneTankMetalCount,
                            metalGearMetalCount,
                            semiBodyMetalCount,
                            smgBodyMetalCount,
                            rifleBodyMetalCount,
                            techTrashMetalCount,
                            camEraMetalCount,
                            lapTopMetalCount,
                            sewingKitMetalCount,
                            ropeMetalCount
                            ), 1.2))
    totalPreSafeZoneCloth = round(
        multiAllResources(
            addAllResources(sheetMetalClothCount,
                            roadSignClothCount,
                            metalSpringClothCount,
                            metalPipeClothCount,
                            metalBladeClothCount,
                            propaneTankClothCount,
                            metalGearClothCount,
                            semiBodyClothCount,
                            smgBodyClothCount,
                            rifleBodyClothCount,
                            techTrashClothCount,
                            camEraClothCount,
                            lapTopClothCount,
                            sewingKitClothCount,
                            ropeClothCount), 1.2))
    
    
    totalNonSafeZoneMessage = createMessageNoSafeZone(totalPreSafeZoneScrap, totalPreSafeZoneHqm, totalPreSafeZoneMetal, totalPreSafeZoneCloth)
    
    
    output_string_not_safe.set(totalNonSafeZoneMessage)


# window
window = tk.Tk()
window.title = ('Recycler Calculator')
window.geometry('1500x900')

# title
title_label = ttk.Label(master = window, text = 'Recycler Calculator', font = 'calibri 30 bold')
title_label.pack(pady=7)
instruction_label = ttk.Label(master = window, text = 'Please input the amount of each component you plan to recycle below:', font = 'calibri 15')
instruction_label.pack(pady=7)
# input field

sheetMetalinputframe = ttk.Frame(master= window)
sheetMetalTitle = ttk.Label(master = sheetMetalinputframe, text = 'Sheet Metal:', font = 'calibri 10')
sheetMetalCount = tk.IntVar()
sheetMetalEntry = ttk.Entry(master = sheetMetalinputframe, textvariable = sheetMetalCount)
sheetMetalTitle.pack(side = 'left', pady = 3)
sheetMetalEntry.pack(side = 'left', padx = 10)
sheetMetalinputframe.pack(pady = 7)

roadSigninputframe = ttk.Frame(master= window)
roadSignTitle = ttk.Label(master = roadSigninputframe, text = 'Road Sign:', font = 'calibri 10')
roadSignCount = tk.IntVar()
roadSignEntry = ttk.Entry(master = roadSigninputframe, textvariable = roadSignCount)
roadSignTitle.pack(side = 'left', pady = 3)
roadSignEntry.pack(side = 'left', padx = 10)
roadSigninputframe.pack(pady = 7)

metalSpringinputframe = ttk.Frame(master= window)
metalSpringTitle = ttk.Label(master = metalSpringinputframe, text = 'Metal Spring:', font = 'calibri 10')
metalSpringCount = tk.IntVar()
metalSpringEntry = ttk.Entry(master = metalSpringinputframe, textvariable = metalSpringCount)
metalSpringTitle.pack(side = 'left', pady = 3)
metalSpringEntry.pack(side = 'left', padx = 10)
metalSpringinputframe.pack(pady = 7)

metalPipeinputframe = ttk.Frame(master= window)
metalPipeTitle = ttk.Label(master = metalPipeinputframe, text = 'Metal Pipe:', font = 'calibri 10')
metalPipeCount = tk.IntVar()
metalPipeEntry = ttk.Entry(master = metalPipeinputframe, textvariable = metalPipeCount)
metalPipeTitle.pack(side = 'left', pady = 3)
metalPipeEntry.pack(side = 'left', padx = 10)
metalPipeinputframe.pack(pady = 7)

metalBladeinputframe = ttk.Frame(master= window)
metalBladeTitle = ttk.Label(master = metalBladeinputframe, text = 'Metal Blade:', font = 'calibri 10')
metalBladeCount = tk.IntVar()
metalBladeEntry = ttk.Entry(master = metalBladeinputframe, textvariable = metalBladeCount)
metalBladeTitle.pack(side = 'left', pady = 3)
metalBladeEntry.pack(side = 'left', padx = 10)
metalBladeinputframe.pack(pady = 7)

propaneTankinputframe = ttk.Frame(master= window)
propaneTankTitle = ttk.Label(master = propaneTankinputframe, text = 'Propane Tank:', font = 'calibri 10')
propaneTankCount = tk.IntVar()
propaneTankEntry = ttk.Entry(master = propaneTankinputframe, textvariable = propaneTankCount)
propaneTankTitle.pack(side = 'left', pady = 3)
propaneTankEntry.pack(side = 'left', padx = 10)
propaneTankinputframe.pack(pady = 7)

metalGearinputframe = ttk.Frame(master= window)
metalGearTitle = ttk.Label(master = metalGearinputframe, text = 'Metal Gear:', font = 'calibri 10')
metalGearCount = tk.IntVar()
metalGearEntry = ttk.Entry(master = metalGearinputframe, textvariable = metalGearCount)
metalGearTitle.pack(side = 'left', pady = 3)
metalGearEntry.pack(side = 'left', padx = 10)
metalGearinputframe.pack(pady = 7)

semiBodyinputframe = ttk.Frame(master= window)
semiBodyTitle = ttk.Label(master = semiBodyinputframe, text = 'Semi Body:', font = 'calibri 10')
semiBodyCount = tk.IntVar()
semiBodyEntry = ttk.Entry(master = semiBodyinputframe, textvariable = semiBodyCount)
semiBodyTitle.pack(side = 'left', pady = 3)
semiBodyEntry.pack(side = 'left', padx = 10)
semiBodyinputframe.pack(pady = 7)

smgBodyinputframe = ttk.Frame(master= window)
smgBodyTitle = ttk.Label(master = smgBodyinputframe, text = 'SMG Body:', font = 'calibri 10')
smgBodyCount = tk.IntVar()
smgBodyEntry = ttk.Entry(master = smgBodyinputframe, textvariable = smgBodyCount)
smgBodyTitle.pack(side = 'left', pady = 3)
smgBodyEntry.pack(side = 'left', padx = 10)
smgBodyinputframe.pack(pady = 7)

rifleBodyinputframe = ttk.Frame(master= window)
rifleBodyTitle = ttk.Label(master = rifleBodyinputframe, text = 'Rifle Body:', font = 'calibri 10')
rifleBodyCount = tk.IntVar()
rifleBodyEntry = ttk.Entry(master = rifleBodyinputframe, textvariable = rifleBodyCount)
rifleBodyTitle.pack(side = 'left', pady = 3)
rifleBodyEntry.pack(side = 'left', padx = 10)
rifleBodyinputframe.pack(pady = 7)

techTrashinputframe = ttk.Frame(master= window)
techTrashTitle = ttk.Label(master = techTrashinputframe, text = 'Tech Trash:', font = 'calibri 10')
techTrashCount = tk.IntVar()
techTrashEntry = ttk.Entry(master = techTrashinputframe, textvariable = techTrashCount)
techTrashTitle.pack(side = 'left', pady = 3)
techTrashEntry.pack(side = 'left', padx = 10)
techTrashinputframe.pack(pady = 7)

camErainputframe = ttk.Frame(master= window)
camEraTitle = ttk.Label(master = camErainputframe, text = 'Camera:', font = 'calibri 10')
camEraCount = tk.IntVar()
camEraEntry = ttk.Entry(master = camErainputframe, textvariable = camEraCount)
camEraTitle.pack(side = 'left', pady = 3)
camEraEntry.pack(side = 'left', padx = 10)
camErainputframe.pack(pady = 7)

lapTopinputframe = ttk.Frame(master= window)
lapTopTitle = ttk.Label(master = lapTopinputframe, text = 'Laptop:', font = 'calibri 10')
lapTopCount = tk.IntVar()
lapTopEntry = ttk.Entry(master = lapTopinputframe, textvariable = lapTopCount)
lapTopTitle.pack(side = 'left', pady = 3)
lapTopEntry.pack(side = 'left', padx = 10)
lapTopinputframe.pack(pady = 7)

sewingKitinputframe = ttk.Frame(master= window)
sewingKitTitle = ttk.Label(master = sewingKitinputframe, text = 'Sewing Kit:', font = 'calibri 10')
sewingKitCount = tk.IntVar()
sewingKitEntry = ttk.Entry(master = sewingKitinputframe, textvariable = sewingKitCount)
sewingKitTitle.pack(side = 'left', pady = 3)
sewingKitEntry.pack(side = 'left', padx = 10)
sewingKitinputframe.pack(pady = 7)

ropeinputframe = ttk.Frame(master= window)
ropeTitle = ttk.Label(master = ropeinputframe, text = 'Rope:', font = 'calibri 10')
ropeCount = tk.IntVar()
ropeEntry = ttk.Entry(master = ropeinputframe, textvariable = ropeCount)
ropeTitle.pack(side = 'left', pady = 3)
ropeEntry.pack(side = 'left', padx = 7)
ropeinputframe.pack(pady = 7)





finalCalcButtonInSafeZone = ttk.Button(master=window, text = 'Inside Safe Zone:', command = totalConvertInSafeZone)
finalCalcButtonInSafeZone.pack(pady = 10)

output_string_safe = tk.StringVar()
output_label_safe = ttk.Label(master=window, text = 'total', textvariable = output_string_safe, font = 'calibri 15')
output_label_safe.pack(pady = 10)

finalCalcButtonNotInSafeZone = ttk.Button(master=window, text = 'Outside Safe Zone:', command = totalConvertNotInSafeZone)
finalCalcButtonNotInSafeZone.pack(pady = 10)
# output


output_string_not_safe = tk.StringVar()
output_label_not_safe = ttk.Label(master=window, text = 'total', textvariable = output_string_not_safe, font = 'calibri 15')
output_label_not_safe.pack(pady = 10)
# run
window.mainloop()
print(sheetMetalEntry)