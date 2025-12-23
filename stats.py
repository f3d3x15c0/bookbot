from operator import itemgetter

def count_words(content):
    words_list = content.split()
    count = 0
    for word in words_list:
        count += 1
    return count

def count_characters(content):
    characters_map = {}
    for x in content:
        if x.lower() not in characters_map.keys():
            characters_map[x.lower()] = 1
        else:
            characters_map[x.lower()] += 1
    return characters_map

def count_characters_ordered(dict):
    list = []
    for x in dict:
        if x.isalpha():
            list.append({"char": x, "num": dict[x]})

    sorted_list = sorted(list, key=itemgetter('num'), reverse=True)
    
    for x in sorted_list:
        print(f"{x['char']}: {x['num']}")



