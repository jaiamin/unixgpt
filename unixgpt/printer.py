# ========================================
# Console print methods using rich.console
# ========================================
#
# TODO: 
# - Handle rich.console errors
# - More table styling options for UnixGPT library tables
#

from rich.console import Console
from rich.table import Table


class RichConsole():
    def __init__(self, pre_symbol: str = "=>"):
        self.console = Console()
        self.tables: dict[Table] = dict()
        self.log: str = ""
        
        # Constants
        self.PRE_SYMBOL: str = pre_symbol
        self.EMOJIS = {
            "in-progress": "👨‍💻",
            "success": "🙆‍♂️",
            "issue": "🤷‍♂️",
            "error": "🤦‍♂️"
        }


    def rich_print(self, message: str):
        """Regular print to rich console"""
        self.console.print(message)
        self.log_message(message)

    
    def rich_print_with_pre_symbol(self, message: str):
        """Print with pre-symbol to rich console"""
        message_with_pre_symbol = self.PRE_SYMBOL + " " + message
        self.console.print(message_with_pre_symbol)
        self.log_message(message_with_pre_symbol)

    
    def rich_print_newline(self):
        """Print newline to rich console"""
        self.console.print("\n")
        self.log_message("\n")

    
    def get_emoji(self, alt_name: str):
        """Get valid emoji"""
        if alt_name not in self.EMOJIS:
            raise ValueError(f"Emoji alt_name '{alt_name}' does not exist.")
        
        return self.EMOJIS[alt_name]
    
    
    def get_code_print(self, message: str):
        """Get message with code styling"""
        message_wrapped = f"[code] {message} [/code]"
        self.console.print(message_wrapped)
    

    def add_table(self, name: str, columns: list[str], rows: list[list[str]], bold_columns: bool=True):
        """Create and add a unique-named table"""
        if not name:
            raise ValueError("The table should have a name in order to be added.")
        if name in self.tables:
            raise ValueError("This table name already exists.")

        if not columns:
            raise ValueError("At least one column must be provided.")
        if not rows:
            raise ValueError("At least one row must be provided.")

        c_len = len(columns)
        for i, row in enumerate(rows):
            if len(row) != c_len:
                raise ValueError(f"Row {i+1} should have exactly {c_len} columns (actual: {len(row)} columns)")

        table = Table()

        for col_name in columns:
            if bold_columns:
                table.add_column(col_name, style="bold")
            else:
                table.add_column(col_name)

        for row in rows:
            table.add_row(*row)

        self.tables[name] = table


    def print_table(self, name: str):
        """Print an existing table to the console"""
        if name not in self.tables:
            raise ValueError("This table name does not exist.")
        
        table = self.tables[name]
        self.console.print(table)
        self.log_message(table)

    
    def log_message(self, message: str):
        """Log a message to UnixGPT log"""
        self.log += message + "\n"


    def get_log(self):
        """Get UnixGPT message log"""
        return self.log