import process_game

game_type = int(input('Введите 0, если хотите играть с другим игроком. Введите 1, если хотите играть с легким ботом. Введите 2, если хотите играть со сложным ботом \n'))
if game_type == 0:
    process_game.player_vs_player()
elif game_type == 1:
    process_game.player_vs_easy_bot()
elif game_type == 2:
    process_game.player_vs_hard_bot()
else:
    print('Введите число от 0 до 2')