import random
import string

class GameLogicService():

    def __init__(self, word_list_path):
        self.__word_list = self.__load_words_from_file(word_list_path)
        
        

    def search_for_word(self, word):
        for w in self.__word_list:
            if w == word:
                return True
        return False
    
    def __load_words_from_file(self, path) -> list[str]:
        with open(path, 'r') as f:
            return f.read().splitlines()

    def generate_random_letters(self, length):
        return random.choices(string.ascii_lowercase, k=length)
    
    def generate_valid_random_letters(self, level):
        letters = self.get_letters_for_level(level)

        while not self.letters_can_make_word(letters):
            letters = self.get_letters_for_level(level)

        return letters
    
    def get_letters_for_level(self, level):
        
        if level == 1:
            count = random.randint(2, 5)
        elif level == 2:
            count = random.randint(6, 10)
        elif level == 3:
            count = random.randint(11, 15)
        else: 
            count = 0

        return self.generate_random_letters(count)
    

    def letters_can_make_word(self, letters):        

        for word in self.__word_list:

            # if len(word) < 3:
            #     continue

            word_found = True
            count = 0

            corpus = letters.copy()

            while count < len(word):
                if word[count] not in corpus:                    
                    word_found = False
                    break

                corpus.remove(word[count])
                count += 1

            if word_found:
                return True
            
        return False
    
    def get_total_possible_words(self, letters: list[str]) -> int:
        total = 0

        for word in self.__word_list:
            
            if len(word) < 3:
                continue

            word_found = True
            count = 0

            corpus = letters.copy()

            while count < len(word):
                if word[count] not in corpus:
                    word_found = False
                    break

                corpus.remove(word[count])

                count += 1

            if word_found:
                total += 1

        return total   
            

    def get_score(self, word, letters: list[str]) -> int:
        if len(word) < 3:
            return 0

        if not self.search_for_word(word):
            return 0
        
        print(word, letters)
        if len(word) == len(letters):            
            return len(word) * 2
        
        return len(word)


            


        
