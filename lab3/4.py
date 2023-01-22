def char_count(str):
    answer_dict = {}
    for ch in str:
        if ch not in answer_dict.keys():
            answer_dict.update({ch: 1})
        else:
            answer_dict[ch] += 1
    
    return answer_dict
