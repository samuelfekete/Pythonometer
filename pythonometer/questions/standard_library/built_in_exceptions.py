"""Tests for the built-in exceptions.

Docs: https://docs.python.org/3.6/library/exceptions.html
"""

from ..base import Question


class CauseAssertionError(Question):
    """Cause an AssertionError.

    https://docs.python.org/3.6/library/exceptions.html#AssertionError
    """

    def get_question_text(self):
        return (
            'Cause an AssertionError.\n\n'
            'Write some code that will raise an AssertionError.\n\n'
            'Your code may not contain the words `raise` or `exec`.'
        )

    def check_answer(self, answer):
        for illegal_word in ['raise', 'exec']:
            if illegal_word in answer:
                return False
        try:
            exec(answer, {}, {})
        except AssertionError:
            return True
        except:
            return False

    def get_correct_answers(self):
        return ['assert(False)']

    def get_wrong_answers(self):
        return ['raise AssertionError']
