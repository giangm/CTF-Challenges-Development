from pprint import pprint

combinations = {"row_1": [], "row_2": [], "row_3": [], "row_4": [], "row_5": [], "row_6": [],
                "col_1": [], "col_2": [], "col_3": [], "col_4": []}

with open("wordlist.txt", "r") as wordlist:
    for word in wordlist:
        # Row #1
        if len(word.strip()) == 8 and word[6] == "n":
            combinations["row_1"].append(word.strip())

        # Row #2
        elif len(word.strip()) == 8 and word[1] == "o":
            combinations["row_2"].append(word.strip())

        # Row #3
        elif len(word.strip()) == 9 and word[3] == "i" and word[5] == "t":
            combinations["row_3"].append(word.strip())

        # Row #4
        elif len(word.strip()) == 13 and word[3] == "n" and word[5] == "r":
            combinations["row_4"].append(word.strip())

        # Row #5
        elif len(word.strip()) == 12 and word[3] == "p":
            combinations["row_5"].append(word.strip())

        # Row #6
        elif len(word.strip()) == 15 and word[7] == "n":
            combinations["row_6"].append(word.strip())

        # Col #1
        elif len(word.strip()) == 10 and word[3] == "i":
            combinations["col_1"].append(word.strip())

        # Col #2
        elif len(word.strip()) == 9 and word[1] == "n" and word[7] == "t":
            combinations["col_2"].append(word.strip())

        # Col #3
        elif len(word.strip()) == 13 and word[4] == "o" and word[12] == "n":
            combinations["col_3"].append(word.strip())

        # Col #4
        elif len(word.strip()) == 13 and word[6] == "r" and word[8] == "p" and word[11] == "n":
            combinations["col_4"].append(word.strip())

pprint(combinations)