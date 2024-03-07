while True:
    try:
        leeftijd = int(input('Wat is je leeftijd? '))
    except ValueError:
        print('je moet wel een nummer invullen')
    