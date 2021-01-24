import boto3
import locale

language_system = locale.getdefaultlocale()[0]

cadena1 = 'Introduce el idioma al que quieres traducir la frase: '

translate = boto3.client('translate')

cadena1_traducida = translate.translate_text(Text=cadena1,
                                          SourceLanguageCode="auto",
                                                                            TargetLanguageCode=language_system[0:2])

lenguaje = input(cadena1_traducida["TranslatedText"])

cadena2 = 'Introduce una frase en un idioma: '

cadena2_traducida = translate.translate_text(Text=cadena2,
                                          SourceLanguageCode="auto",
                                                                            TargetLanguageCode=language_system[0:2])

cadena = input(cadena2_traducida["TranslatedText"])

result = translate.translate_text(Text=cadena,
                                          SourceLanguageCode="auto",
                                                                            TargetLanguageCode=lenguaje)

print(f'TranslatedText: {result["TranslatedText"]}')
print(f'SourceLanguageCode: {result["SourceLanguageCode"]}')
print(f'TargetLanguageCode: {result["TargetLanguageCode"]}')
