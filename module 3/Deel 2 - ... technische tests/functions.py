import time
from termcolor import colored
from data import PEOPLE_PER_HORSE , PEOPLE_PER_TENT ,JOURNEY_IN_DAYS , COST_FOOD_HUMAN_COPPER_PER_DAY , COST_FOOD_HORSE_COPPER_PER_DAY , CURRENCY_CONVERT_COPPER_SILVER , CURRENCY_CONVERT_PLATINUM_GOLD , CURRENCY_CONVERT_SILVER_GOLD, COST_TENT_GOLD_PER_WEEK , COST_HORSE_SILVER_PER_DAY
from data import friends
from math import ceil
##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / CURRENCY_CONVERT_COPPER_SILVER
    
    
def silver2gold(amount:int) -> float:
    return amount / CURRENCY_CONVERT_SILVER_GOLD

def copper2gold(gold:int) -> float:
    amound_silver = copper2silver(gold)
    amound_gold = silver2gold(amound_silver)
    return amound_gold
    
    
    
def platinum2gold(amount:int) -> float:
    return amount * CURRENCY_CONVERT_PLATINUM_GOLD


def getPersonCashInGold(personCash:dict) -> float:
    copper = personCash['copper']
    platinum = personCash['platinum']
    gold = personCash['gold']
    silver = personCash['silver']  
    return platinum2gold(platinum) + copper2gold(copper) + silver2gold(silver) + gold
    
    
        
##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    totale_kosten_paart = copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY)
    totale_kosten_persoon = copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY) 
    totaal = round(totale_kosten_paart * JOURNEY_IN_DAYS * horses + totale_kosten_persoon * JOURNEY_IN_DAYS * people , 2)
    return totaal

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    resultaten = []
    
    for x in list:
        try:
            if x[key] == value:
                resultaten.append(x)
        except:
            pass
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
    result =  people / PEOPLE_PER_HORSE
    result = ceil(result) 
    return result

def getNumberOfTentsNeeded(people:int) -> int:
    result = people / PEOPLE_PER_TENT
    result = ceil(result)
    return result

def getTotalRentalCost(horses:int, tents:int) -> float:
    uitkomst = getNumberOfHorsesNeeded(horses) / silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS
    return uitkomst
##################### O08 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

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