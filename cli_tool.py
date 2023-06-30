import click
import pandas as pd
# import math
# import statistics
# import numpy as np
# import scipy.stats

@click.group()
def main():
    pass

@click.command(name = 'describe')
@click.option('-f', '--filename'   , type=click.Path(exists=True), help = 'describe', default='error')
# @click.argument('filename', type=click.Path(exists=True))
def describe(filename):
    try:
        df = pd.read_csv(filename)
        click.echo(df.describe())
    except FileNotFoundError:
        click.echo(f"Error: No such file exists '{filename}'.")

@click.command(name = 'stat')
@click.option('-f', '--filename'   , type=str, help = 'filename', default='error')
@click.option('-c', '--column' , type=str, help = 'column name', default='error')
@click.option('-o', '--op'         , type=str, help = 'mean, mode, or median', default='error')
# @click.argument('filename', type=str)
# @click.argument('columnname', type=str)
def stat(filename, column, op):
    try:

        df = pd.read_csv(filename)
        if op == "mean":
            click.echo(f"Mean of '{column}': {df[column].mean()}")
        elif op == "mode":
            click.echo(f"Mode of '{column}': {df[column].mode()}")
        elif op == "median":
            click.echo(f"Median of '{column}': {df[column].median()}")
        else:
            click.echo(f"Error: No such option '{op}'.")

    except KeyError:
        click.echo(f"Error: No such column name '{column}'.")
    except FileNotFoundError:
        click.echo(f"Error: No such file exists '{filename}'.")

@click.command(name = "variance")
@click.option('-f', '--filename'   , type=str, help = 'filename', default='error')
@click.option('-cv', '--column' , type=str, help = 'column name', default='error')
# @click.option('-v','--var', type=int, help = 'Var and std dev')
def variance(filename, column):
    try:
        df = pd.read_csv(filename)
        click.echo(f"variance :{df[column].var()}")
        click.echo(f"std deviation : {df[column].std()}")
    except FileNotFoundError:
        click.echo(f"Error: No such file exists '{filename}'.")

main.add_command(describe)
main.add_command(stat)
main.add_command(variance)

if __name__ == '__main__':
    main