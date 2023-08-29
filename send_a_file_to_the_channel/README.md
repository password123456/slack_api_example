# Bot Token Scopes
- Two api are used.
- Bot must be join the channel

1) https://api.slack.com/methods/files.upload
2) https://api.slack.com/methods/chat.postMessage

## remember
Uploading a file cannot be accomplished using a single files.upload API.

1) Upload the file using the files.upload API.
2) Retrieve the link to the uploaded file from the result.
3) After obtaining the link to the file, use chat.postMessage to send the uploaded file to the channel in text format.

## preview
<img src=https://github.com/password123456/slack_api_example/blob/main/send_a_file_to_the_channel/preview.png>

## etc
- If you get a NOT_IN_CHANNEL error in the API response.
```
{ "ok": false, "error": "not_in_channel" }
```

solution 1
- Open channel settings > Click on the Integrations tab > Click Add apps and check out your custom app joined the channel

solution 2
- Give access to the bot to all channels by adding workspace wide scope, for example, chat:write.public. Depends on your needs and security requirements.
  
solution 3
- To access the channel chat from API specify Incoming webhook. Slack will generate a unique URL with the token per each channel. check out channel id


## Reference Pages
- [Slack API Guide](https://api.slack.com/methods)
- [Python Slack Docs](http://www.slack.dev/python-slack-sdk)
