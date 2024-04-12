testarg_investors_test6 = [{
    'profitReturn' : 5,
    'adventuring' : True
},{
    'profitReturn' : 5,
    'adventuring' : False
},{
    'profitReturn' : 9,
    'adventuring' : False
},{
    'profitReturn' : 1,
    'adventuring' : False
}]



def getInterestingInvestors(investors:list) -> list:
    geintreseerde_investors = []
    for x in investors:
        if x['profitReturn'] <= 10:
            geintreseerde_investors.append(x)
    return geintreseerde_investors


def getAdventuringInvestors(investors:list) -> list:
    geintreseerde_investors = []
    for x in investors:
        if x['adventuring'] == True:
            geintreseerde_investors.append(x)
    return geintreseerde_investors



abc = getInterestingInvestors(testarg_investors_test6)
abcd = getAdventuringInvestors(testarg_investors_test6)
for x in abcd:
    print(x)