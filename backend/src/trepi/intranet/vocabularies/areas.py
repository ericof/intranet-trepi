from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory


@provider(IVocabularyFactory)
def vocab_areas(context) -> StaticCatalogVocabulary:
    """Áreas do TRE-PI."""
    return StaticCatalogVocabulary({
        "portal_type": ["Area"],
        "sort_on": "sortable_title",
    })
