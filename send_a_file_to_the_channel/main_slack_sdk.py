__author__ = 'https://github.com/password123456/'
__version__ = '1.0.0-230829'

import os
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


def file_is_not_empty(file_name):
    limit = 10
    f = os.stat(file_name).st_size
    if f >= limit:
        return True
    else:
        return False


def chat_post_message(bot_token, channel_id, message):
    # https://api.slack.com/methods/chat.postMessage
    client = WebClient(token=bot_token)
    try:
        result = client.chat_postMessage(channel=channel_id, text=message, as_user=True)
        print(result)
    except SlackApiError as e:
        print(f'{Bcolors.Yellow}- Api Error:: {e} {Bcolors.Endc}')


def upload_files_to_channel(bot_token, channel_id, upload_file, upload_file_title):
    # https://api.slack.com/methods/files.upload
    # https://github.com/slackapi/python-slack-sdk/releases/tag/v3.19.0
    try:
        client = WebClient(token=bot_token)
        result = client.files_upload_v2(channel=channel_id, title=upload_file_title, file=upload_file)
        if result['ok']:
            return result['file']['permalink']
        else:
            return None
    except SlackApiError as e:
        print(f'{Bcolors.Yellow}- Api Error:: {e} {Bcolors.Endc}')
        return None


def main():
    bot_token = 'slack_apps_oauth_token(bot_token)'
    channel_id = 'Channel number'

    upload_file = f'{os.getcwd()}/jquery.toc.zip'
    upload_file_title = upload_file.rsplit('/')[-1]

    if file_is_not_empty(upload_file):
        uploaded_file_link = upload_files_to_channel(bot_token, channel_id, upload_file, upload_file_title)
        if uploaded_file_link:
            # Display the uploaded file as a Markdown-style link, not an absolute file path.
            # e.g <https://www.stackoverflow.com|link>
            message = f'<!channel> Hello Guys.\nThis is for you\n<{uploaded_file_link}|{upload_file_title}>'
            chat_post_message(bot_token, channel_id, message)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- ::Exception:: Func:[{__name__.__name__}] '
              f'Line:[{sys.exc_info()[-1].tb_lineno}] [{type(e).__name__}] {e}{Bcolors.Endc}')
