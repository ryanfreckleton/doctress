import StringIO
import code
import contextlib
import sys

import docutils.core
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.writers.html4css1 import Writer

def console(lines):
    interpreter = Interpreter()
    next_prompt = '>>> '
    results = []
    for line in lines.splitlines():
        with stdoutIO() as s:
            result = interpreter.push(line)
        results.append(next_prompt + line)
        if s.getvalue():
            results.append(s.getvalue())
        if result:
            next_prompt = '... '
        else:
            next_prompt = '>>> '
        results.extend(line.rstrip() for line in interpreter.output)
    return '\n'.join(results)

class Interpreter(code.InteractiveConsole):
    def __init__(self):
        self.output = []
        code.InteractiveConsole.__init__(self, filename="<stdin>")

    def write(self, data):
        self.output.append(data)

@contextlib.contextmanager
def stdoutIO(stdout=None):
    if stdout is None:
        stdout = StringIO.StringIO()
    old = sys.stdout
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


class PyconDirective(Directive):
    optional_arguments = 1
    final_argument_whitespace = False
    has_content = True

    def run(self):
        if self.arguments and self.content:
            raise Exception("pycon directive takes a filename OR content, not both.")
        if self.arguments:
            content = open(self.arguments[0]).read()
        if self.content:
            content = '\n'.join(self.content)

        results = console(content)
        return [
            nodes.literal_block(
                text=results
            )
        ]

