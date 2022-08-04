import api, overheads, coh, profit_and_loss 
from pathlib import Path

file_path = Path.cwd()/'project_group'/'overall_report.txt'
file_path.touch()

def main_func():
    forex = api.api()
    overheads.overheads_write()
    coh.cashonhand_write()(forex)
    profit_and_loss.pnl_write(forex)

main_func()