import argparse
import subprocess
import subprocess

from pyperclip import copy

from settings import VERSION, DEFAULT_MODEL, SUPPORTED_MODELS
from clients.openai import OpenAIClient

def main():

    parser = argparse.ArgumentParser(
        prog="unixgpt",
        description="Bridges the gap between natural language and UNIX commands"
    )

    # collect input (required)
    parser.add_argument(
        "-i", "--input",
        type=str,
        required=True,
        help="Natural language input to be converted to unix command. Enclose in quotation marks."
    )

    # model selection
    parser.add_argument(
        "-m", "--model",
        type=str,
        default=DEFAULT_MODEL,
        choices=SUPPORTED_MODELS,
        help="Supported large language model to use"
    )

    # force output execution
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Force execution of resulting UNIX command"
    )

    # development/feedback mode
    parser.add_argument(
        "-d", "--dev",
        action="store_true",
        help="Submit input/output for model improvement"
    )

    # print mode
    parser.add_argument(
        "-c", "--copy",
        action="store_true",
        help="Copy resulting UNIX command to clipboard (does not execute)"
    )

    # unixgpt version
    parser.add_argument(
        "--version",
        action="version",
        version=VERSION,
        help="Print version information and quit"
    )

    args = parser.parse_args()

    print("|")
    print("|--- Finding corresponding UNIX command...")
    openai_client = OpenAIClient()
    unix_command = openai_client.get_unix_command(
        args.input, 
        model=args.model
    )

    if unix_command == "unknown":
        print("No UNIX command found. Try again.")
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


def execute_unix_command(unix_command: str):
    print("|")
    try:
        print("|--- Executing...")
        subprocess.run(unix_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("|")
        print("|--- Execution Error:", e)


def copy_command_to_clipboard(unix_command: str):
    copy(unix_command)
    print("|")
    print("|--- Copied to clipboard.")


if __name__ == "__main__":
    main()