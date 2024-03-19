import unittest
from src.services.game_logic import GameLogicService

class TestGameLogicService(unittest.TestCase):
    def setUp(self) -> None:
        self.game_logic_service = GameLogicService("./resources/words.txt")
    
    def test_search_for_word(self):
        # Act 
        valid_word = self.game_logic_service.search_for_word('hello')
        invalid_word = self.game_logic_service.search_for_word('not in here')

        # assets 
        self.assertTrue(valid_word)
        self.assertFalse(invalid_word)

    def test_generate_random_letters(self):
        # arrage 
        letters = self.game_logic_service.generate_random_letters(10)

        # assert 
        self.assertEqual(len(letters), 10)

    def test_generate_random_letters_contains_letters(self):
        # arrage
        letters = self.game_logic_service.generate_random_letters(10)

        # assert
        for letter in letters:
            self.assertTrue(letter.isalpha())

    def test_generate_random_letters_is_lowercase(self):
        # arrage
        letters = self.game_logic_service.generate_random_letters(10)

        # assert
        for letter in letters:
            self.assertTrue(letter.islower())

    def test_generate_random_letter_is_list(self):
        # arrage
        letters = self.game_logic_service.generate_random_letters(10)

        # assert
        self.assertIsInstance(letters, list)

    def test_letters_for_level_value_in_range(self):    
        for i in range(10):
            level_one = self.game_logic_service.get_letters_for_level(1)
            level_two = self.game_logic_service.get_letters_for_level(2)
            level_three = self.game_logic_service.get_letters_for_level(3)

            level_one_actual = 2 <= len(level_one) <= 5
            level_two_actual = 6 <= len(level_two) <= 10
            level_three_actual = 11 <= len(level_three) <= 15

            # Assert 
            self.assertTrue(level_one_actual, f"Expected range 2 - 5 got: {len(level_one)}")
            self.assertTrue(level_two_actual, f"Expected range 6 - 10 got: {len(level_two)}")
            self.assertTrue(level_three_actual, f"Expected range 11 - 15 got: {len(level_three)}")

    def test_letters_can_make_word(self):
        # Arrange
        valid = ['p', 'y', 't', 'h', 'o', 'n']
        valid_two = ['p', 'y', 't', 'h', 'o', 'n', 'r','u','b']
        invalid = ['j', 'p', 'k']

        # Assert 
        actual_valid = self.game_logic_service.letters_can_make_word(valid)
        actual_invalid = self.game_logic_service.letters_can_make_word(invalid)
        actual_valid_two = self.game_logic_service.letters_can_make_word(valid_two)



        # Assert 
        self.assertTrue(actual_valid)
        self.assertTrue(actual_valid_two)
        self.assertFalse(actual_invalid)

    def test_total_possible_words_correct_count(self):
        # Arrange 
        should_have_one = ['p', 'y', 't', 'h', 'o', 'n']
        should_have_two = ['p', 'y', 't', 'h', 'o', 'n', 'r','u','b']
        should_have_zero = ['j', 'p', 'k']

        # Assert 
        actual_should_have_one = self.game_logic_service.get_total_possible_words(should_have_one)
        actual_should_have_two = self.game_logic_service.get_total_possible_words(should_have_two)
        actual_should_have_zero = self.game_logic_service.get_total_possible_words(should_have_zero)

        # Assert
        self.assertEqual(actual_should_have_one, 1, f"Should have 1 got: {actual_should_have_one}")
        self.assertEqual(actual_should_have_two, 2, f"Should have 2 got: {actual_should_have_two}")
        self.assertEqual(actual_should_have_zero, 0, f"Should have 0 got: {actual_should_have_zero}")


    def test_search_for_word(self):
        # Arrange
        valid_words = ['hello', 'python', 'javascript']
        invalid_words = ['not', 'here', 'really']
        
        # Assert Valid words
        for word in valid_words:
            actual = self.game_logic_service.search_for_word(word)
            self.assertTrue(actual)

        # Assert Invalid words
        for word in invalid_words:
            actual = self.game_logic_service.search_for_word(word)
            self.assertFalse(actual)

    def test_get_score(self):
        input_and_score = [
            ('python', ['p','y','t','h','o','n'], 12),
            ('hello', ['h', 'e', 'l', 'l', 'o'], 10),
            ('ruby', ['p', 'y', 't', 'h', 'o', 'n', 'r','u','b'], 4)
        ]

        for word, letters, expected_score in input_and_score:
            actual_score = self.game_logic_service.get_score(word, letters)

            self.assertEqual(actual_score, expected_score)    

    def test_generate_valid_random_letters(self):
        # Arrange
        letters = self.game_logic_service.generate_valid_random_letters(2)        

        # Assert
        self.assertTrue(self.game_logic_service.letters_can_make_word(letters))

if __name__ == '__main__':
    unittest.main()
