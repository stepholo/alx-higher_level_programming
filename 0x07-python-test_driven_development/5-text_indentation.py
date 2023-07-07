#!/usr/bin/python3
def text_indentation(text):
    """fucntions that prints a text with 2 new lines after each of 
       these characters . ? and :
    Arg:
       text: The text to be passed 
    Raise:
      TypeError: if text is not string
    Return:
       the printed texts
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        new_text = [char for char in text]

        for i in range(len(new_text)):
            if new_text[i] == '.':
                new_text.insert(i + 1, '\n\n')
            elif new_text[i] == '?':
                new_text.insert(i + 1, '\n\n')
            elif new_text[i] == ':':
                new_text.insert(i + 1, '\n\n')

        last_char = new_text[-1]
        if last_char in ['.', '?', ':']:
            new_text.append('\n\n')

        print_text = "".join(new_text)

        lines = print_text.split("\n")
        formatted_lines = [line.strip() for line in lines]
        formatted_text ="\n".join(formatted_lines)
        print(formatted_text, end="")
            
                
