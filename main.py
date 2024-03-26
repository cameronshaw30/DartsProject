import functions

game_mode = input('1 Player or 2 Players? ')

while game_mode not in ['1', '2']:
    game_mode = input('1 Player or 2 Players? ')

if game_mode == '1':

    game_style = functions.game_mode()

    remaining_score = int(game_style)
    throws = []
    three_dart_avg = 0
    darts_total = 0
    darts_thrown = 0

    while remaining_score > 0:
        last_throw = input('What did you throw (3 dart score)? ')
        while not last_throw.isnumeric():
            print('Not a number, please enter a valid number')
            last_throw = input('What did you throw (3 dart score)? ')
        if int(last_throw) < 0 or int(last_throw) > 180:
            print('Invalid score')
        elif int(last_throw) > int(remaining_score) or int(last_throw) == (int(remaining_score) - 1):
            print('Bust')
            throws.append(0)
            temp_darts_thrown = input('How many darts did you throw? ')
            while temp_darts_thrown not in ['1', '2', '3']:
                print('Invalid amount')
                temp_darts_thrown = input('How many darts did you throw? ')
            darts_thrown += int(temp_darts_thrown)
            print(f'You have {remaining_score} remaining')
            print("-" * 25)
        else:
            remaining_score -= int(last_throw)
            throws.append(int(last_throw))
            if remaining_score == 0:
                temp_darts_thrown = input('How many darts did you throw? ')
                while temp_darts_thrown not in ['1', '2', '3']:
                    print('Invalid amount')
                    temp_darts_thrown = input('How many darts did you throw? ')
                darts_thrown += int(temp_darts_thrown)
                print("-" * 25)
            else:
                darts_thrown += 3
                print(f'You have {remaining_score} remaining')
                print("-" * 25)
    else:
        print("That's Game")
        print(f'Your throws were: {throws}')
        for score in throws:
            darts_total += score
            three_dart_avg = (darts_total / darts_thrown) * 3
        print(f'Darts Thrown: {darts_thrown}')
        print(f'3 Dart Average: {"{:.2f}".format(three_dart_avg)}')
        print(f'Highest 3 Dart Score: {max(throws)}')

else:
    game_style = functions.game_mode()

    p1_remaining_score = int(game_style)
    p1_throws = []
    p1_three_dart_avg = 0
    p1_darts_total = 0
    p1_darts_thrown = 0

    p2_remaining_score = int(game_style)
    p2_throws = []
    p2_three_dart_avg = 0
    p2_darts_total = 0
    p2_darts_thrown = 0

    while p1_remaining_score > 0 and p2_remaining_score > 0:
        p1_last_throw = input(f'P1 - What did you throw (3 dart score)? {p1_remaining_score} left ')
        while not p1_last_throw.isnumeric():
            print('Not a number, please enter a valid number')
            p1_last_throw = input('What did you throw (3 dart score)? ')
        while int(p1_last_throw) < 0 or int(p1_last_throw) > 180:
            print('Invalid score')
            p1_last_throw = input(f'P1 - What did you throw (3 dart score)? {p1_remaining_score} left ')
            while not p1_last_throw.isnumeric():
                p1_last_throw = input('What did you throw (3 dart score)? ')
        else:
            if int(p1_last_throw) > int(p1_remaining_score) or int(p1_last_throw) == (int(p1_remaining_score) - 1):
                print('Bust')
                p1_last_throw = 0
                p1_throws.append(p1_last_throw)
                p1_temp_darts_thrown = input('How many darts did you throw? ')
                while p1_temp_darts_thrown not in ['1', '2', '3']:
                    print('Invalid amount')
                    p1_temp_darts_thrown = input('How many darts did you throw? ')
                p1_darts_thrown += int(p1_temp_darts_thrown)
                print("-" * 25)
            else:
                p1_remaining_score -= int(p1_last_throw)
                p1_throws.append(int(p1_last_throw))
                if p1_remaining_score == 0:
                    p1_temp_darts_thrown = input('How many darts did you throw? ')
                    while p1_temp_darts_thrown not in ['1', '2', '3']:
                        print('Invalid amount')
                        p1_temp_darts_thrown = input('How many darts did you throw? ')
                    p1_darts_thrown += int(p1_temp_darts_thrown)
                    print("-" * 25)

                    print("That's Game")

                    print("Player 1 Wins!")

                    print("-" * 25)

                    print(f'Player 1"s throws were: {p1_throws}')
                    for score in p1_throws:
                        p1_darts_total += score
                        p1_three_dart_avg = (p1_darts_total / p1_darts_thrown) * 3
                    print(f'Darts Thrown: {p1_darts_thrown}')
                    print(f'3 Dart Average: {"{:.2f}".format(p1_three_dart_avg)}')
                    print(f'Highest 3 Dart Score: {max(p1_throws)}')

                    print("-" * 25)

                    print(f'Player 2"s throws were: {p2_throws}')
                    for score in p2_throws:
                        p2_darts_total += score
                        p2_three_dart_avg = (p2_darts_total / p2_darts_thrown) * 3
                    print(f'Darts Thrown: {p2_darts_thrown}')
                    print(f'3 Dart Average: {"{:.2f}".format(p2_three_dart_avg)}')
                    print(f'Highest 3 Dart Score: {max(p2_throws)}')
                    break
                else:
                    p1_darts_thrown += 3
                    print(f'P1 - You have {p1_remaining_score} remaining')
                    print("-" * 25)

        p2_last_throw = input(f'P2 - What did you throw (3 dart score)? {p2_remaining_score} left ')
        while not p2_last_throw.isnumeric():
            print('Not a number, please enter a valid number')
            p2_last_throw = input('What did you throw (3 dart score)? ')
        while int(p2_last_throw) < 0 or int(p2_last_throw) > 180:
            print('Invalid score')
            p2_last_throw = input(f'P2 - What did you throw (3 dart score)? {p2_remaining_score} left ')
            while not p2_last_throw.isnumeric():
                p2_last_throw = input('What did you throw (3 dart score)? ')
        else:
            if int(p2_last_throw) > int(p2_remaining_score) or int(p2_last_throw) == (int(p2_remaining_score) - 1):
                print('Bust')
                p2_last_throw = 0
                p2_throws.append(p2_last_throw)
                p2_temp_darts_thrown = input('How many darts did you throw? ')
                while p2_temp_darts_thrown not in ['1', '2', '3']:
                    print('Invalid amount')
                    p2_temp_darts_thrown = input('How many darts did you throw? ')
                p2_darts_thrown += int(p2_temp_darts_thrown)
                print("-" * 25)
            else:
                p2_remaining_score -= int(p2_last_throw)
                p2_throws.append(int(p2_last_throw))
                if p2_remaining_score == 0:
                    p2_temp_darts_thrown = input('How many darts did you throw? ')
                    while p2_temp_darts_thrown not in ['1', '2', '3']:
                        print('Invalid amount')
                        p2_temp_darts_thrown = input('How many darts did you throw? ')
                    p2_darts_thrown += int(p2_temp_darts_thrown)
                    print("-" * 25)

                    print("That's Game")

                    print("Player 2 Wins!")

                    print("-" * 25)

                    print(f'Player 1"s throws were: {p1_throws}')
                    for score in p1_throws:
                        p1_darts_total += score
                        p1_three_dart_avg = (p1_darts_total / p1_darts_thrown) * 3
                    print(f'Darts Thrown: {p1_darts_thrown}')
                    print(f'3 Dart Average: {"{:.2f}".format(p1_three_dart_avg)}')
                    print(f'Highest 3 Dart Score: {max(p1_throws)}')

                    print("-" * 25)

                    print(f'Player 2"s throws were: {p2_throws}')
                    for score in p2_throws:
                        p2_darts_total += score
                        p2_three_dart_avg = (p2_darts_total / p2_darts_thrown) * 3
                    print(f'Darts Thrown: {p2_darts_thrown}')
                    print(f'3 Dart Average: {"{:.2f}".format(p2_three_dart_avg)}')
                    print(f'Highest 3 Dart Score: {max(p2_throws)}')
                    break
                else:
                    p2_darts_thrown += 3
                    print(f'P2 - You have {p2_remaining_score} remaining')
                    print("-" * 25)

# TODO: CPU player with different scoring based on level
# TODO: Scores from real player's matches
