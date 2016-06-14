import collections

from docutils import nodes
from docutils.parsers.rst import Directive

def parse(text):
    results = collections.defaultdict(list)
    header = ''
    for line in text.splitlines():
        if line.startswith('/**'):
            header = line.split()[1]
        else:
            results[header].append(line)
    return dict((key, '\n'.join(value))
                for (key, value) in results.iteritems())

class SeeDirective(Directive):
    optional_arguments = 2
    final_argument_whitespace = False

    def run(self):
        if self.arguments and self.content:
            raise Exception("pycon directive takes a filename OR content, not both.")
        if self.arguments:
            filename = self.arguments[0]
            content = open(filename).read()
            language = filename.split('.')[-1]
        if len(self.arguments) > 1:
            section = self.arguments[1]
            content = parse(content)[section]

        node = nodes.literal_block(text=content)
        node['classes'].append('code-block')
        node['language'] = language

        return [node]
