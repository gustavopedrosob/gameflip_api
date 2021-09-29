def compare_words(string_1: str, string_2: str) -> int or float:
    from re import sub
    points = 0
    regex_to_remove = r"\W+"
    string_1 = sub(regex_to_remove, "", string_1.lower())
    string_2 = sub(regex_to_remove, "", string_2.lower()[:len(string_1)])
    for index in range(len(string_1)):
        try:
            if string_1[index].isdigit() == string_2[index].isdigit():
                points += 1 / 4
            elif string_1[index].isdigit() == string_2[index-2].isdigit():
                points += 1 / 16
            elif string_1[index].isdigit() == string_2[index-1].isdigit():
                points += 1 / 8
            elif string_1[index].isdigit() == string_2[index+2].isdigit():
                points += 1 / 16
            elif string_1[index].isdigit() == string_2[index+1].isdigit():
                points += 1 / 8
            if string_1[index].isalpha() == string_2[index].isalpha():
                points += 1 / 4
            elif string_1[index].isalpha() == string_2[index-2].isalpha():
                points += 1 / 16
            elif string_1[index].isalpha() == string_2[index-1].isalpha():
                points += 1 / 8
            elif string_1[index].isalpha() == string_2[index+2].isalpha():
                points += 1 / 16
            elif string_1[index].isalpha() == string_2[index+1].isalpha():
                points += 1 / 8
            if string_1[index] == string_2[index]:
                points += 1
            elif string_1[index] == string_2[index-2]:
                points += 1 / 4
            elif string_1[index] == string_2[index-1]:
                points += 1 / 2
            elif string_1[index] == string_2[index+1]:
                points += 1 / 2
            elif string_1[index] == string_2[index+2]:
                points += 1 / 4
        except IndexError:
            pass
    return points


def compare_phrase(phrase_1: str, phrase_2: str) -> int:
    from re import findall
    regex = r"""[a-zA-Z0-9'"+*\/\|!@#$%¨&()[\]{}]+"""
    words_1 = findall(regex, phrase_1)
    words_2 = findall(regex, phrase_2)
    points = 0
    for word_1 in words_1:
        for word_2 in words_2:
            comparison_report = words_similar_report(word_1, word_2)
            if comparison_report["is_similar"]:
                points += comparison_report["result"]
    return points


def words_similar_report(string_1: str, string_2: str, factor: float = 0.75, debug: bool = False) -> dict:
    max_points = len(string_1) * 1.5
    result = compare_words(string_1, string_2)
    factor_result = (result * 1) / max_points
    min_result = max_points * factor
    is_similar = factor_result > factor
    if debug:
        print(f"Comparing words {string_1} with {string_2}, max result: {max_points}, min result: {min_result}, "
              f"result: {result}, factor result: {factor_result}, factor: {factor}, is similar: {is_similar}")
    return dict(string_1=string_1, string_2=string_2, max_result=max_points, min_result=min_result, result=result,
                factor_result=factor_result, factor=factor, is_similar=is_similar)


def is_words_similar(string_1: str, string_2: str, factor: float = 0.75, debug: bool = False) -> bool:
    return words_similar_report(string_1, string_2, factor, debug)["is_similar"]


def most_similar_into(string: str, list_of_strings: list) -> str:
    results = {}
    for string_to_compare in list_of_strings:
        result = compare_phrase(string, string_to_compare)
        results[string_to_compare] = result
    most_similar = max(results, key=lambda key: results[key])
    return most_similar


def more_similar(string: str, list_of_strings: list, how_much: int = 5) -> list:
    results = {}
    for string_to_compare in list_of_strings:
        result = compare_phrase(string, string_to_compare)
        results[string_to_compare] = result
    more_similar_list = list(results.keys())
    more_similar_list.sort(key=lambda value: results[value], reverse=True)
    return more_similar_list[:how_much] if len(more_similar_list) > how_much else more_similar_list
