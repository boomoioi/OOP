def only_english(string1):
    return "".join([ch for ch in string1 if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z'))])

print(only_english("1235678"))