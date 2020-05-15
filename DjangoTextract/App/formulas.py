from DjangoTextract.settings import MEDIA_ROOT
import boto3

textract =boto3.client('textract')

def DetectarTexto(img):
    texto   = ''
    ruta    = (MEDIA_ROOT) + str(img)
    with open(ruta, 'rb') as document:
        imageBytes  = bytearray(document.read())
    respuesta       = textract.detect_document_text(Document={'Bytes': imageBytes})
    for x in respuesta["Blocks"]:
        if x["BlockType"] == "LINE":
            texto = texto + (x['Text']) + ('\n')
    return texto
