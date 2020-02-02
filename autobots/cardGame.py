import requests
import time

cards_api_url = 'https://deckofcardsapi.com/api/deck/'

# https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=2

class CardGame:

    def __init__(self):
        self.cardsResponse = requests.get(cards_api_url + 'new/shuffle/?deck_count=1').json()
        self.deck_id = self.cardsResponse.get('deck_id')
        self.first_player_score = 0
        self.second_player_score = 0

    def new_game(self):
        self.get_names()

    def checkScore(self):
        if(self.first_player_score >= 10):
            print(self.first_player + ' Won the Game\nScrew you ' + self.second_player)
        elif(self.second_player_score >= 10):
            print(self.second_player + ' Won the Game\nScrew you ' + self.first_player)
        else:
            self.draw_card_prompt()


    def get_names(self):
        self.first_player = input('Enter first players name... \n')
        self.second_player = input('Enter second players name... \n')
        self.draw_card_prompt()

    def draw_card_prompt(self):
        cont = input('Ready to draw card?\n[y/n]\n')
        if(cont == 'y'):
            self.draw_card()
        else:
            self.draw_card_prompt()

    def draw_card(self):
        url_to_hit = 'https://deckofcardsapi.com/api/deck/' + self.deck_id + '/draw/?count=1'

        firstCard = requests.get(url_to_hit).json()['cards']
        secondCard = requests.get(url_to_hit).json()['cards']
        self.first_player_card = firstCard[0].get('value')
        self.second_player_card = secondCard[0].get('value')
        print(self.first_player + ' drew the ' + firstCard[0].get('value') + ' of ' + firstCard[0].get('suit'))
        print(self.second_player + ' drew the ' + secondCard[0].get('value') + ' of ' + secondCard[0].get('suit'))

        self.rank_cards()

    def rank_cards(self):
        # time.sleep(2)
        if(self.first_player_card == self.second_player_card):
            print('DRAW: no player won this round...\n')
            self.draw_card_prompt()
        elif(self.first_player_card == 'ACE'):
            self.first_player_score += 1
            print(self.first_player + ' won this round')
        elif(self.second_player_card == 'ACE'):
            self.second_player_score += 1
            print(self.second_player + ' won this round')
        elif(self.first_player_card == 'KING'):
            self.first_player_score += 1
            print(self.first_player + ' won this round')
        elif(self.second_player_card == 'KING'):
            self.second_player_score += 1
            print(self.second_player + ' won this round')
        elif(self.first_player_card == 'QUEEN'):
            self.first_player_score += 1
            print(self.first_player + ' won this round')
        elif(self.second_player_card == 'QUEEN'):
            self.second_player_score += 1
            print(self.second_player + ' won this round')
        elif(self.first_player_card == 'JACK'):
            self.first_player_score += 1
            print(self.first_player + ' won this round')
        elif(self.second_player_card == 'JACK'):
            self.second_player_score += 1
            print(self.second_player + ' won this round')
        elif(int(self.first_player_card) > int(self.second_player_card)):
            self.first_player_score += 1
            print(self.first_player + ' won this round')
        elif (int(self.second_player_card) > int(self.first_player_card)):
            self.second_player_score += 1
            print(self.second_player + ' won this round')
        print(self.first_player + ' score: ' + str(self.first_player_score) + '\n' + self.second_player + ' score: ' + str(self.second_player_score))

        self.checkScore()





cardGame = CardGame()
cardGame.new_game()