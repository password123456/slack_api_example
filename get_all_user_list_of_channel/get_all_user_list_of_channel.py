__author__ = 'https://github.com/password123456/'
__version__ = '1.0.1-230201'

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


def get_user_list_of_channel(token, channel_id):
    client = WebClient(token=token)

    try:
        result = client.conversations_members(channel=channel_id)
        i = 0
        for user in result['members']:
            try:
                info = client.users_info(user=user).data
                if not info['user']['is_bot']:
                    i = i + 1

                    member_id = info['user']['id']
                    team_id = info['user']['team_id']
                    display_name = info['user']['name']
                    real_name = info['user']['real_name']
                    phone = info['user']['profile']['phone']
                    email = info['user']['profile']['email']

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

                    print(f'{i},{real_name},{display_name},{team_id},{member_id},{email},{phone}')
            except SlackApiError as e:
                print(f'{Bcolors.Yellow}- Api Error:: {e} {Bcolors.Endc}')
    except SlackApiError as e:
        print(f'{Bcolors.Yellow}- Api Error:: {e} {Bcolors.Endc}')

def main():
    bot_token = 'YOUR_BOT_TOKEN'
    channel = 'channel_id_you_want_to_know'

    get_user_list_of_channel(bot_token, channel)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- ::Exception:: Func:[{__name__.__name__}] '
              f'Line:[{sys.exc_info()[-1].tb_lineno}] [{type(e).__name__}] {e}{Bcolors.Endc}')

