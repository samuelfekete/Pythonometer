"""Questions about compound statements.

https://docs.python.org/3.6/reference/compound_stmts.html
"""

import random
import textwrap

from ..base import Question


class CreateFunctionDecorator(Question):
    """Create a function decorator.

    https://docs.python.org/3.6/reference/compound_stmts.html#function-definitions
    """

    def get_question_text(self):
        return textwrap.dedent(
            """\
            Create a function decorator.

            Create a function decorator called `count_calls` that will count the number of times a function is called.
            Assume there's a global variable `num_of_calls`, increment it by 1 whenever the decorated function is called.
            """
        )

    def check_answer(self, answer):
        global_variables = {'num_of_calls': random.randrange(10000)}
        local_variables = {}
        try:
            exec(answer, global_variables, local_variables)
            count_calls = local_variables['count_calls']
            count_before_definition = global_variables['num_of_calls']
            @count_calls
            def test_function(arg, kwarg=0):
                return arg + kwarg
            count_before_call = global_variables['num_of_calls']
            # Check that the count does not increment on function definition.
            if count_before_call != count_before_definition:
                return False
            input_value = random.randrange(10000)
            returned_value = test_function(input_value, input_value)
            # Check that the function returns the correct value.
            if returned_value != input_value * 2:
                return False
            count_after_call = global_variables['num_of_calls']
            # Check that 1 was added to count.
            if count_after_call - count_before_call != 1:
                return False
            else:
                return True
        except:
            return False

    def get_an_answer(self):
        return textwrap.dedent(
            """\
            def count_calls(func):
                def counted_function(*args, **kwargs):
                    global num_of_calls
                    num_of_calls += 1
                    return func(*args, **kwargs)
                return counted_function
            """
        )
