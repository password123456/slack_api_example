__author__ = 'https://github.com/password123456/'
__version__ = '1.0.2-2300828'

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


def get_user_info(token, member_id):
    client = WebClient(token=token)
    try:
        # https://api.slack.com/methods/users.info
        user_info = client.users_info(user=member_id).data

        display_name = user_info['user']['name']
        real_name = user_info['user']['real_name']
        phone = user_info['user']['profile']['phone']
        email = user_info['user']['profile']['email']

        if not display_name:
            display_name = 'null'
        elif not real_name:
            real_name = 'null'
        elif not phone:
            phone = 'null'
        elif not email:
            email = 'null'
            
        return f'"{display_name},{real_name},{email},{phone}"'
    except SlackApiError as e:
        print(f'{Bcolors.Yellow}- Api Error:: {e} {Bcolors.Endc}')
        return None


def get_list_of_uploaded_files_on_channel(token, channel_id):
    client = WebClient(token=token)
    try:
        # https://api.slack.com/methods/conversations.history
        result = client.conversations_history(channel=channel_id)
        conversation_history = result['messages']
        i = 0
        for block in conversation_history:
            if 'files' in block.keys():
                i = i + 1
                for file_list in block['files']:
                    upload_user = file_list['user']
                    upload_user_info = get_user_info(token, upload_user)

                    if not upload_user_info:
                        upload_user_info = 'User not exists'

                    upload_time = file_list['timestamp']
                    record_date = datetime.strptime(str(datetime.fromtimestamp(upload_time, tz=None)), '%Y-%m-%d %H:%M:%S')
                    local_timezone = datetime.now().astimezone().tzinfo
                    local_upload_time = record_date.astimezone(local_timezone)

                    upload_filename = file_list['title']
                    upload_filetype = file_list['filetype']
                    upload_file_preview = file_list['url_private']
                    file_download_url = file_list['url_private_download']

                    result = f'- uploaded_at: {local_upload_time}\n- user_info: {upload_user_info}\n' \
                             f'- filename: {upload_filename}\n- type: {upload_filetype}\n' \
                             f'- upload_preview: {upload_file_preview}\n- download_link: {file_download_url}\n'

                    print(result)

    except SlackApiError as e:
        print(f'{Bcolors.Yellow}- Api Error:: {e} {Bcolors.Endc}')


def main():
    bot_token = 'slack_apps_oauth_token(bot_token)'
    channel = 'Channel number for which you want to know'

    get_list_of_uploaded_files_on_channel(bot_token, channel)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- ::Exception:: Func:[{__name__.__name__}] '
              f'Line:[{sys.exc_info()[-1].tb_lineno}] [{type(e).__name__}] {e}{Bcolors.Endc}')
