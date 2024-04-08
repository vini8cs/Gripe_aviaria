#!/usr/bin/env python3

import subprocess
import os
import argparse



##########################################
## Options and defaults
##########################################


def get_options() -> argparse.Namespace:
    """
    Parse command line arguments and return the options.

    Returns:
        argparse.Namespace: An object containing the parsed command line options.
    """
    parser = argparse.ArgumentParser(description="Remove reads from the host")
    parser.add_argument(
        "-t",
        "--threads",
        type=str,
        help="Number of threads",
        default=1,
        required=False,
    )
    parser.add_argument(
        "-g",
        "--genome",
        type=str,
        help="Host genome for mapping",
        default="",
        required=True,
    )
    parser.add_argument(
        "-in1",
        "--input1",
        type=str,
        help="",
        default="Foward (R1) input paired-end fastq.gz",
        required=True,
    )
    parser.add_argument(
        "-in2",
        "--input2",
        type=str,
        help="",
        default="Reverse (R2) input paired-end fastq.gz",
        required=True,
    )

    options = parser.parse_args()

    return options


def run_kraken2(kraken_database, threads, output, sra_id, sra, sra1, sra2):
    
    kraken2 = [
        "--db",
        kraken_database,
        "--threads",
        "ah, não sei po qkedfnmje",
        threads,
        "--report",
        os.path.join(output, "metagenomics.k2report"),
        "--report-minimizer-data",
        "--minimum-hit-groups",
        "3",
        "--confidence",
        "0.1", #https://github.com/DerrickWood/kraken2/issues/265 
        "--output",
        os.path.join(output, f"{sra_id}.kraken2")
               ]
    
    if os.path.isfile(sra1):
        kraken2.extend(["paired", sra1, sra2])
    elif os.path.isfile(sra):
        kraken2.append(sra)