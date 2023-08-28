# Bot Token Scopes
- Two api are used.
- Bot must be join the channel on which you want to know informations.

1) https://api.slack.com/methods/conversations.open
2) https://api.slack.com/methods/chat.postMessage

## Remember
- If possible, please refrain from using chatPostMessage to deliver the message. You should initiate a conversation and send the message accordingly.


## Reference Pages
- [Slack API Guide](https://api.slack.com/methods)
- [Python Slack Docs](http://www.slack.dev/python-slack-sdk)
