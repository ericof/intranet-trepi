from plone.dexterity.content import Container
from plone.supermodel import model
from trepi.intranet import _
from zope import schema
from zope.interface import implementer


class IPessoa(model.Schema):
    """Definição de uma Pessoa."""

    cargo = schema.Choice(
        title=_("Cargo"),
        vocabulary="trepi.intranet.vocabulary.cargos",
        required=True,
    )


@implementer(IPessoa)
class Pessoa(Container):
    """Uma Pessoa colaboradora do TRE-PI."""
