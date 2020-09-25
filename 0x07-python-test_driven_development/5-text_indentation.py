#!/usr/bin/python3
def text_indentation(text):
    """
    text_identation - Prints a text with 2 new lines after : . ?
    @text: where Type text must be a str
    """

    if text == "":
        raise TypeError('text must be a string')
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i in ['.', '?', ':']:
        text = text.replace(i, i + '\n\n')
    new = [line.strip() for line in text.split('\n')]
    new = '\n'.join(new)
    print(new, end='')
