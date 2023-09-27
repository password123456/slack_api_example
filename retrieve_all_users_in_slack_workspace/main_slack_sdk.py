__author__ = 'https://github.com/password123456/'
__version__ = '1.0.2-230828'

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


def get_all_users_in_workspace(token):
    client = WebClient(token=token)

    try:
        # https://api.slack.com/methods/users.list
        # The 'limit' parameter should be adjusted to match your environment. Default 0 (unlimited)
        # The maximum number of user lists to return. Fewer than the requested number of items may be returned
        result = client.users_list(limit=100)
        i = 0
        for info in result['members']:
            # Exclude Bot Accounts
            if not info['id'] == 'USLACKBOT':
                if not info['is_bot']:
                    i = i + 1
                    member_id = info['id']
                    team_id = info['team_id']
                    display_name = info['profile']['display_name']
                    real_name = info['profile']['real_name']
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
    except SlackApiError as e:
        print(f'{Bcolors.Yellow}- Api Error:: {e} {Bcolors.Endc}')


def main():
    bot_token = 'slack_apps_oauth_token(bot_token)'
    get_all_users_in_workspace(bot_token)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(
            f'{Bcolors.Yellow}- ::Exception:: Func:[{__name__.__name__}] '
            f'Line:[{sys.exc_info()[-1].tb_lineno}] [{type(e).__name__}] {e}{Bcolors.Endc}')
        
