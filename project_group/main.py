import api, overheads, project_group.coh as coh, project_group.profit_and_loss as profit_and_loss 
from pathlib import Path

file_path = Path.cwd()/'project group'/'overall_report.txt'
file_path.touch()

def main_func():
    forex = api.api_function()
    overheads.overheads_function(forex)
    coh.coh_function(forex)
    profit_and_loss.profitloss_function(forex)
