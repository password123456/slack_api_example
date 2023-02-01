# Bot Token Scopes
- Two api are used. That's all
- bot don't have to join the channel that you want to know.

1) https://api.slack.com/methods/conversations.members

```
channels:read
groups:read
im:read
mpim:read (optional)
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
Personal information is included, so pass the preview.:)
```

## Reference Pages
- [Slack API Guide](https://api.slack.com/methods)
- [Python Slack Docs](http://www.slack.dev/python-slack-sdk)
