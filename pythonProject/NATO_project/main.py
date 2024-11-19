import pandas

data = pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")

letter = data["letter"].to_dict()
code = data["code"].to_dict()

dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict)

answer = input("what's is your name ? \n").upper()
answer_list = list(answer.strip())

print(answer_list)

result = [dict[f"{key}"] for key in answer_list]
print(result)
