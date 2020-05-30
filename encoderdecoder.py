import urllib.parse
from urllib.parse import unquote
import sys
import bcolors, argparse

def banner():
    print(bcolors.BLUE + """

                ▒█▀▀▀ █▀▀▄ █▀▀ █▀▀█ █▀▀▄ █▀▀ █▀▀█ ░░ ▒█▀▀▄ █▀▀ █▀▀ █▀▀█ █▀▀▄ █▀▀ █▀▀█ 
                ▒█▀▀▀ █░░█ █░░ █░░█ █░░█ █▀▀ █▄▄▀ ▀▀ ▒█░▒█ █▀▀ █░░ █░░█ █░░█ █▀▀ █▄▄▀ 
                ▒█▄▄▄ ▀░░▀ ▀▀▀ ▀▀▀▀ ▀▀▀░ ▀▀▀ ▀░▀▀ ░░ ▒█▄▄▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀░ ▀▀▀ ▀░▀▀                                                                                    
                                                                         Coded By: NG
           """)

if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] == '-e'):
        try:
            input_url = sys.argv[2]

            parser = argparse.ArgumentParser()
            parser.add_argument("-e", required=True)
            parser.add_argument("-help")
            args = parser.parse_args()

            encode_url = urllib.parse.quote_plus(input_url)
            print(bcolors.OKMSG + 'encoded URL', encode_url)
        except:
            banner()
            print(bcolors.ERR + 'Please enter python  encoderdecoder.py -e <String or URl which you want to encode with inverted commas> ')

    elif (sys.argv[1] == '-d'):
        try:
            input_url_encoded = sys.argv[2]
            parser = argparse.ArgumentParser()
            parser.add_argument("-d", required=True)
            parser.add_argument("-help")
            args = parser.parse_args()

            decoded_url = unquote(input_url_encoded)
            print(bcolors.OKMSG + 'Decocoded URL: ', decoded_url)
        except:
            banner()
            print(bcolors.ERR + 'Please enter python  encoderdecoder.py -d <String or URl which you want to decode>')

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: encoderdecoder.py [-h] -d String or URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-d Decoder,   --enter string or URL which you want to encode witin inverted commas' '\n' '-e Encoder,    --enter string or URL which you want to decode within inverted commas')
else:
    banner()
    print(bcolors.ERR + 'Please select at least 1 option from (-d,-e) or -h, with a name string or url')




