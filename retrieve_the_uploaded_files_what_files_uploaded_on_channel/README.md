# Bot Token Scopes
- Two api are used.
- Bot must be join the channel on which you want to know informations.

1) https://api.slack.com/methods/conversations.history
2) https://api.slack.com/methods/users.info

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
