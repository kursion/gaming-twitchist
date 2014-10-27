"""
This small application let you get a list
of live stream for a specific game on twitch.

Author: Yves Lange (Kursion)

example:
    $ twichist --game "Dota 2" --limit 50
"""

from urllib import request
from subprocess import call
from colorama import Fore, Back, Style
import json, colorama, argparse

def main():
    colorama.init()

    # CONFIGURATION
    parser = argparse.ArgumentParser(description='Twitch.tv Stream List')
    parser.add_argument('--game',
                        help='show stream for a specific game (default: "Dota 2")', default='Dota 2')
    parser.add_argument('--browser',
                        help='name of the browser to open stream (default: chromium)', default='chromium')
    parser.add_argument('--limit', type=int,
                        help='limit of channel to show (default: 20)', default='20')
    args = parser.parse_args()

    # HELPERS
    def colored(s, color):
        """Helper function to have a nice
        coloured python script.
        """
        return color+str(s)+Style.RESET_ALL

    def printError(s):
        print(colored(s, Style.BRIGHT+Fore.RED))
        exit()

    # LET'S START !!!
    print(colored("Parsing '"+args.game+"' from twitch", Style.BRIGHT+Fore.BLACK))

    # Getting list from twitch
    try:
        req = request.urlopen("https://api.twitch.tv/kraken/streams?game="+args.game.replace(" ", "+"))
        encoding = req.headers.get_content_charset()
        obj = json.loads(req.read().decode(encoding))
    except:
        printError("Couldn't parse from twitch.tv")

    # Data used to display streams
    URLS = []
    LIMIT = min(args.limit, len(obj["streams"]))

    # Check if streams were found
    if LIMIT == 0:
        printError("Nothing found for '%s' on twitch" % args.game)
    else:
        print(
            colored("%d found, displaying %d" % (len(obj["streams"]), LIMIT),
                Style.BRIGHT+Fore.GREEN))


    # Display the streams
    for i in range(1, LIMIT+1):
        stream  = obj["streams"][i-1]
        channel = stream["channel"]
        viewers = stream["viewers"]
        name    = channel["display_name"][:12].replace(" ", "")
        status  = channel["status"].replace("\n", "").replace("\r", "")[:50]
        print( "{0:2} {1:17} {2:23} {3:1} {4:50}".format(
            i,
            "["+colored(viewers, Fore.RED)+"]",
            colored(name, Fore.BLUE),
            colored("|", Fore.GREEN),
            status
        ))
        URLS.append(stream["channel"]["url"]+"/popout")


    while True:
        try:
            choice  = int(input("What to see ? "))-1
            channel = obj["streams"][choice]["channel"]
            name    = channel["display_name"]
            status  = channel["status"]
            url     = URLS[choice]
            print(colored("You are watching: %d" % choice, Style.DIM+Fore.YELLOW))
            print(colored("Name %s | %s" % (name, status), Style.BRIGHT+Fore.YELLOW))
            break
        except Exception:
            printError("\n\rBAD CHOICE !")
        except KeyboardInterrupt:
            print("Bye...")
            exit()

    # NOTE: for chrome with use the app parameter
    if args.browser in ["chromium", "chrome", "google-chrome"]:
        call([args.browser, "--app="+url])
    else:
        call([args.browser, url])

if __name__ == "__main__": main()

