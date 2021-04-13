from spacy.language import Language
from spacy.matcher import Matcher
from spacy.tokens import Token, Span, Doc


@Language.factory("resumext",
                  default_config={
                      "ent_types": list(),
                      "extension_name": "resumext",
                  },
                  )
class ResumeExtractor:
    def __init__(self,
                 nlp: Language,
                 name: str,
                 ent_types: list,
                 pattern: dict):
        """

        :param nlp:
        :param pattern:
        """

        Span.set_extension("resume_extract", default=[], force=True)
        self.nlp = nlp
        self.pattern = pattern
        self.matcher = Matcher(nlp.vocab)

        for k, v in self.pattern.items():
            patterns = v['patterns']
            self.matcher.add("_" + str(k), patterns)

    def __call__(self, doc):
        """

        :param doc:
        :return:
        """
        match = self.matcher(doc)
        for e in doc.ents:
            if e.label_ in self.pattern.keys():
                e._.resume_extract = self.get_match(
                    doc,
                    e,
                    match,
                    self.pattern[e.label_]["n"],
                    self.pattern[e.label_]["direction"]
                )
        return doc

    def get_match(self,doc,entity,match,n,direction):

        if type(n) == int:
            if direction  == 'left':



