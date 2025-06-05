---
description: How to connect Grafana Plugin
---

# Grafana Plugin



{% hint style="success" %}
&#x20;Multiple accounts - enables users to [connect more than one account. ](../cloud-infrastructure/using-multiple-accounts-in-anecdotes.md)
{% endhint %}

<details>

<summary>Automated evidence collected</summary>

Grafana OSS - List of users per organization

permission: &#x20;

Grafana OSS - List of SSO configuration

Grafana OSS - List of teams and their members&#x20;

</details>

<details>

<summary>Required permissions</summary>

*   **Users**

    Read only access to Grafana's users and roles.
*   **OnCall Alerts**

    Read only access to Grafana's OnCall alerts.

</details>

## How to connect Grafana plugin <a href="#h_6b50883117" id="h_6b50883117"></a>

In order to connect Grafana plugin, you'll have to provide:

* Authentication Method
* Organization Name / Organization URL
* API Token
* Grafana OnCall API Token _(optional)_
* Grafana OnCall API URL _(optional)_

### Select your Authentication Method

Select the appropriate authentication method based on your setup. If you're using Grafana Cloud, choose the **"Grafana"** authentication option. If you're using a Self-Hosted instance, choose the **"Grafana - Self-Hosted"** authentication option.

### How to find your Organization Name

{% hint style="info" %}
If your Grafana instance is Self-Hosted, you need to provide the Org URL instead. See the explanation below for details.
{% endhint %}

Your organization name is the name you see in the URL when accessing the Grafana Cloud account, type the organization name in the Grafana plugin page at anecdotes.

<figure><img src="https://downloads.intercomcdn.com/i/o/578269813/87b772938614759bc95d454b/image.png" alt=""><figcaption></figcaption></figure>

Alternatively, you can sign in to your Grafana Cloud Portal as an admin user (using [this link](https://grafana.com/auth/sign-in/?tech=target\&plcmt=top-nav\&cta=A-myaccount)) and view your organization name at the top-left side of the screen.

<figure><img src="https://downloads.intercomcdn.com/i/o/578270861/62873ce842fc66791438d419/Screen+Shot+2022-09-11+at+17.20.58.png" alt=""><figcaption></figcaption></figure>

### How to find your Organization Name

{% hint style="info" %}
Only relevant for Self-Hosted Grafana.
{% endhint %}

Your organization URL is the beginning of the URL you see in the URL when accessing the Grafana Self-Hosted account.&#x20;

For example - "https://anecdotes.grafana.net"

Type the organization URL in the Grafana plugin page at anecdotes.

### How to create an API Token (for Grafana Enterprise/Grafana Cloud Adavanced Plans):

1.  In your, Grafana Cloud account navigate to the Administration tab.\


    [![](https://downloads.intercomcdn.com/i/o/711336311/98843c70e566834de3d5afc1/image.png)](https://downloads.intercomcdn.com/i/o/711336311/98843c70e566834de3d5afc1/image.png)

    \

2. Click on Service accounts then click on Add service account
3. Give the service account and indicative name and search for the role user viewer
4. If you are using also Grafana OnCall add the permissions:
   * Grafana OnCall Alert Groups (read)
   * Grafana OnCall Integrations (read)\

5. Click Create
6. On the newly created service account click on Add service account token
7.  Give the token a display name, then click on Generate token\


    <figure><img src="https://downloads.intercomcdn.com/i/o/711354836/ff6a1dd3e667b0d30ab54ae0/image.png" alt=""><figcaption></figcaption></figure>
8. Copy the API token and save it in a secure place, you will not be able to see it again once the window is closed.
9. Paste the API token to the relevant field in the Grafana plugin page at anecdotes.\


### How to create an API Token (for other Grafana plans):

In other Grafana subscriptions, it isn't possible to create a fine-grained token, therefore you will need to create a token that has Admin permissions, to do that you will need to follow the steps in the previous section but grant Admin permissions instead.\


### How to create a Grafana OnCall API Token and get the API URL

1.  From the Grafana Cloud platform, navigate to Grafana OnCall and click on Settings.



    <figure><img src="https://downloads.intercomcdn.com/i/o/578273005/a83f7ec8aefea72b9c7aaa6e/image.png" alt=""><figcaption></figcaption></figure>
2. Copy the API URL to the relevant field in the Grafana plugin page at anecdotes.\

3.  On the right side of the screen click on Create.\


    <figure><img src="https://downloads.intercomcdn.com/i/o/578273480/514a714b1e9bdf58c005d855/image.png" alt=""><figcaption></figcaption></figure>
4. Give the API Token a name and click Create.\

5. Copy the token and save it in a secure place, you will not be able to see it again once the window is closed.\

6. Paste the API token to the relevant field in the Grafana plugin page at anecdotes.
