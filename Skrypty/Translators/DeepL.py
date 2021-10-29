import requests

class DeepL:

    auth_key = 'b6d509df-301f-1b2c-8e7c-ec5e82ec108c'

    def translate_text(self, target, text):
        self.r =  requests.post(url='https://api.deepl.com/v2/translate',
                          data = {
                            'target_lang' : target,  
                            'auth_key' : self.auth_key,
                            'text': text
                          })
        print(self.r)
        return (self.r.json()["translations"][0]["text"])