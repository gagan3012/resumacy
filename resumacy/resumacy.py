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
