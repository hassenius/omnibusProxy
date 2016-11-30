## Netcool Omnibus Proxy

When integrating with Slack (and potentially other webhooks) that require HTTPS this proxy will terminate the SSL and forward
to the URL set in the manifest.yaml file
Originally built for Slack integration, so also strips away everything else than the content of the 'payload' part of the JSON received from
Slack

