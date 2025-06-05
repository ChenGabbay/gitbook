---
description: How to connect Grafana OSS Plugin
---

# Grafana OSS Plugin

{% include "../../.gitbook/includes/plugins-basic-information.md" %}



<details>

<summary>Automated evidence collected and their required permissions</summary>

Grafana OSS - List of users per organization

* **permission**:  Grafana Admin- ( need fixed:roles:reader which exist only in Grafana Admin)

Grafana OSS - List of SSO configuration

* **permission**: Grafana Admin- ( need fixed:settings:reader which exist only in Grafana Admin)

Grafana OSS - List of teams and their members&#x20;

* **permission**: Grafana Admin- ( need fixed:teams:reader which exist only in Grafana Admin)

</details>

## Pre-requisites <a href="#h_ecf1afd25b" id="h_ecf1afd25b"></a>

Grafana OSS is installed inside a private network. Therefore, you will need to first [configure a connector ](../../technical-setup/connectors/how-to-configure-anecdotes-connector-with-docker.md)in order to integrate it with our platform. anecdotes' connector helps you integrate new plugins from your private network environment to anecdotes' platform by creating a secure encrypted tunnel.



## How to connect Grafana OSS plugin <a href="#h_6b50883117" id="h_6b50883117"></a>

In order to connect Grafana OSS plugin, you'll have to provide:

* Username - The user used to connect to Grafana OSS.
* Password - The password of the user
* Hostname - The hostname used to access Grafana OSS .
* Port



## Important :

You should grant Admin permissions to collect all evidence, as only Admin access allows reading all evidence data.

{% include "../../.gitbook/includes/required-plugin-permissions.md" %}

\


<figure><img src="../../.gitbook/assets/image (434).png" alt=""><figcaption></figcaption></figure>
