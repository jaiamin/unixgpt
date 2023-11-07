# ========================================
# Console print methods using rich.console
# ========================================

from rich.console import Console
from rich.table import Table

class RichConsole():
    def __init__(self):
        self.console = Console()
        self.tables = dict()
    
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
        """Print a created table to the console"""

        if name not in self.tables:
            raise ValueError("This table name does not exist.")
        
        table = self.tables[name]
        self.console.print(table)