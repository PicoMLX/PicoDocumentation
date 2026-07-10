import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Introduction',
      items: ['user-guide/about-this-manual', 'user-guide/quick-start-roadmap'],
    },
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        'user-guide/getting-started/install-and-run-pico-ai-server',
        'user-guide/getting-started/configure-settings',
        'user-guide/getting-started/connect-a-client',
      ],
    },
    {
      type: 'category',
      label: 'Networking & Sharing',
      items: [
        'user-guide/networking/lan-sharing-basics',
        'user-guide/networking/hostnames-ip-addresses-and-what-to-copy',
        'user-guide/networking/bonjour-discovery',
      ],
    },
    {
      type: 'category',
      label: 'WebUI',
      items: [
        'user-guide/webui/use-the-webui',
        'user-guide/webui/open-web-chat-and-launch-client-apps',
      ],
    },
    {
      type: 'category',
      label: 'MCP & Tools',
      items: ['user-guide/enable-built-in-tools'],
    },
    {
      type: 'category',
      label: 'Reference',
      items: [
        'reference/endpoint-summary',
        'reference/models/models-api',
        'reference/chat/chat-api',
        'reference/openresponses-api',
        'reference/embeddings/embeddings-api',
      ],
    },
  ],
};

export default sidebars;
