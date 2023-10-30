import subprocess
import pyperclip

def execute_unix_command(unix_command: str):
    print("|")
    try:
        print("|--- Executing...")
        subprocess.run(unix_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("|")
        print("|--- Execution Error:", e)


def copy_command_to_clipboard(unix_command: str):
    pyperclip.copy(unix_command)
    print("|")
    print("|--- Copied to clipboard.")