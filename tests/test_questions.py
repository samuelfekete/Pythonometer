"""Test all questions."""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pythonometer.quiz import all_questions
from pythonometer.questions.base import WrongAnswer


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

        # Assert that at least one correct answer is given.
        self.assert_(current_question.get_correct_answers())

        # Assert that checking with the correct answers returns True.
        for correct_answer in current_question.get_correct_answers():
            self.assert_(current_question.check_answer(correct_answer))

        # Assert that checking with the wrong answers raises WrongAnswer.
        for wrong_answer in current_question.get_wrong_answers():
            with self.assertRaises(WrongAnswer):
                current_question.check_answer(wrong_answer)

        # Assert that checking a wrong answer raises WrongAnswer.
        with self.assertRaises(WrongAnswer):
            current_question.check_answer('')

        # Assert that checking the answer with bad code raises WrongAnswer.
        with self.assertRaises(WrongAnswer):
            current_question.check_answer('raise Exception')

    setattr(TestQuestions, 'test_{}'.format(question.__name__), question_test)


if __name__ == '__main__':
    unittest.main()
