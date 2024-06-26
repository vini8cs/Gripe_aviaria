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


def run_bwa(fastq1, fastq2, genome, threads):

    if not os.path.isfile(f"{genome}.amb"):
        bwa_index = ["bwa", "index", genome]

        command = " ".join(bwa_index)
        print(f"The command used was: {command}")
        subprocess.run(bwa_index, check=True)

    bwa_mem = [
        "bwa",
        "mem",
        "-t",
        threads,
        genome,
        fastq1,
        fastq2,
        "-o"
        f"{fastq1}.sam"
    ]

    command = " ".join(bwa_mem)
    print(f"The command used was: {command}")
    subprocess.run(bwa_mem, check=True)

    samtools_view = [
        "samtools",
        "view",
        "-S",
        "-b",
        "--threads",
        threads,
        f"{fastq1}.sam",
        "-o"
        f"{fastq1}.bam"
    ]
    command = " ".join(samtools_view)
    print(f"The command used was: {command}")
    subprocess.run(samtools_view, check=True)

    samtools_fastq = [
        "samtools",
        "fastq",
        "-f",
        "4",
        f"{fastq1}.bam",
        "-1",
        f"{fastq1}.unaligned.fastq",
        "-2",
        f"{fastq2}.unaligned.fastq",
        "--threads",
        threads
    ]
    command = " ".join(samtools_fastq)
    print(f"The command used was: {command}")
    subprocess.run(samtools_fastq, check=True)

    return f"{fastq1}.unaligned.fastq", f"{fastq2}.unaligned.fastq"


def main():

    options = get_options()
    run_bwa(options.input1, options.input2, options.genome, options.threads)