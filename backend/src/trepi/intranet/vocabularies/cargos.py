from trepi.intranet import _
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


OPCOES = [
    ("servidor", _("Servidor")),
    ("terceiro", _("Terceirizado")),
]


@provider(IVocabularyFactory)
def vocab_cargos(context) -> SimpleVocabulary:
    """Cargos da estrutura do TRE-PI."""
    terms = []
    for token, title in OPCOES:
        terms.append(SimpleTerm(token, token, title))
    return SimpleVocabulary(terms)
