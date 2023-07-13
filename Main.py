import os
import pandas as pd
import random as r
import math
import numpy as np

#function to fill a list with random values from 1-6
def d6(x):
    rolls=[]
    for i in range(x):
        die=r.randint(1,6)
        rolls.append(die)  
    return rolls

#function to fill a list with random values from 1-3
def d3(x):
    rolls=[]
    for i in range(x):
        die=r.randint(1,3)
        rolls.append(die)
    return rolls

#function to fill a list with random values from 1-10
def d10(x):
    rolls=[]
    for i in range(x):
        die=r.randint(1,10)
        rolls.append(die)
    return rolls

def d100(x):
    rolls=[]
    for i in range(x):
        die=r.randint(1,100)
        rolls.append(die)  
    return rolls

def diceroll(x,a,b):
    rolls=[]
    for i in range(x):
        die=r.randint(a,b)
        rolls.append(die)  
    return rolls

def Gender():
    d2=r.randint(1,2)
    if d2 == 1:
        gender = 'Male'
    else:
        gender = 'Female'
    return gender

def RacialOrigin():
    TempRoll=d6(4)
    if (TempRoll[0] in (1,2)):
        Race='French (Frank)'
    if (TempRoll[0] in (3,4,5)):
        Race='Norman'
    if (TempRoll[0] == 6):
        if (TempRoll[1] ==1):
            Race='Anglo-Saxon'
        if (TempRoll[1] ==2):
            Race='Dutch'
        if (TempRoll[1] ==3):
            Race='Occitan'
        if (TempRoll[1] ==4):
            Race='German'
        if (TempRoll[1] in (5,6)):
            if (TempRoll[2] in (1,2)):
                if(TempRoll[3] in (1,2,3)):
                    Race='Danish'
                if(TempRoll[3] in (4,5,6)):
                    Race='Norwegian'
            if (TempRoll[2] in (3,4)):
                Race='Jewish'
            if (TempRoll[2] == 5):
                if(TempRoll[3] in (1,2)):
                    Race='Castille'
                if(TempRoll[3] in (3,4)):
                    Race='Catalonian'
                if(TempRoll[3] in (5,6)):
                    Race='Portuguese'
            if (TempRoll[2] == 6):
                Race='Itallian'
    return Race
    #print(TempRoll)
    
def Name(Race,Gender,ExpandedNames):
    RacialTypesList=[]
    for i in RacialTypes[0]:
        RacialTypesList.append(i)
    if Gender == 'Female' and Race == 'Anglo-Saxon':
        return 'Anglo-Saxon Female'
    n=len(ExpandedNames)
    NameMFList=[]
    SelectList=[]
    #print(Race,Gender)
    for i in range(n):
        if ExpandedNames[0][i] == Race:  
            break
    j=i+1
    #print(j)
    for i in range(j,n):
        if ExpandedNames[0][i] in RacialTypesList:
            break
        NameMFList.append(ExpandedNames[0][i])
    #print(NameMFList)
    m=len(NameMFList)
    for i1 in range(m):
        if NameMFList[i1] == Gender:
            for j1 in range(i1+1,m):
                if NameMFList[j1] == 'Female':
                    break
                SelectList.append(NameMFList[j1])
    #print(len(SelectList))
    #print(SelectList)
    
    Name = r.randint(0,(len(SelectList)-1))
    #print(SelectList[Name])
               
    return SelectList[Name]

def SocialClass():
    TempRoll = sum(d6(2))
    #print(TempRoll)
    if TempRoll == 2:
        Social = 'Outcast'
        Money.append(sum(d3(1)))
    if TempRoll in (3,4,5,6,7,8):
        Social = 'Peasant'
        Money.append(sum(diceroll(1,1,10)))
    if TempRoll in (9,10,11):
        Social = 'Townsman'
        Money.append(sum(d6(3)))
    if TempRoll == 12:
        Social = 'Lesser Nobility'
        Money.append(sum(d100(1)))
    return Social

def Characteristics(CharacteristicsList,Value = 0,Cristics = [None,None,None]):
    Value = 0
    TempRoll = diceroll(3,1,99)
    #TempRoll = [99,99,99]
    print('Characteristics roll is' , TempRoll)
    GeneratedCristics = []
    Values=[]
    ChosenCharacteristics=[]
    for i in TempRoll:
        if i == 99:            
            CharacteristicsRun = GetCharacteristic(CharacteristicsList, Value, 2, TempRoll,True)
            for j in range(2):
                GeneratedCristics.append(CharacteristicsRun[0][j])
                Values.append(CharacteristicsRun[1][j])
            print(GeneratedCristics)
        else:
            CharacteristicsRun = GetCharacteristic(CharacteristicsList, Value, 1, i, False)
            GeneratedCristics.append(CharacteristicsRun[0][0])
            Values.append(CharacteristicsRun[1][0])
            print(GeneratedCristics)
    Tempchar = GeneratedCristics
    #flawed as we're assuming that duplicates will appear next to eachother in the list
    #there are also some characteristics that cannot be entered concurrently
    #Additional flaw, when a 3 cost characteristic appears second in list, we only get one trait e.g cost 1 , na, na. Should reroll if it cant fit.
    for k in range(len(Tempchar)):
        #if Tempchar[k] == Tempchar[k+1]:
        #    GeneratedCristics.pop(k)
        #    Values.pop(k)
        
        Value += Values[k]
        if Value <= 3:
            ChosenCharacteristics.append(GeneratedCristics[k])
        else:
            ChosenCharacteristics.append(None)
            
    print('List of traits:',GeneratedCristics)
    print('List of values:',Values)
    print('List of chosen traits:',ChosenCharacteristics)
    return ChosenCharacteristics

def GetCharacteristic(CharacteristicsList, Value, NoCharacteristics, Roll,NewRoll):
    if NewRoll == True:
        TempRoll = diceroll(NoCharacteristics,1,98)
        print('99 Characteristic reroll is',TempRoll)
    else:
        TempRoll=[Roll]
    #TempRoll = [99,99,99]
    Cristics=[]
    Value=[]
    print('No Characteristics re-roll needed value is' ,TempRoll)
    for i in range(NoCharacteristics):
        for j in range(1,len(CharacteristicsList)):
            #print('Iteration number: ', j)
            #print(int(CharacteristicsList[0][j][0:2]),int(CharacteristicsList[0][j][3:5]))
            if TempRoll[i] in range(int(CharacteristicsList[0][j][0:2]),int(CharacteristicsList[0][j][3:5])+1):               
                Value .append( int(CharacteristicsList[2][j]))
                print('Value of trait is',Value)
                print('Check of roll value', TempRoll[i])
                Cristics.append(CharacteristicsList[1][j])
                print('List of traits:',CharacteristicsList[1][j])
                    
    return Cristics, Value

def AdjustAttributes():
    #Attributes = ['AS','MS','DS','KN','WP','END','PERS','PERC','SPD','AGL']
    Adjustments=[0,0,0,0,0,0,0,0,0,0]
    Selection = r.sample(range(0, 10), 6)
    TempRollAdd = d6(4)
    TempRollSubtract = d6(2)
    for i in range(len(Selection)):
        if i <= 3:
            Adjustments[Selection[i]] += TempRollAdd[i]
        if i > 3:
            Adjustments[Selection[i]] -= TempRollSubtract[i-4]
        
    return Adjustments

#Function to pick correct first career
def FirstCareer(Social,Gender):
    TempRoll = d100(1)
    print('First career roll' , (TempRoll[0]))
    if TempRoll[0] in range(96,101):
        TempRoll = d100(1)
        print('Random living roll' , (TempRoll[0]))
        for j in range(1,len(RandomLivingTable)):
            if TempRoll[0] in range(int(RandomLivingTable[0][j][0:2]),int(RandomLivingTable[0][j][3:6])+1):  
                return FirstCareerSelection(RandomLivingTable,Gender,j)
    for j in range(1,len(OutcastFirstCareer)):
        if TempRoll[0] in range(int(OutcastFirstCareer[0][j][0:2]),int(OutcastFirstCareer[0][j][3:6])+1):  
            print('Roll is in range' , int(OutcastFirstCareer[0][j][0:2]),int(OutcastFirstCareer[0][j][3:6]))
            if Social == 'Outcast':
                return FirstCareerSelection(OutcastFirstCareer,Gender,j)
                #query outcast first career
            elif Social == 'Peasant':
                return FirstCareerSelection(PeasantFirstCareer,Gender,j)
                #query peasant first career
            elif Social == 'Townsman':
                return FirstCareerSelection(TownsmanFirstCareer,Gender,j)
                #query Townsman first career
            elif Social == 'Lesser Nobility':
                return FirstCareerSelection(NobilityFirstCareer,Gender,j)
                #query lesser nobility first career
                
def FirstCareerSelection(Table,Gender,j):
    if Gender == 'Male':
        return Table[1][j]
    else:
        if Table[2][j] == 'NA':
            return Table[1][j]
        else:                       
            return Table[2][j]
        
#Return careername
#Return duration
#Return additions to stats
#
def CareerLoop(year,careername1):

    ExitYear = year + careername1.duration[1]
    
    #Attribute loop
    RelevantEntries = [a for a in Careers[careername1].attributes if a != '']
    for i in range(0,len(RelevantEntries)):
        print()
    
    
    return ExitYear

#Only works for single digit rolls
def TexttoRoll(Roll):
    if Roll[0] != 'D':
        NoRolls = Roll[0]
    else:
        NoRolls = 1
    NoRolls = int(NoRolls)
    if Roll[1:] == 'D6' or Roll[1:] == 'd6':
        return d6(NoRolls)
    elif Roll[1:] == 'D3' or Roll[1:] == 'd3':
        return d3(NoRolls)
    elif Roll[1:] == 'D10' or Roll[1:] == 'd10':
        return d10(NoRolls)
    elif Roll[1:] == 'D100' or Roll[1:] == 'd100':
        return d100(NoRolls)


    
def AttributesLoop(currentattr,careername1):
    #Attribute loop
    Roll=[]
    Characteristic=[]
    RelevantEntries = [a for a in Careers[careername1].attributes if a != '']
    print(RelevantEntries)
    for i in range(1,len(RelevantEntries)):
        print(i)
        Roll.append(sum(TexttoRoll(RelevantEntries[i].split()[0])))
        print(Roll)
        Characteristic.append(RelevantEntries[i].split()[1])
        print(Characteristic)
    for i in range(0,len(Roll)):
        currentattr[AttributesMap[Characteristic[i]]]+Roll[i]
    
    return Roll, Characteristic,currentattr


    
class career():
    def __init__(self,duration,attributes,abilities,resourcenumbers,resources,careerexitnumbers,careerexits,randomevent,description,standardequipment):
        self.duration = duration #integer
        self.attributes = attributes #list
        self.abilities = abilities #list
        self.resourcenumbers = resourcenumbers
        self.resources = resources #list
        self.careerexitnumbers = careerexitnumbers
        self.careerexits = careerexits #list
        self.randomevent = randomevent #string
        self.description = description #string
        self.standardequipment = standardequipment #list
        
#Function to adjust stats based on career from data
#Important to know what number
#Duration of service, attributes added, abilities added, resources added



#script = os.path.realpath(__file__)
#print("SCript path:", script)

directory = 'C:\\Users\\Chris\\OneDrive\\Projects\\Python\\Maelstrom Character Creator'
os.chdir(directory)
os.getcwd()

################################
Output = False
################################

filedirectory = 'C:\\Users\\Chris\\OneDrive\\Projects\\Python\\Maelstrom Character Creator\\Data Files'
ReadCSV={}
ReadXLSX={}
for file in os.listdir(filedirectory):
     filename = os.fsdecode(file)
     print(filename)
     if filename.endswith(".csv"): 
         ReadCSV[filename] = pd.read_csv(os.path.join(filedirectory, filename),header=None,keep_default_na=False)
         continue
     elif filename.endswith(".xlsx"):
         ReadXLSX[filename] = pd.read_excel(os.path.join(filedirectory, filename),header=None)
         continue
     else:
         continue
     
careersdirectory = 'C:\\Users\\Chris\\OneDrive\\Projects\\Python\\Maelstrom Character Creator\\Data Files\\Careers'
ReadCareers={}
Careers = {}
for file in os.listdir(careersdirectory):
     filename = os.fsdecode(file)
     print(filename)
     if filename.endswith(".xlsx"): 
         ReadCareers[filename[:-5]] = pd.read_excel(os.path.join(careersdirectory, filename),header=None,keep_default_na=False, sheet_name=None)
         continue
for careername in ReadCareers['CareerDetails']:  
    ref = ReadCareers['CareerDetails'][careername]
    Careers[careername] = career(ref[1], ref[2], ref[3], ref[4], ref[5], ref[6], ref[7], ref[8], ref[9], ref[10])
     
#Read in necessary files
CharacterTemplate = ReadXLSX['Maelstrom Character Creation.xlsx']
ExpandedNames = ReadCSV['Expanded Names.csv']
RacialTypes = ReadCSV['Racial Type.csv']
CharacteristicsList = ReadCSV['Characteristics.csv']
RandomLivingTable = ReadCSV['Random Living Table.csv']
OutcastFirstCareer = ReadCSV['Outcast First Career.csv']
PeasantFirstCareer = ReadCSV['Peasant First Career.csv']
TownsmanFirstCareer = ReadCSV['Townsman First Career.csv']
NobilityFirstCareer = ReadCSV['Nobility First Career.csv']

##FirstCareerTables = 

#Define variables 
AttributesMap = {
  "Attack Skill": 0,
  "Missile Skill": 1,
  "Defence Skill": 2,
  "Knowledge": 3,
  "Willpower": 4,
  "Endurance": 5,
  "Perspective": 6,
  "Perception": 7,
  "Speed": 8,
  "Agility": 9,
}
Attributes = ['AS','MS','DS','KN','WP','END','PERS','PERC','SPD','AGL']
AttributeValues = [40,40,40,40,40,40,40,40,40,40]
AttributeAdjust = AdjustAttributes()
AttributeValues = [a+b for a, b in zip(AttributeValues, AttributeAdjust)]
Money = []
CareerPath = np.full([6, 21], '----------------')


#Generate Characteristics
CharacteristicsRun = Characteristics(CharacteristicsList)
#SheetValues=[Name,Characteristic1,Characteristic2,Characteristic3,Race]
Characteristic1= CharacteristicsRun[0]
Characteristic2= CharacteristicsRun[1]
Characteristic3= CharacteristicsRun[2]
Race = RacialOrigin()
Social = SocialClass()
Supernatural=None
Patron=None
Age=13
Born=1073
Gender = Gender()
Name=Name(Race,Gender,ExpandedNames)
FirstCareer = FirstCareer(Social,Gender)

#Generating career
CareerPath[0][0] = FirstCareer
CareerPath[0][1] = Careers[FirstCareer].duration[1]
ClassAttributes = [a for a in dir(Careers[FirstCareer]) if not a.startswith('__')]
for i in range(0,10):
    print(i)
    CareerPath[0][i] = getattr(Careers[FirstCareer],ClassAttributes[i])[1]

#Assign characteristic to the sheet
CharacterTemplate.at[0,9] = Race
CharacterTemplate.at[1,9] = Social
CharacterTemplate.at[0,2] = Name
CharacterTemplate.at[2,15] = Gender
CharacterTemplate.at[3,1] = Characteristic1
CharacterTemplate.at[4,1] = Characteristic2
CharacterTemplate.at[5,1] = Characteristic3
CharacterTemplate.at[3,9] = Supernatural
CharacterTemplate.at[4,9] = Patron
CharacterTemplate.at[0,15] = Age
CharacterTemplate.at[1,15] = Born
CharacterTemplate.at[10,1] = CareerPath[0][0]
CharacterTemplate.at[11,1] = CareerPath[1][0]
CharacterTemplate.at[12,1] = CareerPath[2][0]
CharacterTemplate.at[13,1] = CareerPath[3][0]
CharacterTemplate.at[14,1] = CareerPath[4][0]
CharacterTemplate.at[15,1] = CareerPath[5][0]

#Output the sheet to folder
if (Output):
    CharacterTemplate.to_excel(r'C:\\Users\\Chris\\OneDrive\\Projects\\Maelstrom Character Creator\\Generated Character\\Character.xlsx', index = False)
