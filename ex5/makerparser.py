from argparse import Namespace, ArgumentParser

parser = ArgumentParser()

parser.add_argument("-vs", "--vertical-start", type=int, default=None)
parser.add_argument("-ve", "--vertical-end", type=int, default=None)
parser.add_argument("-hs", "--horizontal-start", type=int, default=None)
parser.add_argument("-he", "--horizontal-end", type=int, default=None)
parser.add_argument("-p", "--partial", action="store_true")
parser.add_argument("-f", "--file", type=str, default=None)
parser.add_argument("-k", "--key", type=str, default=None)
parser.add_argument("-d", "--decrypt", action="store_true")


def check_args(args: Namespace):
    if args.file is None:
        print("Missing file")
        exit(1)
    if args.partial:
        missing_string = "Missing required argument for partial mode:"
        error = False
        if args.vertical_start is None:
            missing_string += " --vertical-start"
            error = True
        if args.horizontal_start is None:
            missing_string += " --horizontal-start"
            error = True
        if args.vertical_end is None:
            missing_string += " --vertical-end"
            error = True
        if args.horizontal_end is None:
            missing_string += " --horizontal-end"
            error = True
        if error:
            print(missing_string)
            exit(1)
    if args.decrypt:
        if args.key is None:
            print("Missing required argument for decryption mode: --key")
            exit(1)
