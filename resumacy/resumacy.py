from spacy.language import Language
from spacy.matcher import Matcher
from spacy.tokens import Token, Span, Doc


@Language.factory("resumext")
class ResumeExtractor:
    def __init__(self, nlp: Language, pattern: dict):
        Span.set_extension("resume_extract", default=[], force=True)
        self.nlp = nlp
        self.pattern = pattern
        self.matcher = Matcher(nlp.vocab)

        for k, v in self.pattern.items():
            patterns = v['patterns']
            self.matcher.add("_" + str(k), patterns)

    def __call__(self,doc):
        
