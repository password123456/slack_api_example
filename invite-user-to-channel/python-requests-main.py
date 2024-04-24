__author__ = 'https://github.com/password123456/'
__date__ = '2024.04.24'
__version__ = '1.0.0'
__status__ = 'Production'

# write in python requests syntax

import os
import sys
import requests


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


def catch_try_error(error, func_name):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_details = {
        'filename': os.path.realpath(__file__),
        'line_number': exc_traceback.tb_lineno,
        'func_name': func_name,
        'exception': str(error)
    }
    message = (
        f'{traceback_details["filename"]}\n'
        f' - [func]: {traceback_details["func_name"]}\n'
        f' - [line_num]: {traceback_details["line_number"]}\n'
        f' - [exception]: {traceback_details["exception"]}\n'
    )
    return message


def catch_http_error(response, func_name):
    traceback_details = {
        'filename': os.path.realpath(__file__),
        'func_name': func_name,
        'status_code': response.status_code,
        'reason': response.reason,
        'content': response.content.decode('utf-8')
    }
    message = (
        f'{traceback_details["filename"]}\n'
        f' - [func]: {traceback_details["func_name"]}\n'
        f' - [status_code]: {traceback_details["status_code"]}\n'
        f' - [reason]: {traceback_details["reason"]}\n'
        f' - [content]: {traceback_details["content"]}\n'
    )
    return message


def invite_user_to_channel(token, channel, users, is_multiple):
    api_method = 'conversations.invite'

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
               'Authorization': f'Bearer {token}'
               }

    # https://api.slack.com/methods/conversations.invite
    params = {
        'channel': channel,
        'users': users,
        'force': is_multiple
    }

    try:
        response = requests.post(
            f'https://slack.com/api/{api_method}',
            headers=headers,
            data=params,
            verify=True
        )
        result = response.json()
        if response.status_code == 200:
            if result['ok']:
                print(result['channel'])
            else:
                print(result)
        else:
            message = catch_http_error(response, invite_user_to_channel.__name__)
            print(f'{Bcolors.Yellow}[-] Error: {message} {Bcolors.Endc}')
    except Exception as error:
        message = catch_try_error(error, invite_user_to_channel.__name__)
        print(f'{Bcolors.Yellow}[-] Error: {message} {Bcolors.Endc}')


def main():
    token = 'slack-apps-oauth-token(bot_token)'  # e.g. xoxb~~~
    channel = 'channel_id-to-invite'             # e.g. C05~~~
    users = ['users-to-invite']                  # e.g. U05~~~
    # If there are more than two users to invite, please include them as parameters separated by commas.
    # and is_multiple flag set to true
    # e.g. C05~~~,C05~~~
  
    users = ','.join(users)
    is_multiple = False
    if len(users) >= 2:
        is_multiple = True
    invite_user_to_channel(token, channel, users, is_multiple)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- ::Exception:: Func:[{__name__.__name__}] '
              f'Line:[{sys.exc_info()[-1].tb_lineno}] [{type(e).__name__}] {e}{Bcolors.Endc}')
