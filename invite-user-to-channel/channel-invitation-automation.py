"""
This is an automated code that retrieves the user lists from two channels, A and B. 

It collects the user list from channel B that is not present in channel A, and automatically invites them to channel A.

It's similar to a LEFT JOIN in SQL. It compares the user lists from two channels, A and B. 
Then, it collects the user list from channel B that is not present in channel A, and automatically invites them to channel A.
"""

__author__ = 'https://github.com/password123456/'
__date__ = '2024.04.25'
__version__ = '1.0.0'
__status__ = 'Production'

import os
import sys
from datetime import datetime
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


def catch_try_error(error, func_name):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_details = {
        'filename': os.path.realpath(__file__),
        'line_num': exc_traceback.tb_lineno,
        'func_name': func_name,
        'exception': str(error)
    }
    message = (
        f'{traceback_details["filename"]}\n\n'
        f'- [func]: {traceback_details["func_name"]}\n'
        f'- [line_num]: {traceback_details["line_num"]}\n'
        f'- [exception]: {traceback_details["exception"]}\n'
    )
    return message


def export_data(filename, data, mode):
    with open(filename, mode, encoding='utf-8', newline='') as f:
        for line in data:
            f.write(f'{line}\n')


def check_files(exported_db_paths):
    result = True
    for file_path in exported_db_paths:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            result = False
            break
    return result


def export_users_in_channel(token, channel_id, export_db, export_count):
    contents_result = []
    mode = 'w'

    client = WebClient(token=token)
    try:
        # https://api.slack.com/methods/conversations.members
        result = client.conversations_members(channel=channel_id, limit=export_count)
        i = 0
        for user in result['members']:
            try:
                info = client.users_info(user=user).data
                if not info['user']['is_bot']:
                    user_info = info['user']
                    i += 1
                    member_id = user_info.get('id', None)
                    real_name = user_info.get('real_name', None)
                    email = user_info.get('profile', {}).get('email', None)

                    contents = (f'{i}|{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
                                f'|{channel_id}|{member_id}|{email}|{real_name}')
                    contents_result.append(contents)

                    if len(contents_result) >= 50:
                        export_data(export_db, contents_result, mode)
                        contents_result = []
                        mode = 'a'
            except SlackApiError as error:
                message = catch_try_error(error, export_users_in_channel.__name__)
                print(f'{Bcolors.Yellow}[-] Error: {message} {Bcolors.Endc}\n\n')

        if contents_result:
            export_data(export_db, contents_result, mode)
    except SlackApiError as error:
        message = catch_try_error(error, export_users_in_channel.__name__)
        print(f'{Bcolors.Yellow}[-] Error: {message} {Bcolors.Endc}\n\n')


def compare_db_and_get_users_not_in(file_paths):
    """
    Compares two database files and returns a list of users that are not present in the first file.
    Parameters:
        file_paths (list): A list containing paths to the two database files to be compared.
    Returns:
        list: A list of users that are present in the second file but not in the first file.
    """
    users_not_in_first_file = []
    with open(file_paths[0], 'r', encoding='utf-8') as file_a:
        users_in_file_a = set(line.strip().split('|')[3] for line in file_a)

    with open(file_paths[1], 'r', encoding='utf-8') as file_b:
        users_checked = set()
        for line in file_b:
            fields = line.strip().split('|')
            user, email, real_name = fields[3], fields[4], fields[5]
            if user not in users_checked and user not in users_in_file_a:
                users_not_in_first_file.append(user)
                users_checked.add(user)  # Add user to checked set
    return users_not_in_first_file


def invite_user_to_channel(token, channel, users, is_multiple):
    client = WebClient(token=token)
    try:
        # https://api.slack.com/methods/conversations.invite
        result = client.conversations_invite(channel=channel, users=users, force=is_multiple)
        if result['ok']:
            print(result['channel'])
        else:
            print(result['errors'])
    except SlackApiError as error:
        message = catch_try_error(error, invite_user_to_channel.__name__)
        print(f'{Bcolors.Yellow}[-] Error: {message} {Bcolors.Endc}\n\n')


def main():
    token = 'slack-apps-oauth-token(bot_token)'  # e.g. xoxb~~~
    """
    The "A" channel serves as the reference channel from which the user lists are retrieved, 
    while the "B" channel contains the list of users to be invited to the "A" channel.
    """
    channel_a = 'channel_id-to-invite'  # e.g. C05~~~
    channel_b = 'channel_id-to-invite'  # e.g. C05~~~

    export_count = 1000  # https://api.slack.com/methods/conversations.members > 'limit' parameter
    is_multiple = False

    channels = [channel_a, channel_b]
    home_path = os.path.dirname(os.path.realpath(__file__))
    exported_db_paths = []
    for channel in channels:
        export_filepath = os.path.join(home_path, f'channel_{channel}.db')
        export_users_in_channel(token, channel, export_filepath, export_count)
        exported_db_paths.append(export_filepath)

    is_valid = check_files(exported_db_paths)
    if is_valid:
        result_users = compare_db_and_get_users_not_in(exported_db_paths)
        if result_users:
            result_users = ','.join(result_users)
            if len(result_users) >= 2:
                is_multiple = True
            invite_user_to_channel(token, channel_a, result_users, is_multiple)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}'
              f'- [Func]: {__name__.__name__}\n'
              f'- [line_num]: {sys.exc_info()[-1].tb_lineno}\n'
              f'- [exception]: {type(e).__name__} {e}\n'
              f'{Bcolors.Endc}')
