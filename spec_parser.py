r"""
The parser should parse a file and give a dictionary of titled sections and the code in it.

For example:

    ### section 1
    This is a line of code.

Should give output:

    { 'section 1' : 'This is a line of code.\n' }
"""
import dapper

from textwrap import dedent as dd

class DescribeParser(object):
    def it_should_parse_a_titled_line(self):
        file_content = dd("""\
                          ### section 1
                          This is a line of code.
                          """)
        expected =  { 'section 1' : 'This is a line of code.\n' }
        assert dapper.parse(file_content) == expected

    def it_should_parse_two_title_lines(self):
        file_content = dd("""\
                          ### section 1
                          This is a line of code.
                          ### section 2
                          This is a second line of code.
                          """)
        expected =  { 'section 1' : 'This is a line of code.\n',
                      'section 2' : 'This is a second line of code.\n' }
        assert dapper.parse(file_content) == expected
