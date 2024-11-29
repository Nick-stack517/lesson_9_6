def all_variants(text):
    for i_ in range(len(text)):
        for j in range(len(text) - i_):
            yield text[j:j + i_ + 1]


a = all_variants("abc")
for i in a:
    print(i)
