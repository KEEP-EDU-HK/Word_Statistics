import collections
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import os

basepath = os.path.dirname(os.path.realpath(__file__))
# print(basepath)
miscpath = 'misc'
joined_path = os.path.join(basepath, miscpath)
# print(joined_path)
mycwd = os.getcwd()

class Lexicalmetrics:
    def __init__(self):
        self.wordfrequency_all = None
        self.wordfrequency_context = None
        self.wordfrequency_function = None
        self.wordrangescore = None
        self.familiarityscore = None
        self.concretenessscore = None
        self.imageabilityscore = None
        self.meaningfulnesscscore = None
        self.meaningfulnesspscore = None
        self.ageofacquisitionscore = None

    def generate_score(self, tokenized_text):
        try:
            os.chdir(joined_path)
            f = open('written.num', 'r', encoding='utf-8')
            f1 = open('familiarity.txt', 'r', encoding='utf-8')
            f2 = open('concreteness.txt', 'r', encoding='utf-8')
            f3 = open('imageability.txt', 'r', encoding='utf-8')
            f4 = open('meaningfulness_coloradonorms.txt', 'r', encoding='utf-8')
            f5 = open('meaningfulness_paivionorms.txt', 'r', encoding='utf-8')
            f6 = open('ageofacquisition.txt', 'r', encoding='utf-8')
        except IOError:
            print("file cannot be opened")
            exit()

        try:
            bnc = f.read().splitlines()
            mrc_familiarity = f1.read().splitlines()
            mrc_concreteness = f2.read().splitlines()
            mrc_imageability = f3.read().splitlines()
            mrc_meaningfulness_c = f4.read().splitlines()
            mrc_meaningfulness_p = f5.read().splitlines()
            mrc_ageofacquisition = f6.read().splitlines()
            os.chdir(mycwd)
        except IOError:
            print("Could Not Read From File.")
            exit()

        freqlist = collections.defaultdict()
        occurlist = collections.defaultdict()
        contentlist = collections.defaultdict()
        functionlist = collections.defaultdict()
        familiaritylist = collections.defaultdict()
        concretenesslist = collections.defaultdict()
        imageabilitylist = collections.defaultdict()
        ageofacquisitionlist = collections.defaultdict()
        meaningfulness_c_list = collections.defaultdict()
        meaningfulness_p_list = collections.defaultdict()

        for i in range (1, len(bnc)):
            freq, word, pos, occurrence = bnc[i].split()
            freqlist[word] = int(freq)
            occurlist[word] = int(occurrence)
            if pos=="aj0-av0" or pos=="aj0-nn1" or pos=="aj0-vvd" or pos=="aj0-vvg" or pos=="aj0-vvn" or pos=="nn1-np0" or pos=="nn1-vvb" or pos=="nn1-vvg" or pos=="nn2-vvz" or pos=="vvd-vvn" or pos=="aj0" or pos=="ajc" or pos=="ajs" or pos=="av0" or pos=="nn0" or pos=="nn1" or pos=="nn2" or pos=="np0" or pos=="vvb" or pos=="vvg" or pos=="vvi" or pos=="vvn" or pos=="vvz":
                contentlist[word] = int(freq)
            else:
                if pos!="pul" and pos!="pun" and pos!="puq" and pos!="pur" and pos!="unc" and pos!="zz0" and pos!="itj":
                    functionlist[word] = int(freq)

        for i in range (1, len(mrc_familiarity)):
            mrc_familiarity[i] = mrc_familiarity[i].strip()
            word, score = mrc_familiarity[i].split()
            familiaritylist[word] = int(score)

        for i in range (1, len(mrc_concreteness)):
            word, score = mrc_concreteness[i].split()
            concretenesslist[word] = int(score)

        for i in range (1, len(mrc_imageability)):
            word, score = mrc_imageability[i].split()
            imageabilitylist[word] = int(score)

        for i in range (1, len(mrc_ageofacquisition)):
            word, score = mrc_ageofacquisition[i].split()
            ageofacquisitionlist[word] = int(score)

        for i in range (1, len(mrc_meaningfulness_c)):
            word, score = mrc_meaningfulness_c[i].split()
            meaningfulness_c_list[word] = int(score)

        for i in range (1, len(mrc_meaningfulness_p)):
            word, score = mrc_meaningfulness_p[i].split()
            meaningfulness_p_list[word] = int(score)
    
        try:
            f.close()
            f1.close()
            f2.close()
            f3.close()
            f4.close()
            f5.close()
            f6.close()
        except IOError:
            print("Could Not Close File.")
            exit()
        
        stop_words = set(stopwords.words('english'))
        nostopwords_tokenized_text = []
        for words in tokenized_text:
            if words not in stop_words:
                nostopwords_tokenized_text.append(words)

        self.wordfrequencyall(tokenized_text, freqlist)
        self.wordfrequencycontent(tokenized_text, contentlist)
        self.wordfrequencyfunction(tokenized_text, functionlist)
        self.wordrange(tokenized_text, occurlist)
        self.wordfamiliarity(nostopwords_tokenized_text, familiaritylist)
        self.wordconcreteness(nostopwords_tokenized_text, concretenesslist)
        self.wordimageability(nostopwords_tokenized_text, imageabilitylist)
        self.ageofacquisition(nostopwords_tokenized_text, ageofacquisitionlist)
        self.wordmeaningfulness_c(nostopwords_tokenized_text, meaningfulness_c_list)
        self.wordmeaningfulness_p(nostopwords_tokenized_text, meaningfulness_p_list)
        pass


    def wordfrequencyall(self, tokenized_text, freqlist):
        self.wordfrequency_all = 0
        count = 0
        freqsum = 0
        for w in tokenized_text:
            if w in freqlist:
                freqsum += freqlist[w]
                count +=1
        
        if count == 0:
            wordfa = 0
        else:
            wordfa = float('{:.2f}'.format(freqsum/count))
        self.wordfrequency_all = wordfa
        pass

    def wordfrequencycontent(self, tokenized_text, contentlist):
        self.wordfrequency_content = 0
        count = 0
        freqsum = 0
        for w in tokenized_text:
            if w in contentlist:
                freqsum += contentlist[w]
                count +=1
        if count == 0:
            wordfc = 0
        else: 
            wordfc = float('{:.2f}'.format(freqsum/count))
        self.wordfrequency_content = wordfc
        pass

    def wordfrequencyfunction(self, tokenized_text, functionlist):
        self.wordfrequency_function = 0
        count = 0
        freqsum = 0
        for w in tokenized_text:
            if w in functionlist:
                freqsum += functionlist[w]
                count +=1
        if count == 0:
            wordff = 0
        else:
            wordff = float('{:.2f}'.format(freqsum/count))
        self.wordfrequency_function = wordff
        pass
    
    def wordrange(self, tokenized_text, occurlist):
        count = 0
        occursum = 0
        for w in tokenized_text:
            if w in occurlist:
                occursum += occurlist[w]
                count += 1
        if count == 0:
            wordrange = 0
        else:
            wordrange = float('{:.2f}'.format(occursum/count))
        self.wordrangescore = wordrange
        pass

    def wordfamiliarity(self,tokenized_text, scorelist):
        count = 0
        scoresum = 0
        for w in tokenized_text:
            if w.upper() in scorelist:
                scoresum += scorelist[w.upper()]
                count += 1
        if count == 0:
            familiarity = 0
        else:
            familiarity = float('{:.2f}'.format(scoresum/count))
        self.familiarityscore = familiarity
        pass

    def wordconcreteness(self,tokenized_text, scorelist):
        count = 0
        scoresum = 0
        for w in tokenized_text:
            if w.upper() in scorelist:
                scoresum += scorelist[w.upper()]
                count += 1
        if count == 0:
            concreteness = 0
        else:
            concreteness = float('{:.2f}'.format(scoresum/count))
        self.concretenessscore = concreteness
        pass
                    
    def wordimageability(self,tokenized_text, scorelist):
        count = 0
        scoresum = 0
        for w in tokenized_text:
            if w.upper() in scorelist:
                scoresum += scorelist[w.upper()]
                count += 1
        if count == 0:
            imageability = 0
        else:
            imageability = float('{:.2f}'.format(scoresum/count))
        self.imageabilityscore = imageability
        pass

    def wordmeaningfulness_c(self,tokenized_text, scorelist):
        count = 0
        scoresum = 0
        for w in tokenized_text:
            if w.upper() in scorelist:
                scoresum += scorelist[w.upper()]
                count += 1
        if count == 0:
            meaningfulness_c = 0
        else:
            meaningfulness_c = float('{:.2f}'.format(scoresum/count))
        self.meaningfulnesscscore = meaningfulness_c
        pass

    def wordmeaningfulness_p(self,tokenized_text, scorelist):
        count = 0
        scoresum = 0
        for w in tokenized_text:
            if w.upper() in scorelist:
                scoresum += scorelist[w.upper()]
                count += 1
        if count == 0:
            meaningfulness_p = 0
        else:
            meaningfulness_p = float('{:.2f}'.format(scoresum/count))
        self.meaningfulnesspscore = meaningfulness_p
        pass

    def ageofacquisition(self,tokenized_text, scorelist):
        count = 0
        scoresum = 0
        for w in tokenized_text:
            if w.upper() in scorelist:
                scoresum += scorelist[w.upper()]
                count += 1
        if count == 0:
            ageofacquisition = 0
        else:
            ageofacquisition = float('{:.2f}'.format(scoresum/count))
        self.ageofacquisitionscore = ageofacquisition
        pass
