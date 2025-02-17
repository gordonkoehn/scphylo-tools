import os

import click

import scphylo as scp


@click.command(short_help="Run SPhyR.")
@click.argument(
    "genotype_file",
    required=True,
    type=click.Path(
        exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True
    ),
)
@click.argument(
    "alpha",
    required=True,
    type=float,
)
@click.argument(
    "beta",
    required=True,
    type=float,
)
@click.option(
    "--n_restarts",
    "-r",
    default=10,
    type=int,
    show_default=True,
    help="Number of restarts.",
)
@click.option(
    "--n_threads",
    "-p",
    default=1,
    type=int,
    show_default=True,
    help="Number of threads.",
)
def sphyr(genotype_file, alpha, beta, n_restarts, n_threads):
    """SPhyR.

    Tumor phylogeny estimation from single-cell sequencing data under loss and error
    :cite:`SPhyR`.

    scphylo solver sphyr input.SC 0.0001 0.1
    """
    outfile = os.path.splitext(genotype_file)[0]

    scp.settings.verbosity = "info"
    scp.settings.logfile = f"{outfile}.sphyr.log"

    df_in = scp.io.read(genotype_file)
    if alpha == 0:
        alpha = 0.000000000001
    df_out = scp.tl.sphyr(
        df_in, alpha=alpha, beta=beta, n_restarts=n_restarts, n_threads=n_threads
    )
    scp.io.write(df_out, f"{outfile}.sphyr.CFMatrix")

    return None
