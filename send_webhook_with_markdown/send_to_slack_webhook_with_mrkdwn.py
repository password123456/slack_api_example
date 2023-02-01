__author__ = 'https://github.com/password123456/'
__date__ = '2023.01.28'
__version__ = '1.0.0'

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


def send_to_slack(message):
    webhook_url = 'YOUR WEBHOOK URL'

    header = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    }

    params = [
        {
            'type': 'section',
            'text': {
                'type': 'mrkdwn',
                'text': message
            }
        }
    ]

    try:
        r = requests.post(webhook_url, headers=header, data=json.dumps({'blocks': params}), verify=True)
        print(f'{Bcolors.Green}- http_code: {r.status_code} { Bcolors.Endc}')
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- ::Exception:: Func:[{send_to_slack.__name__}] Line:[{sys.exc_info()[-1].tb_lineno}] [{type(e).__name__}] {e}{Bcolors.Endc}')
    else:
        r.close()


def main():
    msg = f"""
Hi ~ <!channel>
> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.

I love supporting the **[EFF](https://eff.org)**.
This is the *[Markdown Guide](https://www.markdownguide.org)*.

`# This program prints Hello, world!`
`print('Hello, world!')`
"""
    send_to_slack(msg)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- ::Exception:: Func:[{__name__.__name__}] Line:[{sys.exc_info()[-1].tb_lineno}] [{type(e).__name__}] {e}{Bcolors.Endc}')
        
        
