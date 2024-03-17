testarg_investors_test1_2_4 = [{
    'profitReturn' : 5,
    'adventuring' : True
}]
testarg_gearList_test1_8 = [{
    'amount' : 3,
    'price' : {
        'amount' : 1,
        'type' : 'gold'
    }
}]


def getInterestingInvestors(investors:list) -> list:
    for x in investors:
        if x['adventuring'] == True:
            profits = x['profitReturn']
            print(profits)
    return profits

getInterestingInvestors(testarg_gearList_test1_8)