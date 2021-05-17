from spacy.language import Language
from spacy.matcher import Matcher
from spacy.tokens import Token, Span, Doc

from .pattern import ent_pat, pat


@Language.factory("resumext",
                  default_config={
                      "ent_types": list(),
                      "extension_name": "resumext",
                  },
                  )
class ResumeExtractor:
    pattern = pat()
    ent_pattern = ent_pat()

    def __init__(self,
                 nlp: Language,
                 name: str,
                 ent_types: list):
        """

        :param nlp:
        :param pattern:
        """

        Span.set_extension("resume_extract", default=[], force=True)
        self.nlp = nlp
        self.pattern = pattern
        self.ent_types = ent_types
        self.ent_pattern = ent_pattern
        self.matcher = Matcher(nlp.vocab)

        for k, v in self.ent_pattern.items():
            patterns = v['patterns']
            self.matcher.add("_" + str(k), patterns)

    def res(self, doc):
        """

        :param doc:
        :return:
        """
        match = self.matcher(doc)
        common_elements = set(self.pattern.keys()).intersection(self.ent_types)
        for e in doc.ents:
            if e.label_ in common_elements:
                e._.resume_extract = self.get_match(
                    doc,
                    e,
                    match,
                    self.pattern[e.label_]["direction"],
                    self.pattern[e.label_]["n"]
                )
        return doc

    def get_match(self,
                  doc,
                  entity,
                  match,
                  direction,
                  n=1):
        """
        :param doc:
        :param entity:
        :param match:
        :param direction:
        :param n:
        :return:
        """

        if type(n) == int:
            if direction == "left":
                end_i = entity.start
                start_i = max(entity.start - n, 0)
            else:
                end_i = min(entity.end + (n - 1), len(doc))
                if direction == "right":
                    start_i = entity.end
                if direction == "both":
                    start_i = max(entity.start - n, 0)

        elif n == "sent":
            if direction == "right":
                start_i = entity.end
                end_i = entity.sent.end - 1
            if direction == "both":
                start_i = entity.sent.start
                end_i = entity.sent.end - 1
            if direction == "left":
                start_i = entity.sent.start
                end_i = entity.start

        else:
            raise ValueError(
                "If using pattern_match, expecting n to be an int or equal to 'sent'"
            )
