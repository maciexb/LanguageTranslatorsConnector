#!/usr/bin/env python
# coding: utf-8

# In[4]:

data_in = "D:\Dokumenty\Praca_Magisterska\MagisterkaGlowna\Model\Dane\Surowe"
data_proc = "D:\Dokumenty\Praca_Magisterska\MagisterkaGlowna\Model\Dane\Przetworzone"
data_out = "D:\Dokumenty\Praca_Magisterska\MagisterkaGlowna\Model\Skrypty\Comparisson\DataOut"
data_test = "D:\Dokumenty\Praca_Magisterska\MagisterkaGlowna\Model\Dane\Testowe\Surowe"

# In[9]:

import statistics
from Components.FileNames import FileNames as FN
from Translators.GoogleTranslator import GoogleTranslator
from Translators.MicrosoftTranslator import MicrosoftTranslator
from Translators.AmazonTranslate import AmazonTranslate
from Components.BleuScore import BleuScore
from Translators.DeepL import DeepL
from Translators.YandexTranslate import YandexTranslate
import pandas as pd

# In[158]:


# load doc into memory
def load_doc(filename):
    # open the file as read only
    if filename.split("\\")[-1] == FN.subtitles_pl:
        encoding = "unicode_escape"
    else:
        encoding = "utf-8"
        
    file = open(filename, mode='rt', encoding=encoding)
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text


# split a loaded document into sentences
def to_sentences(doc):
    return doc.strip().split('\n')

def CreateNSentences(filename):
    filename = filename
    file = data_test + "\\" + filename
    doc = load_doc(file)
    sentences = to_sentences(doc)
    #sentences = sentences[0:10]
    return sentences
    
# In[166]:

def translate_text(translator_name, target, text):
    """Translates text into the target language.
    
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    
    if translator_name == "GoogleTranslator":
        GT = GoogleTranslator()
        result = GT.translate_text(target = target, text = text)
    
    elif translator_name == "MicrosoftTranslator":
        MT = MicrosoftTranslator()
        result = MT.translate_text(target,text)
        
    elif translator_name == "AmazonTranslate":
        AT = AmazonTranslate()
        result = AT.translate_text(target, text)
        
    elif translator_name == "DeepL":
        DL = DeepL()
        result = DL.translate_text(target, text)
    
    elif translator_name == "YandexTranslate":
        YT = YandexTranslate()
        result = YT.translate_text(target, text)
    
    return result
           
# In[ ]:

def translate_sentences(translator_name, sentences, target):
    
    translated = []
    for sentence in sentences:
        result = translate_text(translator_name = translator_name, target = target, text = sentence)
        translated.append(result)
    
    return translated

# In[235]:

def calculate_avg_BLEU(translated, sentences_eng):
    global score_all
    global reference_all
    global candidate_all
    score_all = []
    reference_all = []
    candidate_all = []
    CB = BleuScore()
    for candidate, reference in zip(translated, sentences_eng):
        score = CB.calculate_bleu(reference, candidate)
        score_all.append(score)
        reference_all.append(reference)
        candidate_all.append(candidate)
    return(statistics.mean(score_all))


# In[236]:

def main():

    Translators = ["DeepL"]
    Data_from = [FN.bible_pl]
    Data_to = [FN.bible_eng]

    for Translator in Translators:
        for Dataframe_from, Dataframe_to in zip (Data_from, Data_to):
            sentences_from = CreateNSentences(Dataframe_from)
            sentences_to = CreateNSentences(Dataframe_to)
        
            translated = translate_sentences(Translator, sentences_from, target = "en")
        
            print ("BLEU for ", Translator, " on ", Dataframe_from,": ",str(calculate_avg_BLEU(translated, sentences_to)))
            data = pd.DataFrame({'Sentences_from': sentences_from, "Sentences_to": sentences_to, "Translated_sentences": translated, "BLEU": score_all})
            data.to_csv(data_out+ "\\" + Translator + "_" + Dataframe_from + ".csv")

# In[237]:
       
main()
# In[238]:


# In[182]:


# In[193]:


# In[ ]:

