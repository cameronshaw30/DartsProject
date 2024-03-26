def game_mode():

    game_style = input('501 or 301? ')

    while game_style != '501' and game_style != '301':
        print('501 and 301 are the only valid options')
        print("-" * 25)
        game_style = input('501 or 301? ')
    else:
        if game_style == '501':
            print('You are playing 501')
            print("-"*25)
        elif game_style == '301':
            print('You are playing 301')
            print("-" * 25)

    return game_style
