# slack_example

![made-with-python][made-with-python]
![Python Versions][pyversion-button]

[pyversion-button]: https://img.shields.io/pypi/pyversions/Markdown.svg
[made-with-python]: https://img.shields.io/badge/Made%20with-Python-1f425f.svg

- Meaningless work on the slack


### How to set up
1. Install `slack-sdk`
```
# pip install slack_sdk 
```
2. or Install `requests`
```
# pip install requests
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

# Examples - python slack_sdk/requests
- [Retrieve the list of users who have joined on channel](https://github.com/password123456/slack_api_example/tree/main/retrieve_the_list_of_users_who_have_joined_on_channel)
- [Retrieve all users in slack workspace](https://github.com/password123456/slack_api_example/tree/main/retrieve_all_users_in_slack_workspace)
- [Retrieve the uploaded files what files uploaded on channel](https://github.com/password123456/slack_api_example/tree/main/retrieve_the_uploaded_files_what_files_uploaded_on_channel)
- [Bot sending direct message to user](https://github.com/password123456/slack_api_example/tree/main/bot_sending_direct_message_to_user)
- [Bot send a file to channel](https://github.com/password123456/slack_api_example/tree/main/send_a_file_to_the_channel)
- [Bot send a file to user as a direct_message](https://github.com/password123456/slack_api_example/tree/main/send_a_file_to_the_user_as_a_direct_message)
# And...
- If you find this helpful, please consider giving it a **"star"**:star2: to support further improvements.


## Reference Pages
[Slack API Application](https://api.slack.com/apps)

[Slack API Docs](http://www.slack.dev/python-slack-sdk)




