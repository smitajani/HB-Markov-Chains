"""Generate Markov text from text files."""

from random import choice, choices


def open_and_read_file(file_path):

    #return "Contents of your file as one long string"

    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_file = open(file_path)
    text_string = text_file.read().replace("\n", " ")

    text_file.close()

    return text_string




def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}

    word_list = text_string.split(" ")

    index = 0

    while index < (len(word_list) - 2):
        key = (word_list[index], word_list[index + 1])
        chains[key] = chains.get(key, [])
        new_list = chains.get(key)
        new_list.append(word_list[index + 2])
        chains[key] = new_list 
        print(f"{index} - {key} - {new_list}")
        index += 1
        #checker_string = str(key[0]) + " " + str(key[1])

    return chains


def make_text(chains):
    """Return text from chains."""

    the_new_string_of_words = []
    # Pick a random starting word from chains dictionary
    # Get start_word's corresponding values from the dictionary   
    words_for_my_key = choice(list(chains.keys()))
    print(f"Start with - {words_for_my_key}")

    i=0
    for words_for_my_key in chains:

        list_of_words_to_choose_from = chains.get(words_for_my_key)
        
        # Use choices to randomly pick the next word using occurance count len(list_of_words_to_choose_from),  
        next_word = choices(list_of_words_to_choose_from, k = 1)
        
        the_new_string_of_words.extend(words_for_my_key)
        the_new_string_of_words.extend(next_word)
        words_for_my_key = the_new_string_of_words[-2:]

        print(f"Values for the key - {list_of_words_to_choose_from}\n",
        f"Picked my next word - {next_word}\n",
        f"New string of words - {the_new_string_of_words}\n",    
        f"New key - {i}   {words_for_my_key}\n\n")
        if i > 3: 
            break
        i = i + 1
    # your code goes here

    return " ".join(the_new_string_of_words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
