"""Test all questions."""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pythonometer.quiz import all_questions


class TestQuestions(unittest.TestCase):
    """Test the questions.

    All question tests are the same, so they are loaded dynamically.
    """
    pass


# Add a test for every question.
for question in all_questions():
    def question_test(self, question=question):
        current_question = question()

        # Assert that a question string is supplied.
        question_string = current_question.get_question_text()
        self.assertIsInstance(question_string, basestring)

        # Assert that checking with the supplied answer returns True.
        self.assert_(current_question.check_answer(current_question.get_an_answer()))

        # Assert that checking a wrong answer returns False.
        self.assertFalse(current_question.check_answer(''))

        # Assert that checking the answer with bad code returns False.
        self.assertFalse(current_question.check_answer('raise Exception'))

    setattr(TestQuestions, 'test_{}'.format(question.__name__), question_test)


if __name__ == '__main__':
    unittest.main()
