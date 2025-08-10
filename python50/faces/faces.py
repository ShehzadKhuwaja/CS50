def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence

def main():
    sentence = input()
    print(convert(sentence))

if __name__== "__main__":
    main()