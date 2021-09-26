# Cleans up words_alpha.txt, removing words that are less than 6 characters and extra words.
# Word list from https://github.com/dwyl/english-words

with open("words_alpha.txt", "r") as words_alpha:
    with open("wordlist.txt", "w") as wordlist:
        for word in words_alpha:
            if len(word.strip()) >= 6:
                if word == "sniffing\n" or word == "honeypot\n":
                    wordlist.write(word)
                    continue
                elif len(word.strip()) == 8:
                    continue

                if word == "plaintext\n" or word == "integrity\n":
                    wordlist.write(word)
                    continue
                elif len(word.strip()) == 9:
                    continue

                if word == "mitigation\n":
                    wordlist.write(word)
                    continue
                elif len(word.strip()) == 10:
                    continue

                if word == "cryptography\n":
                    wordlist.write(word)
                    continue
                elif len(word.strip()) == 12:
                    continue

                if word == "vulnerability\n" or word == "authorization\n" or word == "eavesdropping\n":
                    wordlist.write(word)
                    continue
                elif len(word.strip()) == 13:
                    continue

                if word == "confidentiality\n":
                    wordlist.write(word)
                    continue
                elif len(word.strip()) == 15:
                    continue

                wordlist.write(word)