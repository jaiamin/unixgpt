import argparse
from constants import (
    DEFAULT_MODEL, 
    SUPPORTED_MODELS,
    VERSION
)

def parse():
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

    # force output execution (CONSIDER REMOVING)
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Force execution of resulting UNIX command"
    )

    # development/feedback mode (CONSIDER REMOVING)
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

    # # interactive mode
    # parser.add_argument(
    #     "--interactive",
    #     action="store_true",
    #     help="Continue the conversation to clarify input"
    # )

    # unixgpt version
    parser.add_argument(
        "--version",
        action="version",
        version=VERSION,
        help="Print version information and quit"
    )
    
    return parser.parse_args()