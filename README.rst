Tool to do literate programming in Python 'backwards', separate source,
interleaved with code.

The code is broken into blocks such that:

### Block Name

Code goes here

is broken into a dictionary with 'Block Name' as the key and 'Code goes here'
as the value. This should be general enough to handle other comment types, so
it supports other languages.

It should extract it into a dictionary that can be fed into a jinja2 template system
