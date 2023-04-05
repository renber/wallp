import argparse
import config

def getCommandLineOptions():
    parser = argparse.ArgumentParser()

    parser.add_argument('provider',                        
                        type=str,
                        metavar="provider",
                        choices=config.providers.keys(),
                        help="The service to retrieve the image from (" + ', '.join(config.providers.keys()) + ")")    

    return parser.parse_args()