__author__ = 'https://github.com/password123456/'
__version__ = '1.0.0-231005'

# write in python requests syntax

import os
import sys
import requests
import json
from datetime import datetime


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


def lookup_users_info(headers, user_id):
    api_method = 'users.info'
    result = ''
    try:
        # https://api.slack.com/methods/users.info
        response = requests.get(
            f'https://slack.com/api/{api_method}?user={user_id}',
            headers=headers
        )
        # result = response.json()
        result = response.text

    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- Exception::{e} {Bcolors.Endc}')
    return result


def lookup_conversations_history(headers, channel_id):
    api_method = 'conversations.history'
    limit = 400
    result = ''
    try:
        # https://api.slack.com/methods/conversations.history
        response = requests.get(
            f'https://slack.com/api/{api_method}?channel={channel_id}&limit={limit}&pretty=1',
            headers=headers
        )
        # result = response.json()
        result = response.text

    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- Exception::{e} {Bcolors.Endc}')
    return result


def get_value_or_null(value):
    return 'null' if not value else value


def main():
    token = 'slack_apps_oauth_token(bot_token)'
    channel_id = 'Channel number'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Authorization': f'Bearer {token}'
    }

    result = lookup_conversations_history(headers, channel_id)
    data = json.loads(result)
    i = 0
    if data['ok']:
        conversation_history = data['messages']
        for block in conversation_history:
            if 'files' in block.keys():
                i = i + 1
                for file_list in block['files']:
                    f_upload_user = file_list['user']
                    f_upload_user_info = lookup_users_info(headers, f_upload_user)
                    f_user_data = json.loads(f_upload_user_info)

                    if not f_user_data:
                        upload_user = 'User not exists'
                    else:
                        user_info = f_user_data['user']
                        display_name = get_value_or_null(user_info.get('name'))
                        real_name = get_value_or_null(user_info.get('real_name'))
                        mobile = get_value_or_null(user_info['profile'].get('phone'))
                        email = get_value_or_null(user_info['profile'].get('email'))
                        upload_user = f'{display_name},{real_name},{mobile},{email}'

                    upload_time = file_list['timestamp']
                    record_date = datetime.strptime(str(datetime.fromtimestamp(upload_time, tz=None)),
                                                    '%Y-%m-%d %H:%M:%S')
                    local_timezone = datetime.now().astimezone().tzinfo
                    local_upload_time = record_date.astimezone(local_timezone)

                    upload_filename = file_list['title']
                    upload_filetype = file_list['filetype']
                    upload_file_preview = file_list['url_private']
                    file_download_url = file_list['url_private_download']

                    result = f'- created_at: {local_upload_time}\n- user: {upload_user}\n' \
                             f'- filename: {upload_filename}\n- type: {upload_filetype}\n' \
                             f'- file_preview: {upload_file_preview}\n- file_download: {file_download_url}\n'

                    print(result)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- ::Exception:: Func:[{__name__.__name__}] '
              f'Line:[{sys.exc_info()[-1].tb_lineno}] [{type(e).__name__}] {e}{Bcolors.Endc}')
