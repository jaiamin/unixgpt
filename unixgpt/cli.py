#
# TODO:
# - Move table creation out of functions to avoid duplicate tables in self.tables
# - Handle potential ValueErrors raised by RichConsole methods
#


import sys

from .argparser import parse
from .models.openai import OpenAIClient
from .library import (
    save_to_library
)
from .utils import (
    execute_unix_command, 
    copy_command_to_clipboard
)
from .prompts import OPENAI_UNIX_COMMAND_PROMPT, OPENAI_REVISE_INSTRUCTIONS_PROMPT
from .printer import RichConsole


ACTIONS = {
    "execute": "e",
    "copy": "c",
    "save": "s",
    "revise": "r",
    "abort": "a"
}

console = RichConsole()

OPENAI_CLIENT: OpenAIClient = None

known_actions_table_name = "known-actions"
known_actions_table_cols = ["Action", "Key", "Combineable", "Description"]
known_actions_table_rows = [
    ["Execute", "e", "Yes", "Execute the command"],
    ["Copy", "c", "Yes", "Copy the command"],
    ["Save", "s", "Yes", "Save the command"],
    ["Revise", "r", "No", "Revise the input"],
    ["Abort", "a", "No", "Abort the program"],
]

console.add_table(
    name=known_actions_table_name,
    columns=known_actions_table_cols,
    rows=known_actions_table_rows,
)

unknown_actions_table_name = "unknown-actions"
unknown_actions_table_cols = ["Action", "Key", "Description"]
unknown_actions_table_rows = [
    ["Revise", "r", "Revise the input"],
    ["Abort", "a", "Abort the program"],
]

console.add_table(
    name=unknown_actions_table_name,
    columns=unknown_actions_table_cols,
    rows=unknown_actions_table_rows,
)


def cli(openai_api_key: str):
    """CLI entry point"""
    args = parse()

    global OPENAI_CLIENT
    OPENAI_CLIENT = OpenAIClient(openai_api_key=openai_api_key)

    # -i, --input
    if args.input:
        user_input = args.input.strip()
        handle_input(nl_input=user_input, prompt=OPENAI_UNIX_COMMAND_PROMPT)


def handle_input(nl_input: str, prompt: str):
    """handle input"""
    in_progress_emoji = console.get_emoji("in-progress")
    console.rich_print_with_pre_symbol(f"Searching... {in_progress_emoji}")

    unix_command = OPENAI_CLIENT.fetch_unix_command(
        user_input=nl_input,
        system_prompt=prompt,
        model="gpt-3.5-turbo",
    )
    unix_command = unix_command.strip()

    if unix_command.lower() == "unknown":
        issue_emoji = console.get_emoji("issue")
        console.rich_print_with_pre_symbol(f"Command not found. {issue_emoji}")

        console.print_table("unknown-actions")

        handle_unknown_actions(unix_command=unix_command, nl_input=nl_input)

    else:
        success_emoji = console.get_emoji("success")
        code_wrapped_message = console.get_print_code(unix_command)
        console.rich_print_with_pre_symbol(f"Command found! {success_emoji} {code_wrapped_message}")

        console.print_table("known-actions")

        handle_known_actions(unix_command=unix_command, nl_input=nl_input)


def handle_unknown_actions(unix_command: str, nl_input: str):
    """handle unknown actions"""
    try:
        action_input = input("=> Choose an action key: ").strip().lower()
    except KeyboardInterrupt:
        console.rich_print_newline()
        handle_abort_action()
    
    if not any(act in action_input for act in ACTIONS.values()):
        error_emoji = console.get_emoji("error")
        console.rich_print_with_pre_symbol(f"Enter a valid action. {error_emoji}")
        handle_unknown_actions(nl_input)
    
    if ACTIONS["abort"] == action_input:
        handle_abort_action()
        return
    elif ACTIONS["revise"] == action_input:
        handle_revise_action(unix_command)
        return
    else:
        handle_unknown_actions(unix_command, nl_input)


def handle_known_actions(unix_command: str, nl_input: str):
    """handle known actions"""
    try:
        action_input = input("=> Choose action key(s): ").strip().lower()
    except KeyboardInterrupt:
        console.rich_print_newline()
        handle_abort_action()

    if not any(act in action_input for act in ACTIONS.values()):
        error_emoji = console.get_emoji("error")
        console.rich_print_with_pre_symbol(f"Enter a valid action. {error_emoji}")
        handle_known_actions(unix_command=unix_command, nl_input=nl_input)

    if ACTIONS["abort"] in action_input:
        handle_abort_action()
        return
    if ACTIONS["revise"] in action_input:
        handle_revise_action(unix_command)
        return
    
    if ACTIONS["copy"] in action_input:
        handle_copy_action(unix_command=unix_command)
    if ACTIONS["save"] in action_input:
        handle_save_action(unix_command=unix_command, nl_input=nl_input)
    if ACTIONS["execute"] in action_input:
        handle_execute_action(unix_command=unix_command)


def handle_execute_action(unix_command: str):
    """handle execute actions"""
    in_progress_emoji = console.get_emoji("in-progress")
    console.rich_print_with_pre_symbol(f"Executing... {in_progress_emoji}")
    response = execute_unix_command(unix_command=unix_command)

    if "success" in response:
        console.rich_print_with_pre_symbol(response["success"])
    else:
        console.rich_print_with_pre_symbol(response["error"])


def handle_edit_command_action(unix_command: str):
    pass


def handle_copy_action(input: str):
    """handle copy action"""
    response = copy_command_to_clipboard(unix_command=input)

    if "success" in response:
        console.rich_print_with_pre_symbol(response["success"])
    else:
        console.rich_print_with_pre_symbol(response["error"])


def handle_save_action(unix_command: str, nl_input: str):
    """handle save action"""
    ### COMING SOON ###
    save_to_library(nl_input=nl_input, unix_command=unix_command)


def handle_revise_action(unix_command: str):
    """handle revise action"""
    new_input = input("=> Clarify instructions: ")
    prompt = OPENAI_REVISE_INSTRUCTIONS_PROMPT.format(unix_command)
    handle_input(nl_input=new_input, prompt=prompt)

    
def handle_abort_action():
    """handle abort action"""
    in_progress_emoji = console.get_emoji("in-progress")
    console.rich_print_with_pre_symbol(f"Aborting... {in_progress_emoji}")
    sys.exit()
