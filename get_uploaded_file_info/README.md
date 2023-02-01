# Bot Token Scopes
- Two api are used.

1) https://api.slack.com/methods/conversations.history

```
channels:history
groups:history
im:history
mpim:history
```

2) https://api.slack.com/methods/users.info
```
users:read 
users:read.email

:note:
Apps created after January 4th, 2017 must request both the users:read and users:read.email OAuth permission scopes to access the email field of user objects.
(default: not show email field) so, If not grant users:read.email, email field does not return.
```

## preview
```
- uploaded_at: 2023-02-01 14:06:30+09:00
- user_info: "k****6,mynameis,****@gmail.com,010-1111-1111"
- filename: 2101254.pdf
- type: pdf
- upload_preview: https://files.slack.com/files-pri/TB37064-F04M9GYES/2101254.pdf
- download_link: https://files.slack.com/files-pri/TB37064-F04M9GYES/download/2101254.pdf

- uploaded_at: 2023-02-01 14:01:12+09:00
- user_info: "k****6,mynameis,****@gmail.com,010-1111-1111"
- filename: blackbean.png
- type: png
- upload_preview: https://files.slack.com/files-pri/TBZ064-F04HRUVS8/blackbean.png
- download_link: https://files.slack.com/files-pri/TBZ064-F04HRUVS8/download/blackbean.png
```

## Reference Pages
- [Slack API Guide](https://api.slack.com/methods)
- [Python Slack Docs](http://www.slack.dev/python-slack-sdk)
