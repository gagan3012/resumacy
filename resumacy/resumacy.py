from spacy.language import Language
from spacy.matcher import Matcher
from spacy.tokens import Token, Span, Doc

from .pattern import ent_pat, pat


@Language.factory("resumext",
                  default_config={
                      "ent_types": list(),
                      "extension_name": "resumext",
