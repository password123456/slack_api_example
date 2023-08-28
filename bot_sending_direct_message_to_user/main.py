__author__ = 'https://github.com/password123456/'
__version__ = '1.0.0-230828'

import sys
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class Bcolors:
    Black = '\033[30m'
    Red = '\033[31m'
    Green = '\033[32m'
    Yellow = '\033[33m'
    Blue = '\033[34m'
    Magenta = '\033[35m'
    Cyan = '\033[36m'
    White = '\033[37m'
    Endc = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def conversations_open(bot_token, user_id):
    # https://api.slack.com/methods/conversations.open
    client = WebClient(token=bot_token)
    try:
        result = client.conversations_open(users=user_id)
        channel_id = result['channel']['id']
        if channel_id:
            return channel_id
        else:
            return None
    except SlackApiError as e:
        print(f'{Bcolors.Yellow}- Api Error:: {e} {Bcolors.Endc}')
        return None


def chat_post_message(bot_token, channel_id, message):
    # https://api.slack.com/methods/chat.postMessage
    client = WebClient(token=bot_token)
    try:
        result = client.chat_postMessage(token=bot_token, channel=channel_id, text=message, as_user=True)
        print(result)
    except SlackApiError as e:
        print(f'{Bcolors.Yellow}- Api Error:: {e} {Bcolors.Endc}')


def main():
    bot_token = 'slack_apps_oauth_token(bot_token)'
    user_id = 'User ID to which the bot can send direct messages.'
  
    conversation_id = conversations_open(bot_token, user_id)
    if conversation_id:
        message = f'<@{user_id}> hello my freiend.'
        chat_post_message(bot_token, conversation_id, message)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- ::Exception:: Func:[{__name__.__name__}] '
              f'Line:[{sys.exc_info()[-1].tb_lineno}] [{type(e).__name__}] {e}{Bcolors.Endc}')
