from makerparser import parser, check_args
from encrypter import encrypt_partial, encrypt_full
from decrypter import decrypt_partial, decrypt_full

# Main entry point for the script, handling command-line arguments to perform encryption or decryption
if __name__ == "__main__":
    args = parser.parse_args()
    check_args(args)
    if not args.decrypt:
        # If the script is not set to decrypt, it will proceed with encryption
        if args.partial:
            # Encrypts a portion of the image based on specified vertical and horizontal ranges
            encrypt_partial(args.file, args.vertical_start, args.vertical_end, args.horizontal_start, args.horizontal_end)
        else:
            # Encrypts the entire image
            encrypt_full(args.file)
    else:
        # If the script is set to decrypt, it will proceed with decryption
        if args.partial:
            # Decrypts a portion of the image based on specified vertical and horizontal ranges
            decrypt_partial(args.file, args.key, args.vertical_start, args.vertical_end, args.horizontal_start, args.horizontal_end)
        else:
            # Decrypts the entire image
            decrypt_full(args.file, args.key)
