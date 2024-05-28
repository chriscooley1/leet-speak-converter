def convert(text: str) -> str:
    leet_dict = {
        'a': '@', 'A': '4',
        'B': '8', 'b': '8',
        'E': '3', 'e': '3',
        'I': '!', 'i': '!',
        'L': '1', 'l': '1',
        'O': '0', 'o': '0',
        'S': '5', 's': '5'
    }
    
    leet_text = []
    
    for char in text:
        leet_text.append(leet_dict.get(char, char))
    
    return ''.join(leet_text)

text = "Hello World! This is an example of leet speak."
converted_text = convert(text)
print(converted_text)
