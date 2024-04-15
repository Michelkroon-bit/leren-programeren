lijst = ['codewars', 'flick', 'code', 'wars']


def always_true_with_flick(lijst):
    omgekeerd = True
    result = []
    for item in lijst:
        if item == 'flick':
            omgekeerd = False
        result.append(not omgekeerd)
        if omgekeerd:
            omgekeerd = True
    return result

# Example usage:
lijst = ['codewars', 'flick', 'code', 'wars']
print(always_true_with_flick(lijst))  
