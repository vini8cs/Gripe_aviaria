#!/usr/bin/env python3

import subprocess
import os
import argparse
from Bio import Entrez, SeqIO


##########################################
## Options and defaults
##########################################


# def get_options() -> argparse.Namespace:
#     """
#     Parse command line arguments and return the options.

#     Returns:
#         argparse.Namespace: An object containing the parsed command line options.
#     """
#     parser = argparse.ArgumentParser(description="Trim Fastq files")
#     parser.add_argument(
#         "-s",
#         "--sample",
#         help="SRA accession",
#         default="",
#         required=True,
#     )
#     parser.add_argument(
#         "-d",
#         "--directory_path",
#         help="Directory path where all data will be stored",
#         default="",
#         required=True,
#     )
#     parser.add_argument(
#         "-t",
#         "--threads",
#         type=str,
#         help="Number of threads",
#         default=1,
#         required=False,
#     )
#     parser.add_argument(
#         "-in1",
#         "--input1",
#         type=str,
#         help="",
#         default="Foward (R1) input paired-end fastq.gz",
#         required=True,
#     )
#     parser.add_argument(
#         "-in2",
#         "--input2",
#         type=str,
#         help="",
#         default="Reverse (R2) input paired-end fastq.gz",
#         required=True,
#     )
#     parser.add_argument(
#         "-out1",
#         "--output1",
#         type=str,
#         help="",
#         default="Foward (R1) output filtered paired-end fastq",
#         required=True,
#     )
#     parser.add_argument(
#         "-out2",
#         "--output2",
#         type=str,
#         help="",
#         default="Reverse (R2) output filtered paired-end fastq",
#         required=True,
#     )

#     options = parser.parse_args()

#     return options


def run_bwa(fastq1, fastq2, genome, threads):

    if not os.path.isfile(f"{genome}.amb"):
        bwa_index = ["bwa", "index", genome]

        command = " ".join(bwa_index)
        print(f"The command used was: {command}")
        subprocess.run(bwa_index, check=True)

    bwa_aln = ["bwa", "aln", "-t", threads, genome]

    for j, i in zip(["-1", "-2"], [fastq1, fastq2]):

        bwa_aln.extend([j, i, "-f", f"{i}.sai"])
        command = " ".join(bwa_aln)
        print(f"The command used was: {command}")
        subprocess.run(bwa_aln, check=True)
        bwa_aln = bwa_aln[:-4]

    bwa_sampe = [
        "bwa",
        "sampe",
        genome,
        f"{fastq1}.sai",
        f"{fastq2}.sai",
        fastq1,
        fastq2,
    ]

    command = " ".join(bwa_sampe)
    print(f"The command used was: {command}")
    with open(f"{fastq1}.sam") as output_file:
        subprocess.run(bwa_sampe, check=True, stdout=output_file)

    return f"{fastq1}.sam"
