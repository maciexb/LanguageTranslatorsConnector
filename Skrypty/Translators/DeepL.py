import requests

class DeepL:

    auth_key = 'xxx'

    def translate_text(self, target, text):
        self.r =  requests.post(url='https://api.deepl.com/v2/translate',
                          data = {
                            'target_lang' : target,  
                            'auth_key' : self.auth_key,
                            'text': text
                          })
        print(self.r)
        return (self.r.json()["translations"][0]["text"])
