import six
from google.cloud import translate_v2 as translate

class GoogleTranslator:
    def translate_text(self, target, text):
        
        self.translate_client = translate.Client()

        if isinstance(text, six.binary_type):
            text = text.decode("utf-8")
    
            # Text can also be a sequence of strings, in which case this method
            # will return a sequence of results for each text.
        self.result = self.translate_client.translate(text, target_language=target)

        #print(u"Text: {}".format(self.result["input"]))
        #print(u"Translation: {}".format(self.result["translatedText"]))
        #print(u"Detected source language: {}".format(self.result["detectedSourceLanguage"]))
        return (u"{}".format(self.result["translatedText"]).lower())
