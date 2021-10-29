import requests, uuid

class MicrosoftTranslator:
    subscription_key = "c62bff9c4fb24c93a5bd8bdd121074fa"
    endpoint = "https://api.cognitive.microsofttranslator.com/"
    
    # Add your subscription key and endpoint
        

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
    location = "westeurope"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
            'api-version': '3.0',
            'from': 'pl',
            'to': ['en']
            }
    constructed_url = endpoint + path

    headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
            }

    
    
    def translate_text(self, target, text):
        # You can pass more than one object in body.
        self.body = [{
            'text': text
            }]
    
        request = requests.post(self.constructed_url, params=self.params, headers=self.headers, json=self.body)
        response = request.json()

        #print(response[0]['translations'][0]['text'])
        return (response[0]['translations'][0]['text'])