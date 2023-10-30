from models.openai import OpenAIClient
from argparser import parse
from utils import (
    execute_unix_command, 
    copy_command_to_clipboard
)

def cli():
    args = parse()

    print("|")
    print("|--- Finding corresponding UNIX command...")
    openai_client = OpenAIClient()
    unix_command = openai_client.get_unix_command(
        args.input, 
        model=args.model
    )

    if unix_command == "unknown":
        print("|")
        print("|--- No UNIX command found. Try again.")
        return

    print("|")
    print("|--- UNIX Command:", unix_command)

    if args.copy:
        copy_command_to_clipboard(unix_command)
        return
    
    if args.force:
        execute_unix_command(unix_command)
        return

    print("|")
    print("|--- Press Enter to execute command, type 'c' to copy, type anything else to abort: ", end="", flush=True)
    user_input: str = input().strip()
    if not user_input:
        execute_unix_command(unix_command)
    elif user_input == "c":
        copy_command_to_clipboard(unix_command)
    else:
        print("|")
        print("|--- Execution aborted.")