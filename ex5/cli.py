from cli.makerparser import parser, check_args
from cli.encrypter import encrypt_partial, encrypt_full
from cli.decrypter import decrypt_partial, decrypt_full

if __name__ == "__main__":
    args = parser.parse_args()
    check_args(args)
    if not args.decrypt:
        if args.partial:
            encrypt_partial(args.file, args.vertical_start, args.vertical_end, args.horizontal_start, args.horizontal_end)
        else:
            encrypt_full(args.file)
    else:
        if args.partial:
            decrypt_partial(args.file, args.key, args.vertical_start, args.vertical_end, args.horizontal_start, args.horizontal_end)
        else:
            decrypt_full(args.file, args.key)
