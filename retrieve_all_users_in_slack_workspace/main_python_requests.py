__author__ = 'https://github.com/password123456/'
__version__ = '1.0.0-230927'

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


def lookup_users_list(headers):
    api_method = 'users.list'
    limit = 400
    result = ''
    try:
        # https://api.slack.com/methods/users.info
        response = requests.get(
            f'https://slack.com/api/{api_method}?limit={limit}',
            headers=headers
        )
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

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Authorization': f'Bearer {token}'
    }

    result = lookup_users_list(headers)
    users_info = json.loads(result)
    i = 0
    if users_info['ok']:
        for info in users_info['members']:
            # Exclude Bot Accounts
            if not info['id'] == 'USLACKBOT':
                if not info['is_bot']:
                    i = i + 1
                    member_id = get_value_or_null(info.get('id'))
                    team_id = get_value_or_null(info.get('team_id'))
                    display_name = get_value_or_null(info['profile'].get('display_name'))
                    real_name = get_value_or_null(info['profile'].get('real_name'))
                    mobile = get_value_or_null(info['profile'].get('phone'))
                    email = get_value_or_null(info['profile'].get('email'))

                    print(f'{i},{real_name},{display_name},{member_id},{team_id},{email},{mobile}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- ::Exception:: Func:[{__name__.__name__}] '
              f'Line:[{sys.exc_info()[-1].tb_lineno}] [{type(e).__name__}] {e}{Bcolors.Endc}')
