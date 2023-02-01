# slack_example

![made-with-python][made-with-python]
![Python Versions][pyversion-button]
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fpassword123456%2Fpy_certificate_extractor&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

[pyversion-button]: https://img.shields.io/pypi/pyversions/Markdown.svg
[made-with-python]: https://img.shields.io/badge/Made%20with-Python-1f425f.svg

- Meaningless work on the slack


## How to set up
1. Install `slack-sdk` library
```
(user) $ pip install slack_sdk 
```

2. Create Slack application bot and Set authorization scopes

e.g) if you want to know uploaded file information in a Specific channel, grant these scope to the Bot.

Two Slack API are used.
```
1) https://api.slack.com/methods/conversations.history

channels:history
groups:history
im:history
mpim:history

2) https://api.slack.com/methods/users.info

users:read 
users:read.email

:note:
Apps created after January 4th, 2017 must request both the users:read and users:read.email OAuth permission scopes to access the email field of user objects.
(default: not show email field) so, If not grant users:read.email, email field does not return.
```

Refer to a API guide [link](https://api.slack.com/methods)


# Code example
(1) [send webhook with markdown message](https://github.com/password123456/slack_api_example/tree/main/send_webhook_with_markdown)

(2) [get list of all member of the specific channel](https://github.com/password123456/slack_api_example/tree/main/get_all_user_list_of_channel)

(3) [get list of all member of the whole workspace](https://github.com/password123456/slack_api_example/tree/main/get_all_user_list_of_the_team)

(4) [get list of uploaded file, user information on the specific channel](https://github.com/password123456/slack_api_example/tree/main/get_uploaded_file_info)



## Reference Pages
[Slack API Application](https://api.slack.com/apps)

[Slack API Docs](http://www.slack.dev/python-slack-sdk)




