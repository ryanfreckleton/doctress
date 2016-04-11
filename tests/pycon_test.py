from textwrap import dedent

from doctress import pycon

class DescribeConsole:
    def check_simple_statement(self):
        statement = 'a = 1'
        assert pycon.console(statement) == '>>> a = 1'

    def check_simple_expression(self):
        expression = '1 + 1'
        assert pycon.console(expression) == '>>> 1 + 1\n2\n'

    def check_complex_statements(self):
        statements = 'def f():\n    pass'
        expected = dedent("""\
               >>> def f():
               ...     pass""")
        assert pycon.console(statements) == expected

    def check_invalid_syntax(self):
        statement = 'do'
        expected = dedent("""\
               >>> do
               Traceback (most recent call last):
                 File "<stdin>", line 1, in <module>
               NameError: name 'do' is not defined""")
        assert pycon.console(statement) == expected
