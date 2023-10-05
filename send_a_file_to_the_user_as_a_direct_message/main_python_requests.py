__author__ = 'https://github.com/password123456/'
__version__ = '1.0.0-231005'

# write in python requests syntax

import os
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


def files_upload(headers, channel_id, upload_file, upload_file_title):
    api_method = 'files.upload'
    result = ''
    try:
        # https://api.slack.com/methods/files.upload
        payload = {"channels": channel_id}
        readfile = open(upload_file, 'rb')
        file_upload = {"file": (upload_file_title, readfile)}

        response = requests.post(
            f'https://slack.com/api/{api_method}',
            files=file_upload,
            data=payload,
            headers=headers
        )

        result = response.json()
        if result['ok']:
            return result['file']['permalink']
        else:
            return None

    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- 11Exception::{e} {Bcolors.Endc}')
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


def file_is_not_empty(file_name):
    limit = 10
    f = os.stat(file_name).st_size
    if f >= limit:
        return True
    else:
        return False


def main():
    token = 'slack_apps_oauth_token(bot_token)'
    user_id = 'user_id to sending message'

    upload_file = f'{os.getcwd()}/your_upload_file.pdf'
    upload_file_title = upload_file.rsplit('/')[-1]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Authorization': f'Bearer {token}'
    }

    user_chat_id = conversations_open(headers, user_id)
    if user_chat_id:
        if file_is_not_empty(upload_file):
            uploaded_file_link = files_upload(headers, user_chat_id, upload_file, upload_file_title)
            if uploaded_file_link:
                # Display the uploaded file as a Markdown-style link, not an absolute file path.
                # <https://www.stackoverflow.com|link>
                message = f'<!channel> Hello Guys.\nThis is for you\n<{uploaded_file_link}|{upload_file_title}>'
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
