from spacy.language import Language
from spacy.matcher import Matcher
from spacy.tokens import Token, Span, Doc

@Language.factory("resumacy")
class ResumeExtractor:
    def __init__(self, nlp: Language):
        
