import time
from termcolor import colored
from data import PEOPLE_PER_HORSE , PEOPLE_PER_TENT ,JOURNEY_IN_DAYS , COST_INN_HORSE_COPPER_PER_NIGHT , COST_INN_HUMAN_SILVER_PER_NIGHT , COST_FOOD_HUMAN_COPPER_PER_DAY , COST_FOOD_HORSE_COPPER_PER_DAY , CURRENCY_CONVERT_COPPER_SILVER , CURRENCY_CONVERT_PLATINUM_GOLD , CURRENCY_CONVERT_SILVER_GOLD, COST_TENT_GOLD_PER_WEEK , COST_HORSE_SILVER_PER_DAY 
from data import friends , adventurerGear
from math import ceil

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / CURRENCY_CONVERT_COPPER_SILVER
    
    
def silver2gold(amount:int) -> float:
    return amount / CURRENCY_CONVERT_SILVER_GOLD

def copper2gold(gold:int) -> float:
    return silver2gold(copper2silver(gold))
    
    
    
def platinum2gold(amount:int) -> float:
    return amount * CURRENCY_CONVERT_PLATINUM_GOLD


def getPersonCashInGold(personCash:dict) -> float:
    return platinum2gold(personCash['platinum']) + copper2gold(personCash['copper']) + \
        silver2gold(personCash['silver'] ) + personCash['gold']
    
    
        
##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    dag_kosten_paard = copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY)
    totale_kosten_persoon = copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY) 
    totaal = round(dag_kosten_paard * JOURNEY_IN_DAYS * horses + totale_kosten_persoon * JOURNEY_IN_DAYS * people , 2)
    return totaal

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    resultaten = []
    
    for x in list:
        if key in x and x[key] == value:
            resultaten.append(x)
    return resultaten
        
def getAdventuringPeople(people:list) -> list:
    result = getFromListByKeyIs(people , 'adventuring' , True)
    
    return result

def getShareWithFriends(friends:list) -> list:
    result = getFromListByKeyIs(friends , 'shareWith' , True)
    
    return result

def getAdventuringFriends(friends:list) -> list:
    result = getFromListByKeyIs('adventuring' ,'shareWith', getAdventuringPeople(friends ))
    return result

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return ceil(people / PEOPLE_PER_HORSE)

def getNumberOfTentsNeeded(people:int) -> int:
    return ceil(people / PEOPLE_PER_TENT)

def getTotalRentalCost(horses:int, tents:int) -> float:
    kosten_tent = ceil(JOURNEY_IN_DAYS / 7) * COST_TENT_GOLD_PER_WEEK * tents
    kosten_paart = silver2gold(JOURNEY_IN_DAYS* COST_HORSE_SILVER_PER_DAY) * horses
    
    uitkomst = kosten_paart + kosten_tent
    return uitkomst

    

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    output_str = ''
    spullen = []
    for x in items: 
        zin = (f"{x['amount']}{x['unit']} {x['name']}")
        spullen.append(zin)
    counter = 0
    for x in spullen:
        if len(spullen) > 1:
            
            if counter == 0 :
                output_str += f'{x}'
            
            elif counter > 0 and counter != len(spullen) - 1:
                output_str += f', {x}' 
            else:
                output_str += f' & {x}' 
                
            counter +=1
        else:
            return x
    return output_str
    
    
    
def getItemsValueInGold(items:list) -> float:
    totale_uitkomst = 0.0
    index = 0
    for x in items:
        uitkomst_1 = x['amount'] * items[index]['price']['amount']
        
        if items[index]['price']['type'] == 'copper':
            totale_uitkomst += float(copper2gold(uitkomst_1))
            
        
        if items[index]['price']['type'] == 'silver':
            totale_uitkomst += float(silver2gold(uitkomst_1))
            
        
        if items[index]['price']['type'] == 'platinum':
            totale_uitkomst += float(platinum2gold(uitkomst_1))
            
        
        if items[index]['price']['type'] == 'gold':
            totale_uitkomst += uitkomst_1 #float(x['amount'] * items[0]['price']['amount'])
        index +=1  
    return totale_uitkomst

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    totale_uitkomst = 0.0
    index = 0
    for x in people:
        copper = x['cash']['copper']
        silver = x['cash']['silver']
        gold = x['cash']['gold']
        platinum = x['cash']['platinum']
        totale_uitkomst += copper2gold(copper) + silver2gold(silver) + gold + platinum2gold(platinum)
        index +=1  
    return round(totale_uitkomst , 2)
        # return platinum2gold(single_person.get('platinum')) + copper2gold( single_person.get('copper')) + \
        #     silver2gold(single_person.get('silver')) + single_person.get('gold')

##################### O10 #####################


def getInterestingInvestors(investors:list) -> list:
    geintreseerde_investors = []
    for x in investors:
        if x['profitReturn'] <= 10:
            geintreseerde_investors.append(x)
    return geintreseerde_investors


def getAdventuringInvestors(investors:list) -> list:
    adventuring_investors = []
    for x in investors:
        if x['adventuring'] == True:
            adventuring_investors.append(x)
    return adventuring_investors


def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    uitkomst = 0.0
    abc = getInterestingInvestors(investors)
    abcd = getAdventuringInvestors(abc)
    for x in abcd:
        index = 0
        #berekening #1
        koste_eten_paart = copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY) * JOURNEY_IN_DAYS
        koste_paart = silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS
        koste_tent = ceil(JOURNEY_IN_DAYS / 7) * COST_TENT_GOLD_PER_WEEK
        koste_eten = copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY) * JOURNEY_IN_DAYS
        uitkomst += koste_tent + koste_eten + koste_paart + koste_eten_paart
        
        #berekening 2 
        for y in gear:
            uitkomst_1 = y['amount'] * gear[index]['price']['amount']
            
            if gear[index]['price']['type'] == 'copper':
                uitkomst += float(copper2gold(uitkomst_1))
                
            
            if gear[index]['price']['type'] == 'silver':
                uitkomst += float(silver2gold(uitkomst_1))
                
            
            if gear[index]['price']['type'] == 'platinum':
                uitkomst += float(platinum2gold(uitkomst_1))
                
            
            if gear[index]['price']['type'] == 'gold':
                uitkomst += uitkomst_1 #float(x['amount'] * items[0]['price']['amount'])
            index +=1      
    return round(uitkomst , 2)

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    cost_horse_per_night = horses * COST_INN_HORSE_COPPER_PER_NIGHT
    copper2gold(cost_horse_per_night)
    cost_person_per_night= people * COST_INN_HUMAN_SILVER_PER_NIGHT
    silver2gold(cost_person_per_night)
    
    
    return float(cost_person_per_night + cost_horse_per_night) * nightsInInn

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()