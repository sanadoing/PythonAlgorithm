def solution(survey, choices):
    result = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    n = len(choices)
    for s, c in zip(survey, choices):
        c = c - 4
        if c < 0:
            result[s[0]] -= c
        elif c > 0:
            result[s[1]] += c
    answer = ""

    p_types = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    for type1, type2 in p_types:
        if result[type1] >= result[type2]:
            answer += type1
        else:
            answer += type2
    return answer