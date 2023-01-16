def only_english(string1):
    return len([ch for ch in string1 if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z'))])

txt = input()
print(only_english(txt))