from nltk.translate.bleu_score import sentence_bleu
import string

class BleuScore:
   
    def calculate_bleu(self, translation, reference):
        #print("reference clear: ",reference)
        #print("candidate clear: ", translation)
        self.candidate = translation.lower().translate(str.maketrans('', '', string.punctuation)).split()
        self.reference = [reference.lower().translate(str.maketrans('', '', string.punctuation)).split()]
        #print("reference processed: ",self.reference)
        #print("candidate processed: ", self.candidate)
        return round(sentence_bleu(self.reference, self.candidate),3)
        