__author__ = 'https://github.com/password123456/'
__version__ = '1.0.0-231005'

# write in python requests syntax

import sys
import requests
import json


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


def conversations_open(headers, user_id):
    api_method = 'conversations.open'
    result = ''
    try:
        # https://api.slack.com/methods/conversations.open
        response = requests.get(
            f'https://slack.com/api/{api_method}?users={user_id}',
            headers=headers
        )
        result = response.json()
        if result['ok']:
            return result['channel']['id']

    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- Exception::{e} {Bcolors.Endc}')
    return result


def chat_post_message(headers, user_chat_id, message):
    api_method = 'chat.postMessage'
    result = ''
    try:
        # https://api.slack.com/methods/chat.postMessage
        response = requests.get(
            f'https://slack.com/api/{api_method}?channel={user_chat_id}&text={message}&as_user=true',
            headers=headers
        )
        result = response.text

    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- Exception::{e} {Bcolors.Endc}')
    return result


def main():
    token = 'slack_apps_oauth_token(bot_token)'
    user_id = 'user_id to sending message'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Authorization': f'Bearer {token}'
    }

    user_chat_id = conversations_open(headers, user_id)
    if user_chat_id:
        message = f'<@{user_id}> hello? good day to see you again:)'
        result = chat_post_message(headers, user_chat_id, message)
        data = json.loads(result)
        if data['ok']:
            print(data['message'])


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- ::Exception:: Func:[{__name__.__name__}] '
              f'Line:[{sys.exc_info()[-1].tb_lineno}] [{type(e).__name__}] {e}{Bcolors.Endc}')
