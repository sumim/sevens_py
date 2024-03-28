import random

SUITS = ['S', 'H', 'D', 'C']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']

def initialize_deck():
    return [(suit, rank) for suit in SUITS for rank in RANKS]

def initialize_players(player_name):
    if player_name:
        return [player_name, 'Computer1', 'Computer2']
    else:
        return ['Computer1', 'Computer2', 'Computer3']

def deal_cards(deck, players):
    random.shuffle(deck)
    hands = {player: sorted(deck[i::len(players)], key=lambda x: (SUITS.index(x[0]), RANKS.index(x[1]))) for i, player in enumerate(players)}
    
    field = [(suit, '7') for suit in SUITS]
    for player, hand in hands.items():
        for card in hand.copy():
            if card[1] == '7':
                hand.remove(card)
                if card[0] == 'D':
                    starting_player = player
    
    return hands, field, starting_player

def display_field(field):
    for suit in SUITS:
        field_suit = ['_' if (suit, rank) not in field else rank for rank in RANKS]
        print(f"{suit}: {' '.join(field_suit)}")
    print()

def display_hand(hand):
    hand_by_suit = {suit: [] for suit in SUITS}
    for card in hand:
        suit, rank = card
        hand_by_suit[suit].append(rank)
    
    hand_str = ' '.join([f"{suit}-{','.join(hand_by_suit[suit])}" for suit in SUITS if hand_by_suit[suit]])
    if hand_str == '':
        hand_str = "None"
    return hand_str

def get_valid_moves(hand, field):
    valid_moves = []
    for suit in SUITS:
        sorted_field_rank_indices = sorted([RANKS.index(rank) for s, rank in field if s == suit])
        rank_index_seqs = []
        rank_index_seq = []
        for i in range(len(sorted_field_rank_indices)):
            rank_index = sorted_field_rank_indices[i]
            if not rank_index_seq or rank_index - rank_index_seq[-1] == 1:
                rank_index_seq.append(rank_index)
            else:
                if len(rank_index_seq) > 1 or rank_index_seq[0] == 6:
                    rank_index_seqs.append(rank_index_seq)
                rank_index_seq = [rank_index]
        if len(rank_index_seq) > 1 or rank_index_seq[0] == 6:
            rank_index_seqs.append(rank_index_seq)

        valid_move_indices = []
        for rank_index_seq in rank_index_seqs:
            adjacent_rank_index = rank_index_seq[0] - 1
            if adjacent_rank_index >= 0 and adjacent_rank_index not in valid_move_indices:
                valid_move_indices.append(adjacent_rank_index)
            adjacent_rank_index = rank_index_seq[-1] + 1
            if adjacent_rank_index < 13 and adjacent_rank_index not in valid_move_indices:
                valid_move_indices.append(adjacent_rank_index)

        for valid_move_index in valid_move_indices:
            card = (suit, RANKS[valid_move_index])
            if card in hand:
                valid_moves.append(card)

    return valid_moves

def play_game():
    player_name = input("Player Name? ")
    players = initialize_players(player_name)
    deck = initialize_deck()
    hands, field, starting_player = deal_cards(deck, players)
    passes = {player: 0 for player in players}

    display_field(field)

    current_player_index = players.index(starting_player)
    while True:
        player = players[current_player_index]
        valid_moves = get_valid_moves(hands[player], field)
        valid_moves_str = ', '.join([f"{suit}-{rank}" for suit, rank in valid_moves])

        if valid_moves:
            if player == player_name:
                print(f"{player}'s hand:", display_hand(hands[player]))
                while True:
                    move = input(f"Enter a card to play ({valid_moves_str}) or press Enter to pass ({3-passes[player]} rest): ")
                    move = move.upper()
                    if move == '':
                        print(f"{player}: pass")
                        passes[player] += 1
                        break
                    else:
                        card = tuple([move[0], move[-1]])
                    if card in valid_moves:
                        print(f"{player}'s choice: {'-'.join(card)}")
                        hands[player].remove(card)
                        field.append(card)
                        display_field(field)
                        break
                    else:
                        print("Invalid move. Please try again.")
            else:
                card = random.choice(valid_moves)
                # print(f"{player}'s valid moves: {valid_moves_str}")
                print(f"{player}'s choice: {'-'.join(card)}")
                hands[player].remove(card)
                field.append(card)
                display_field(field)
        else:
            print(f"{player}: pass")
            passes[player] += 1
            if passes[player] > 3:
                print(f"{player} is out of the game.")
                field.extend(hands[player])
                display_field(field)
                del hands[player]
                players.remove(player)
            else:
                print()

        if (player in players and not hands[player]) or len(players) == 1:
            if len(players) == 1: player = players[0]
            print(f"{player} wins!")
            print("Final hands:")
            for p in players:
                if p in hands:
                    print(f"{p}: {display_hand(hands[p])}")
            return

        current_player_index = (current_player_index + 1) % len(players)

play_game()
