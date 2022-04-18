#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HW 3
"""

def is_onto (domain, co_domain, mapping):
    """" Determines if the function is onto.


       Arguments:
        - domain [list]: a list of values in the domain
        - co_domain [list]: a list of values in the co-domain
        - mapping [dict]: a dictionary of the function mapping between the domain and co-domain
        """

    values = []
    
    for key in mapping:
        values.append(mapping[key])
    
    uniqueValues = set(values)
    
    if uniqueValues == co_domain:
        return True
    
    else:
        return False

def is_one_to_one (domain, co_domain, mapping):
    """" Determines if the function is one-to-one.


       Arguments:
        - domain [list]: a list of values in the domain
        - co_domain [list]: a list of values in the co-domain
        - mapping [dict]: a dictionary of the function mapping between the domain and co-domain
        """

    values = []
    
    for key in mapping:
        if mapping[key] in values:
            return False
        values.append(mapping[key])
        
    return True


def is_bijective ( domain , co_domain , mapping ) :
    """" Determines if the function is bijective.


    Arguments:
     - domain [list]: a list of values in the domain
     - co_domain [list]: a list of values in the co-domain
     - mapping [dict]: a dictionary of the function mapping between the domain and co-domain
     """
    # WRITE YOUR CODE 
    onto_Bool = is_onto(domain, co_domain, mapping)
    one_to_one_Bool = is_one_to_one(domain, co_domain, mapping)
    
    meets_definition = onto_Bool and one_to_one_Bool
    return meets_definition #bool


def new_word(my_word, word_bank, used):
    """" Returns a tuple containing the old word and the new word that can be 
    formed from the old word and the remaining tiles in the pile. This tuple 
    must not be in used. Function updates the used list appropriately. If there
    is no unused tuple to return, return None.


       Arguments:
        - my_word [str]: the word to be added to
        - word_bank [list]: a list of valid words that can be considered
        - used [list]: a list of tuples that have already been made
        """
    len_list = len(word_bank)
    tup = tuple()
    for i in range(len_list):    
        cur_word = word_bank[i]
        word_len = len(cur_word)
        if (word_len == len(my_word) + 1):
            test_tup = (my_word, cur_word)
            if (test_tup not in used):
                tup = test_tup
    

    if (len(tup) > 0):
        used.append(tup)
        return tup #tuple or None
    else:
        return None



def generate_games_main(my_word, word_bank):
############################################################
###        CALL THIS FUNCTION TO SEE POSET OUTPUT        ### 
### THIS FUNCTION RETURNS A LIST OF TUPLES AS YOUR POSET ###
###             DO NOT EDIT THIS FUNCTION!!              ###
############################################################
    poset = []
    used = []
    generate_games(my_word, word_bank, used, poset) 
    return poset



def generate_games(my_word, word_bank, used, poset):
    """" Recursively generates a poset of the possible games.


       Arguments:
        - my_word [str]: the word to be added to
        - word_bank [list]: a list of valid words that can be considered
        - used [list]: a list of tuples that have already been made
        - poset [list]: a list of tuples representing the poset so far
        """
    new_tuple = new_word(my_word, word_bank, used);
    
    if (new_tuple==None):
        return
                
    else:
        created_word = new_tuple[1]
        poset.append(new_tuple)
        return generate_games(my_word, word_bank, used, poset), generate_games(created_word,word_bank,used,poset)

        
    # WRITE YOUR CODE HERE


def find_neighbors(poset, word):
    """" Finds the immediate predecessors and successors of a word


       Arguments:
        - word [str]: the word
        - poset [list]: a list of tuples representing the poset
        """
    # WRITE YOUR CODE HERE
    successors = []
    predecessors = []
    
    for i in poset:
        if word in i:
            if i[0] == word:
                successors.append(i[1])
            if i[1] == word:
                predecessors.append(i[0])
    return (predecessors, successors) #tuple of lists



######################################################################
### DO NOT TURN IN AN ASSIGNMENT WITH ANYTHING BELOW HERE MODIFIED ###
######################################################################
if __name__ == '__main__':
    print("#######################################")
    print("Welcome to Coding 3: Functions, Posets, and PHP!")
    print("#######################################")
    print()
    print("---------------------------------------")
    print("PART A: Function Properties")
    print("---------------------------------------")

    example_1 = [[1 ,2 ,3 ,4],[1,2,3,4,5,6,7],{1:2, 2:3, 3:1,4:3}] #not anything
    example_2 = [[1 ,2 ,3 ,4],[1,2,3,4,5,6,7],{1:2, 2:3, 3:1,4:5}] #one to one (nothing else)
    example_3 = [[1 ,2 ,3 ,4],[1,2,3],{1:2, 2:3, 3:1,4:3}] #onto (nothing else)
    example_4 = [[1 ,2 ,3 ,4],[1,2,3,4],{1:2, 2:3, 3:1,4:4}] #bijective
    
    print("---------------------------------------")
    print("\'is_onto\' Tests")
    print("---------------------------------------")
    is_onto_tests = [example_1, example_2, example_3, example_4]
    is_onto_answers = [False, False, True, True]
      
    for count, test in enumerate(is_onto_tests):
        if (is_onto(is_onto_tests[count][0],is_onto_tests[count][1],
                    is_onto_tests[count][2]) == is_onto_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_onto_answers[count]}')
        print(f'Your Answer: {is_onto(is_onto_tests[count][0],is_onto_tests[count][1],is_onto_tests[count][2])}')
        
    print("---------------------------------------")
    print("\'is_one_to_one\' Tests")
    print("---------------------------------------")
    is_one_to_one_tests = [example_1, example_2, example_3, example_4]
    is_one_to_one_answers = [False, True, False, True]
  
    for count, test in enumerate(is_one_to_one_tests):
        if (is_one_to_one(is_one_to_one_tests[count][0],is_one_to_one_tests[count][1],
                    is_one_to_one_tests[count][2]) == is_one_to_one_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_one_to_one_answers[count]}')
        print(f'Your Answer: {is_one_to_one(is_one_to_one_tests[count][0],is_one_to_one_tests[count][1],is_one_to_one_tests[count][2])}')
    
    print("---------------------------------------")
    print("\'is_bijective\' Tests")
    print("---------------------------------------")
    is_bijective_tests = [example_1, example_2, example_3, example_4]
    is_bijective_answers = [False, False, False, True]
  
    for count, test in enumerate(is_onto_tests):
        if (is_bijective(is_bijective_tests[count][0],is_bijective_tests[count][1],
                    is_bijective_tests[count][2]) == is_bijective_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_bijective_answers[count]}')
        print(f'Your Answer: {is_bijective(is_bijective_tests[count][0],is_bijective_tests[count][1],is_bijective_tests[count][2])}')
        
        
    print("---------------------------------------")
    print("PART B: Modeling with Posets")
    print("---------------------------------------")

    sample_word_bank_1 = ['a', 'at', 'cat', 'cats', 'scat', 'scats']
    gg_answers_1 = [('a', 'at'), ('at', 'cat'), ('cat', 'cats'), ('cats', 'scats'), ('cat', 'scat'), ('scat', 'scats')]
    fn_answers_1 = (['at'], ['cats', 'scat'])
    sample_word_bank_2 = ['a', 'ta', 'tav', 'tave', 'taver', 'tavern', 'taverns']
    gg_answers_2 = [('a', 'ta'), ('ta', 'tav'), ('tav', 'tave'), ('tave', 'taver'), ('taver', 'tavern'), ('tavern', 'taverns')]
    fn_answers_2 = (['taver'], ['taverns'])
    sample_word_bank_3 = ['a', 'ha', 'ah', 'hah', 'aha', 'haha', 'ahah', 'hahah']
    gg_answers_3 = [('a', 'ha'), ('ha', 'hah'), ('hah', 'haha'), ('haha', 'hahah'), 
                    ('hah', 'ahah'), ('ahah', 'hahah'), ('ha', 'aha'), ('aha', 'haha'), 
                    ('aha', 'ahah'), ('a', 'ah'), ('ah', 'hah'), ('ah', 'aha')]
    fn_answers_3 = (['ha', 'ah'], ['haha', 'ahah'])

    print("---------------------------------------")
    print("\'generate_games\' Tests")
    print("---------------------------------------")
    gg_tests = [("a", sample_word_bank_1), ("a", sample_word_bank_2), ("a", sample_word_bank_3)]
    gg_answers = [gg_answers_1, gg_answers_2, gg_answers_3]

    for count in range(len(gg_tests)):
        student_answer = generate_games_main(gg_tests[count][0], gg_tests[count][1])
        if len(student_answer) == len(gg_answers[count]):
            passed = 'PASSED!'
            for each in (gg_answers[count]):
                if each not in student_answer:
                    passed = 'FAILED!'
                    break
        else:
            passed = 'FAILED!'
        
        print("Test #{}: {}".format(count+1, passed))
        print(f'Correct Answer: {gg_answers[count]}')
        print(f'Your Answer:    {generate_games_main(gg_tests[count][0], gg_tests[count][1])}')

    print("---------------------------------------")
    print("\'find_neighbors\' Tests")
    print("---------------------------------------")
    fn_tests = [(gg_answers_1, "cat"), (gg_answers_2, "tavern"), (gg_answers_3, "hah")]
    fn_answers = [fn_answers_1, fn_answers_2, fn_answers_3]

    for count in range(len(fn_tests)):
        student_answer = find_neighbors(fn_tests[count][0], fn_tests[count][1])
        if len(student_answer[0]) == len(fn_answers[count][0]) and len(student_answer[1]) == len(fn_answers[count][1]):
            passed = 'PASSED!'
            for each in fn_answers[count][0]:
                if each not in student_answer[0]:
                    passed = 'FAILED'
                    break
            for each in fn_answers[count][1]:
                if each not in student_answer[1]:
                    passed = 'FAILED'
                    break
        else:
            passed = 'FAILED!'
        
        print("Test #{}: {}".format(count+1, passed))
        print(f'Correct Answer: {fn_answers[count]}')
        print(f'Your Answer:    {find_neighbors(fn_tests[count][0], fn_tests[count][1])}')

        