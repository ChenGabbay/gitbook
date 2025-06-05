---
description: >-
  The Box plugin allows you to upload custom files as evidence using a shared
  link.
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# hibob plugin

## Plugin details

## What you get from this plugin

## Plugin setup

Access to content is further restricted by the user's permission and Access Token used.

### **Connecting to Box**

From within the anecdotes Plugin page, you can initiate the plugin connection to your Box account.

1. From the Box plugin page in anecdotes, click on **Connect Plugin**.

<figure><img src="../.gitbook/assets/image%20(391).png" alt="" width="375"><figcaption></figcaption></figure>

2.  You will be redirected to box's OAuth authorization page, where you can select **Grant access to Box**:\\

    <figure><img src="../.gitbook/assets/image%20(409).png" alt=""><figcaption></figcaption></figure>

Anecdotes will then test the connection to your Box account.

Optionally, you may later reconfigure the anecdotes plugin permissions here by clicking _Deny access to Box._

### Linking to a shared Box file

Once the plugin is connected, navigate to the file you want to link from within Box, and provide anecdotes a shared link to that file.

1.  Within Box, mouseover the file you wish to share, and select the **Share** icon. You can also use the **Copy Shared Link** icon.\\

    <figure><img src="../.gitbook/assets/image%20(394).png" alt=""><figcaption></figcaption></figure>
2.  Create a _Share link_ for the file you want to upload as evidence, and copy the path to your clipboard.\\

    <figure><img src="../.gitbook/assets/image%20(393).png" alt="" width="241"><figcaption></figcaption></figure>
3.  Within a relevant anecdotes page (such as within a Requirement's Control), select **Collect evidence**, then **Box**.\\

    <figure><img src="../.gitbook/assets/image%20(395).png" alt=""><figcaption></figcaption></figure>
4.  Provide the shared link within the _Link to the Box_ input form, and press **Connect link**:\\

    <figure><img src="../.gitbook/assets/image%20(396).png" alt="" width="311"><figcaption></figcaption></figure>
5.  Specify how you want to add the custom evidence: to all frameworks, only this framework, or only to the given control. Select **Add evidence**.\\

    <figure><img src="../.gitbook/assets/image%20(412).png" alt="" width="375"><figcaption></figcaption></figure>
6.  If successful, anecdotes will display _Evidence was linked successfully to the requirement_. Optionally, you may revisit the Plugins page to review any logs.\\

    <figure><img src="../.gitbook/assets/image%20(407).png" alt="" width="335"><figcaption></figcaption></figure>

## FAQs

_Are linked files updated after they are initially collected?_

Yes, linked evidence will be gathered as a new version each time the plugin runs, weekly.

_How can I review the anecdotes integration from within Box?_

From within the Box integrations page, select _My Integrations_, and you will see the Anecdotes app listed.
