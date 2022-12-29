# import random
#
# def play():
#     user = input("'s' for snake and 'w' for water and 'g' for gun :\n")
#     computer = random.choice(['s', 'w', 'g'])
#     if user == computer:
#         return "It's about to Tie :\n"
#     if is_win(user , computer):
#         return "You won :"
#     return "you lose"
# def is_win(player, unplayer):
#     if (player == 's' and unplayer == 'w') or (player == 'w' and unplayer == 'g') or (player == 'g' and unplayer == 's'):
#         return True
#
# print(play())