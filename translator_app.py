from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# Extract language options
language_options = LANGUAGES.items()
language_codes = []
language_names = []

# Helper function to display language options
def errors():
    print("\nUnknown language. Wisely choose from these options:")
    print(f"\nLanguage Codes:\n{language_codes}")
    print(f"\nLanguage Names:\n{language_names}\n")

# Populate language codes and names
for code, name in language_options:
    language_codes.append(code)
    language_names.append(name.lower())

# Get user input
translating_from = input("Enter the language code or name you want to translate from:\n").strip().lower()
word = input("Enter the word or sentence you want to translate:\n").strip()
translating_to = input("Enter the language code or name you want to translate to:\n").strip().lower()

try:
    # Check if inputs are valid
    from_code = translating_from if translating_from in language_codes else None
    to_code = translating_to if translating_to in language_codes else None

    if translating_from in language_names:
        from_code = language_codes[language_names.index(translating_from)]

    if translating_to in language_names:
        to_code = language_codes[language_names.index(translating_to)]

    if from_code and to_code:
        # Perform translation
        translation = translator.translate(word, src=from_code, dest=to_code).text
        print(f"\nTranslation ({from_code} -> {to_code}):\n{translation}")
    else:
        errors()

except Exception as e:
    print(f"\nSomething went wrong: {e}")
    errors()
