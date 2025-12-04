from AccessControl import Unauthorized
from plone import api
from plone.dexterity.fti import DexterityFTI
from trepi.intranet.content.area import Area
from zope.component import createObject

import pytest


CONTENT_TYPE = "Area"


@pytest.fixture
def area_payload() -> dict:
    """Return a payload to create a new area."""
    return {
        "type": "Area",
        "id": "ti",
        "title": "Tecnologia da Informação",
        "description": ("Área responsável por TI"),
        "email": "ti@tre-pi.jus.br",
        "telefone": "(61) 3210.1234",
    }


@pytest.fixture
def area(portal, area_payload) -> Area:
    """Cria um objeto to tipo Area na raiz do Portal."""
    with api.env.adopt_roles(["Manager"]):
        area = api.content.create(
            container=portal,
            **area_payload,
        )
    return area


class TestArea:
    @pytest.fixture(autouse=True)
    def _setup(self, get_fti, portal):
        self.fti = get_fti(CONTENT_TYPE)
        self.portal = portal

    def test_fti(self):
        assert isinstance(self.fti, DexterityFTI)

    def test_factory(self):
        factory = self.fti.factory
        obj = createObject(factory)
        assert obj is not None
        assert isinstance(obj, Area)

    @pytest.mark.parametrize(
        "behavior",
        [
            "plone.basic",
            "plone.namefromtitle",
            "plone.shortname",
            "plone.excludefromnavigation",
            "trepi.intranet.behavior.contato",
            "trepi.intranet.behavior.endereco",
            "plone.versioning",
            "volto.blocks",
            "plone.constraintypes",
            "volto.preview_image",
        ],
    )
    def test_has_behavior(self, get_behaviors, behavior):
        assert behavior in get_behaviors(CONTENT_TYPE)

    @pytest.mark.parametrize(
        "role,allowed",
        [
            ("Manager", True),
            ("Site Administrator", True),
            ("Editor", False),
            ("Reviewer", False),
            ("Contributor", False),
            ("Reader", False),
        ],
    )
    def test_create(self, area_payload, role: str, allowed: bool):
        with api.env.adopt_roles([role]):
            if allowed:
                content = api.content.create(container=self.portal, **area_payload)
                assert content.portal_type == CONTENT_TYPE
                assert isinstance(content, Area)
            else:
                with pytest.raises(Unauthorized):
                    api.content.create(container=self.portal, **area_payload)

    def test_subscriber_added_with_description_value(self, area_payload):
        container = self.portal
        with api.env.adopt_roles(["Manager"]):
            area = api.content.create(
                container=container,
                **area_payload,
            )
        assert area.exclude_from_nav is False

    def test_subscriber_added_without_description_value(self, area_payload):
        from copy import deepcopy

        container = self.portal
        with api.env.adopt_roles(["Manager"]):
            payload = deepcopy(area_payload)
            payload["description"] = ""
            area = api.content.create(container=container, **payload)
        assert area.exclude_from_nav is True

    def test_subscriber_modified(self, area):
        """Testa o subscriber de modificação do Area.

        O parametro `area` é um fixture que cria um objeto Area com
        descrição preenchida. (ou seja, com exclude_from_nav=False)
        """
        # Importamos os módulos necessários para disparar o evento de modificação
        from zope.event import notify
        from zope.lifecycleevent import ObjectModifiedEvent

        # Após criação, com a descrição preenchida, o campo exclude_from_nav
        # deve estar como False
        assert area.exclude_from_nav is False

        # Agora vamos alterar a descrição para uma string vazia
        area.description = ""

        # Disparamos o evento de modificação
        notify(ObjectModifiedEvent(area))

        # Após a modificação, o campo exclude_from_nav deve ser atualizado para True
        assert area.exclude_from_nav is True

        # Alteramos a descrição novamente para uma string não vazia
        area.description = "Nova descrição"

        # Disparamos o evento de modificação
        notify(ObjectModifiedEvent(area))

        # Após a modificação, o campo exclude_from_nav deve ser atualizado para False
        assert area.exclude_from_nav is False
