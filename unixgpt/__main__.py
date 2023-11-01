from .cli import cli


def main():
    cli()


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        exit()