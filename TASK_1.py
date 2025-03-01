from spellchecker import SpellChecker

spell = SpellChecker()

def get_suggestions(word):
    return list(spell.candidates(word))

def autocorrect(text):
    words = text.split()
    corrected_text = []

    for word in words:
        if word in spell:
            corrected_text.append(word)
        else:
            suggestions = get_suggestions(word)
            
            if suggestions:
                print(f"\nPossible corrections for '{word}':")
                for i, suggestion in enumerate(suggestions, 1):
                    print(f"{i}. {suggestion}")
                
                while True:
                    try:
                        choice = int(input(f"Select the correct option (1-{len(suggestions)}) or 0 to keep '{word}': "))
                        if choice == 0:
                            corrected_text.append(word)
                            break
                        elif 1 <= choice <= len(suggestions):
                            corrected_text.append(suggestions[choice - 1])
                            break
                        else:
                            print("Invalid choice, please enter a valid option.")
                    except ValueError:
                        print("Please enter a number.")
            else:
                corrected_text.append(word)

    return ' '.join(corrected_text)

def main():
    input_text = input("Please enter a sentence: ")
    corrected_text = autocorrect(input_text)
    print(f"\nFinal Corrected Text: {corrected_text}")

if __name__ == "__main__":
    main()
