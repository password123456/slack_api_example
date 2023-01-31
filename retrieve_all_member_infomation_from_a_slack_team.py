__author__ = 'https://github.com/password123456/'
__version__ = '1.0.0-230131'

import logging
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


def save_users(users_array):
    i = 0
    for info in users_array:
        #print(info)
        if not info['id'] == 'USLACKBOT':
            if not info['is_bot']:
                i = i + 1
                member_id = info['id']
                team_id = info['team_id']
                display_name = info['name']
                real_name = info['real_name']
                phone = info['profile']['phone']
                email = info['profile']['email']

                if not member_id:
                    member_id = 'null'
                elif not team_id:
                    team_id = 'null'
                elif not display_name:
                    display_name = 'null'
                elif not real_name:
                    real_name = 'null'
                elif not phone:
                    phone = 'null'
                elif not email:
                    email = 'null'

                print(f'{i},{real_name},{display_name},{team_id},{email},{member_id},{phone}')


def main():
    # Require Package slack-sdk
    # pip install slack-sdk
    
    slack_api_bot_token = f'YOUR_BOT_TOKEn'

    client = WebClient(token=slack_api_bot_token)
    logger = logging.getLogger(__name__)

    try:
        result = client.users_list()
        save_users(result["members"])
    except SlackApiError as e:
        logger.error("Error creating conversation: {}".format(e))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(
            f'{Bcolors.Yellow}- ::Exception:: Func:[{__name__.__name__}] Line:[{sys.exc_info()[-1].tb_lineno}] [{type(e).__name__}] {e}{Bcolors.Endc}')



