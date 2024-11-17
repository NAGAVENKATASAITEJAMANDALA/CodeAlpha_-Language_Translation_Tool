from googletrans import Translator
translator = Translator()
text_to_translate = input("Enter the text to translate: ")
target_language = input("like (te) for telugu ,(fr) french ,(de) for german ")

# Translate text to the target language
translated_text = translator.translate(text_to_translate, src='en', dest=target_language)

# Display the translated text
print(f" {target_language}:", translated_text.text)     