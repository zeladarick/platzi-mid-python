import os
import random

#Start the game
def run():
    try:    
        os.system("clear")
        print("Welcome to Hangman game!")
        game_word_str = get_random_word()
        
        #Stores all word characters with a boolean value 
        #The boolean value is True if the char is already guessed
        game_word_obj_dict = [
            {
                "char": word_char,
                "guessed":  False
            }
            for word_char in game_word_str
        ]
        print("Press any key to start!")
        input("")

        while True:
            os.system("clear")
            if(player_win(game_word_obj_dict)):
                print("Congratulations! You guessed the word "
                + game_word_str
                )
                break
            
            print_dict(game_word_obj_dict)            
            usr_char = input("Enter a character: ")

            for char_obj in game_word_obj_dict:
                if(char_obj["char"] == usr_char):
                    char_obj["guessed"] = True
                
    except Exception as e:
        print("Fatal error: ", e)

#Returns a random word from words file
def get_random_word():
    try:
        words_list = []
        file_path = "./file_resources/hangman_words.txt"

        with open(file_path, "r", encoding="utf-8") as f:
            for word in f:
                words_list.append(word)
        random_word_index = random.randint(0, len(words_list) - 1)

        #Removes breaklines from string
        random_word = words_list[random_word_index]
        random_word = random_word.replace("\n", "")
        return random_word

    except Exception as e:
        raise Exception("Uncorrect or corrupted data in "
        + file_path)         

#Print in console the hangman text
def print_dict(chars_obj_list):
    
    to_print_list = [
        (word_char["char"] if word_char["guessed"] else "_")
        for word_char in chars_obj_list
    ]

    print("---------------")
    for actual_char in to_print_list:
        print(actual_char, end = '')
    print("\n", end = '')    
    print("---------------")

#Returns True/False if game is over
def player_win(chars_obj_list):
    
    for char_obj in chars_obj_list:
        if not char_obj["guessed"]:
            return False
    return True

if __name__ == '__main__':
    run()