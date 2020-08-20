import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from lib.lexicalmetrics import Lexicalmetrics
from lib.readability import Readability
from lib.general_information import GeneralInformation
import string
from nltk.tokenize import word_tokenize

class Score:
    def __init__(self):
        self.lex = Lexicalmetrics()
        self.readability = Readability()
        self.general = GeneralInformation()

    def scale_freq(self, score):
        scaled = (1 - ((score-1)/5776384)) * 100
        return scaled

    def scale_familiarity(self, score):
        scaled = ((score - 101)/(657-101)) * 100
        return scaled

    def scale_wordrange(self,score):
        scaled = (1-((score - 1)/(3209 - 1))) * 100
        return scaled

    def evaluation(self, text):
        nopunc_text = text.translate(str.maketrans('','',string.punctuation))
        tokenized_text = word_tokenize(nopunc_text)

        self.general.generate_score(text)
        self.lex.generate_score(tokenized_text)
        self.readability.generate_score(text)

        metrics = dict()
        general = dict()
        readability = dict()
        lexical = dict()
        writing = dict()
        
        general['language'] = self.general.language
        general['sentence_length'] = self.general.sentence_length
        general['average_sentence_length'] = self.general.avgsentence
        general['word_length'] = self.general.word_length
        general['average_word_length'] = self.general.avgword
        general['unique_words_length'] = self.general.unique_words_length
        general['characters_length'] = self.general.characters_length
        general['lexical_diversity'] = self.general.lexical_diversity
        general['part_of_speech'] = self.general.partofspeech
        general['part_of_speech_percentage'] = self.general.partofspeechpercentage

        readability['flesch_reading_ease'] = self.readability.flesch_reading_grade
        readability['flesch_reading_grade_consensus'] = self.readability.flesch_reading_grade_consensus
        readability['dale_chall_grade'] = self.readability.dale_chall_grade
        readability['flesch_kincaid_grade'] = self.readability.flesch_kincaid_grade
        readability['smog_grade'] = self.readability.smog_grade
        readability['ari_grade'] = self.readability.ari_grade
        readability['coleman_liau_grade'] = self.readability.coleman_liau_grade

        lexical['wordfrequency_all'] = self.scale_freq(self.lex.wordfrequency_all)
        lexical['wordfrequency_content'] = self.lex.wordfrequency_content
        lexical['wordfrequency_function'] = self.lex.wordfrequency_function
        lexical['wordrangescore'] = self.scale_wordrange(self.lex.wordrangescore)
        lexical['familiarityscore'] = self.scale_familiarity(self.lex.familiarityscore)
        lexical['concretenessscore'] = self.lex.concretenessscore
        lexical['imagabilityscore'] = self.lex.imagabilityscore
        lexical['meaningfulnesscscore'] = self.lex.meaningfulnesscscore
        lexical['meaningfulnesspscore'] = self.lex.meaningfulnesspscore
        lexical['ageofacquisitionscore'] = self.lex.ageofacquisitionscore

        writing['top_8_named_entity'] = self.general.namedentity
        writing['top_10_phrases'] = self.general.topphrases
        writing['phrases_wordcloud'] = self.general.topphraseswordcloud
        writing['keywords'] = self.general.keywords

        metrics['general'] = general
        metrics['readability'] = readability
        metrics['lexical'] = lexical
        metrics['writing'] = writing
        return metrics


if __name__ == "__main__":
    score()