from yandex.Translater import Translater

class YandexTranslate:
    tr = Translater()
    tr.set_key('xxx') # Api key found on https://translate.yandex.com/developers/keys

    def translate_text(self, target, text):
        
        self.tr.set_from_lang('pl')
        self.tr.set_to_lang(target)
        self.tr.set_text(text)
        
        #print(self.tr.translate())
        return (self.tr.translate())
