import boto3


class AmazonTranslate:
    def translate_text(self, target, text):
        
        self.translate = boto3.client(service_name='translate', region_name='us-west-2')

        self.result = self.translate.translate_text(Text=text, 
                SourceLanguageCode="pl", TargetLanguageCode=target)

        #print('TranslatedText: ' + self.result.get('TranslatedText'))
        #print('SourceLanguageCode: ' + self.result.get('SourceLanguageCode'))
        #print('TargetLanguageCode: ' + self.result.get('TargetLanguageCode'))
        
        return (self.result.get('TranslatedText'))