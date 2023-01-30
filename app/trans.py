from googletrans import Translator


def translate_text(text: str, src="auto", dest="ru"):
    try:
        translator = Translator()
        translation = translator.translate(text, src="auto", dest="ru")

        return translation.text
    except Exception as ex:
        print(ex)


def main():
    text = input("input text:   ").strip().lower()
    print(translate_text(text))


if __name__ == '__main__':
    main()
