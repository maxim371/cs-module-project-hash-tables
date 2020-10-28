import re
def word_count(s):
    # declare word_dict
    word_dict = dict()
    #split string into words
    words = s.split()
    if words == ['']:
        return {}
    for w in words:
        parsed_word = re.sub(
            r'[\"\&\.\:\;\,\-\+\=\/\\\[\]\{\}\(\)\*\^\&\|\s]', '', w.lower()
        )

        if parsed_word == '':
            continue

        else:
            if word_dict.get(parsed_word):
                word_dict[parsed_word] += 1
            else:
                word_dict[parsed_word] = 1
    return word_dict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))