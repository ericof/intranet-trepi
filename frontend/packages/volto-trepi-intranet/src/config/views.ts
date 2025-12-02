import type { ConfigType } from '@plone/registry';
import AreaView from 'volto-trepi-intranet/components/Views/AreaView';
import PessoaView from 'volto-trepi-intranet/components/Views/PessoaView';

export default function install(config: ConfigType) {
  // Registra Visoes padrao para tipos de conteúdo
  config.views.contentTypesViews = {
    ...config.views.contentTypesViews,
    Area: AreaView,
    Pessoa: PessoaView,
  };
  return config;
}
