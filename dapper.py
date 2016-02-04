import collections

def parse(content):
    d = collections.defaultdict(str)
    title = None
    for line in content.splitlines():
        if line.startswith('###'):
            title = line.lstrip('### ')
            continue
        if title:
            d[title] += line + '\n'
    return dict(d)
