import random
from collections import Counter

LETTER_POOL = {
  'A': 9,
  'B': 2,
  'C': 2,
  'D': 4,
  'E': 12,
  'F': 2,
  'G': 3,
  'H': 2,
  'I': 9,
  'J': 1,
  'K': 1,
  'L': 4,
  'M': 2,
  'N': 6,
  'O': 8,
  'P': 2,
  'Q': 1,
  'R': 6,
  'S': 4,
  'T': 6,
  'U': 4,
  'V': 2,
  'W': 2,
  'X': 1,
  'Y': 2,
  'Z': 1
}

SCORE_CHART = {
  'A': 1,
  'B': 3,
  'C': 3,
  'D': 2,
  'E': 1,
  'F': 4,
  'G': 2,
  'H': 4,
  'I': 1,
  'J': 8,
  'K': 5,
  'L': 1,
  'M': 3,
  'N': 1,
  'O': 1,
  'P': 3,
  'Q': 10,
  'R': 1,
  'S': 1,
  'T': 1,
  'U': 1,
  'V': 4,
  'W': 4,
  'X': 8,
  'Y': 4,
  'Z': 10
}

LETTER_POOL_LIST = []
temp_list = []

def draw_letters():

    # Creates a comprehensive list which includes the total quanity of each available letter from the LETTER_POOL dictionary as individual elements.  
    for letter, quantity in LETTER_POOL.items():
        temp_list.append([letter] * quantity)
 
    for sublist in temp_list:
        for letter in sublist:
            LETTER_POOL_LIST.append(letter)

    # Chooses 10 random letters as hand, excluding the ones that are already chosen.
    #hand = random.sample(LETTER_POOL_LIST, 10)

    hand = []
    while len(hand) < 10:
        random_letter = random.choice(LETTER_POOL_LIST)
        random_letter_index = LETTER_POOL_LIST.index(random_letter)
        LETTER_POOL_LIST.pop(random_letter_index)
        hand.append(random_letter)

    return hand

draw_letters()
     
def uses_available_letters(word, letter_bank):       
    word_verification = []
    hand_letter_count = {}
    word_letter_count = {}
    count = 0
    capitalized_word = word.upper()

    for letter in letter_bank:
        if letter not in hand_letter_count:
            count = 1
            hand_letter_count[letter] = count
        else: 
            count += 1
            hand_letter_count[letter] = count
      
    for letter in capitalized_word:
        letter_quantity = capitalized_word.count(letter)
        word_letter_count[letter] = letter_quantity

        if letter in letter_bank and word_letter_count[letter] <= hand_letter_count[letter]:
            word_verification.append("True")
        else:
            word_verification.append("False")
      
    if "False" in word_verification:
        return False
    else:
        return True
      

def score_word(word):
    word_score = {}

    if word == "":
       word_score["empty"] = 0

    for letter in word.upper():
        if letter in SCORE_CHART:
            if letter not in word_score:
                word_score[letter] = SCORE_CHART[letter]
            else:
                word_score[letter] += SCORE_CHART[letter]

    if 7 <= len(word) <= 10:
        word_score["bonus"] = 8
      
    return sum(word_score.values())

def get_highest_word_score(word_list):
    score_dict = {}
    score_list = []
    matching_scores_dict = {}
    highest_score = 0

    for word in word_list:
        score = score_word(word)
        score_dict[word] = score

    for word, score in score_dict.items():
        score_list.append(score)
        if score > highest_score:
            highest_score = score
            winning_word = word
    
    matching_scores = [k for k,v in Counter(score_list).items() if v>1]

    for word, score in score_dict.items():
        if score in matching_scores:
            matching_scores_dict[word] = score

    for word, score in matching_scores_dict.items():
        if score == highest_score and len(word) == 10:
            highest_score = score
            winning_word = word
            break
        elif score == highest_score and len(word) < len(winning_word):
            highest_score = score
            winning_word = word
            break
        
    best_word = (winning_word, highest_score)
    return best_word