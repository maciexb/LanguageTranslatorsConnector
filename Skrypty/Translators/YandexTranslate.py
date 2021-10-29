from yandex.Translater import Translater

class YandexTranslate:
    tr = Translater()
    tr.set_key('trnsl.1.1.20210930T081813Z.9fb115603f3d0aae.7c0d268f730355aafff70ea03fa7aa3c1d55ee32') # Api key found on https://translate.yandex.com/developers/keys

    def translate_text(self, target, text):
        
        self.tr.set_from_lang('pl')
        self.tr.set_to_lang(target)
        self.tr.set_text(text)
        
        #print(self.tr.translate())
        return (self.tr.translate())