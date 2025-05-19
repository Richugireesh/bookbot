
def get_num_word(text):
    return len(text.split())

def sort_on(dict):
    return dict["num"]

def char_count(text):
    char_list = list(text)
    count = dict()
    for c in char_list:
        lower_char = c.lower()
        if lower_char not in count:
            count.update({lower_char : 1})
        else:
            count[lower_char] += 1
    return count

def sort_char(dict_char):
    #dict_char = sorted(dict_char.items(), key=lambda x:x[1], reverse=True)
    dict_list_char = []
    for key in dict_char:
        a_key = {"char":key,"num":dict_char[key]}
        dict_list_char.append(a_key)

    dict_list_char.sort(reverse=True, key=sort_on)
    return dict_list_char
