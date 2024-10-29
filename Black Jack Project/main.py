import random

from art import logo

def deal_card():
    """
    :return: a random card from the decK  
    """""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return  card


def calculate_score(cards):
    """

    :param cards:Take a list of  the cards  and return the score calculated from the cards
    :return:
    """
    # if 11 in cards and 10 in cards and len(cards)==2:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score,computer_score):

    if computer_score==user_score:
        return "Draw"
    elif computer_score==0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score==0:
        return "You win , You have a Blackjack 😱"
    elif user_score>21:
        return  "You went over. You lose 😭"
    elif computer_score>21:
        return  "Opponent went over. You win 😁"
    elif user_score>computer_score:
        return "You Win"
    else:
        return "Computer Wins!! you loose!!"


def play_game():
    print(logo)
    user_card=[]
    computer_card=[]
    user_score=-1
    computer_score=-1


    is_game_over=False
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append((deal_card()))

    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)

        print(f"Your cards: {user_card}, current score {user_score}")
        print(f"Computer's first card:{computer_card[0]}")


        if user_score==0 and computer_score==0 or user_score>21:
             is_game_over=True
        else:
            user_should_deal = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal=='y':
                user_card.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)


    print(f'Your final hand: {user_card}, final score: {user_score}')
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while  input(f"Do you want to play BlackJack? Type 'y' or 'n' ").lower()=="y":
    print("\n"*20)
    play_game()


# def black_jack_game():
#     print('\n' * 20)
#     print(logo)
#     user_list=list(random.choices(deal_card(), k=2))
#     computer_list=list(random.choices(cards,k=2))
#     game_continue=True
#
#     while game_continue:
#         print(f"Your cards: {user_list}, current score: {sum(user_list)}")
#         print(f"Computer's first card:{computer_list[0]}")
#
#         choice_continue=input(f"Type 'y' to get another card, type 'n' to pass: ").lower()
#         if choice_continue=='y':
#            user_list.append(random.choice(deal_card(),))
#            computer_list.append(random.choice(deal_card(),))
#
#            if sum(user_list)>21:
#                print(f'Your final hand: {user_list}, final score: {sum(user_list)}')
#                print(f"Computer's final hand: {computer_list}, final score: {sum(computer_list)}")
#                print("You went over. You lose 😭")
#                game_continue = False
#            elif sum(computer_list)==21:
#                print(f"Your final hand: {user_list}, final score: {sum(user_list)}")
#                print(f"Computer's final hand:{computer_list}, final score: 0")
#                print(f"Lose, opponent has Blackjack 😱")
#                game_continue = False
#         else:
#             computer_list.append(random.choice(cards))
#             if sum(computer_list)>21:
#                 print(f'Your final hand: {user_list}, final score: {sum(user_list)}')
#                 print(f"Computer's final hand: {computer_list}, final score: {sum(computer_list)}")
#                 print("Opponent went over. You win 😁")
#                 game_continue = False
#
#
#     choice = input(f"Do you want to play BlackJack? Type 'y' or 'n' ").lower()
#     if choice=='y':
#         black_jack_game()
#
#
# choice=input(f"Do you want to play BlackJack? Type 'y' or 'n' ").lower()

#
# if choice=='y':
#     print('\n'*20)
#     black_jack_game()
