from plone import api
from plone.restapi.services import Service
from trepi.intranet import logger
from trepi.intranet.services.clima import openmeteo


class ClimaGet(Service):
    @property
    def coordinates(self) -> tuple:
        """Retorna latitude e longitude do TRE-PI."""
        return (-5.083092355681725, -42.79922375672997)

    @property
    def timezone(self) -> str:
        return api.portal.get_registry_record("plone.portal_timezone")

    def reply(self):
        """Retorna os dados de clima do TRE-PI."""
        # Obtem a url do portal
        portal = api.portal.get()
        portal_url = portal.absolute_url()

        # Obtem latitude e longitude
        latitude, longitude = self.coordinates
        # Obtem timezone
        timezone = self.timezone
        # Acessa dados do clima da openmeteo
        logger.info("Acessa dados do clima")
        dados = openmeteo.dados_clima(latitude, longitude, timezone)
        # Adiciona o @id (url deste serviço) aos dados
        dados["@id"] = f"{portal_url}/@clima"
        logger.info("Retorna dados do clima")
        return dados
