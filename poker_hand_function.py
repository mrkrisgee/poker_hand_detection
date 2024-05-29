def findPokerHand(hand):
    rank_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    
    # Parse hand into ranks and suits
    ranks = [rank_map[card[:-1]] for card in hand]
    print(f"ranks {ranks}")
    suits = [card[-1] for card in hand]
    print(f"suits {suits}")

    sorted_ranks = sorted(ranks)
    rank_counts = {rank: ranks.count(rank) for rank in set(ranks)}
    
    is_flush = len(set(suits)) == 1
    is_straight = all(sorted_ranks[i] == sorted_ranks[i - 1] + 1 for i in range(1, len(sorted_ranks)))
    rank_count_values = sorted(rank_counts.values(), reverse=True)

    # Determine the hand rank
    if is_flush and sorted_ranks == [10, 11, 12, 13, 14]:
        hand_rank = "Royal Flush"
    elif is_flush and is_straight:
        hand_rank = "Straight Flush"
    elif rank_count_values == [4, 1]:
        hand_rank = "Four of a Kind"
    elif rank_count_values == [3, 2]:
        hand_rank = "Full House"
    elif is_flush:
        hand_rank = "Flush"
    elif is_straight:
        hand_rank = "Straight"
    elif rank_count_values == [3, 1, 1]:
        hand_rank = "Three of a Kind"
    elif rank_count_values == [2, 2, 1]:
        hand_rank = "Two Pair"
    elif rank_count_values == [2, 1, 1, 1]:
        hand_rank = "Pair"
    else:
        hand_rank = "High Card"
    
    print(hand, hand_rank)
    return hand_rank

if __name__ == "__main__":
    findPokerHand(["AH", "KH", "QH", "JH", "10H"]) # Royal Flush
    findPokerHand(["QC", "JC", "10C", "9C", "8C"]) # Straight Flush
    findPokerHand(["5C", "5S", "5H", "5D", "QH"]) # Four of a Kind
    findPokerHand(["2H", "2D", "5H", "10D", "10C"]) # Full House
    findPokerHand(["2D", "KD", "7D", "6D", "5D"]) # Flush   
    findPokerHand(["JC", "10H", "9C", "8C", "7D"]) # Straight 
    findPokerHand(["10H", "10C", "10D", "2D", "5S"]) # Three of a Kind
    findPokerHand(["KD", "KH", "5C", "5S", "6D"]) # Two pair
    findPokerHand(["2D", "2S", "9C", "KD", "10C"]) # Pair
    findPokerHand(["KD", "5H", "2D", "10C", "JH"]) # High Card
