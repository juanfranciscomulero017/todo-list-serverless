import boto3


translate = boto3.client('translate')

cuerpo = "prueba"
    
cadena1_traducida = translate.translate_text(Text=cuerpo,
                                         SourceLanguageCode="auto",
                                         TargetLanguageCode="en")
                                        
lenguaje = input(cadena1_traducida["TranslatedText"])

print(lenguaje)