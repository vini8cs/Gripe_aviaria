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
    parser = argparse.ArgumentParser(description="Trim Fastq files")
    parser.add_argument(
        "-s",
        "--sample",
        help="SRA accession",
        default="",
        required=True,
    )
    parser.add_argument(
        "-d",
        "--directory_path",
        help="Directory path where all data will be stored",
        default="",
        required=True,
    )
    parser.add_argument(
        "-t",
        "--threads",
        type=str,
        help="Number of threads",
        default=1,
        required=False,
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
    parser.add_argument(
        "-out1",
        "--output1",
        type=str,
        help="",
        default="Foward (R1) output filtered paired-end fastq",
        required=True,
    )
    parser.add_argument(
        "-out2",
        "--output2",
        type=str,
        help="",
        default="Reverse (R2) output filtered paired-end fastq",
        required=True,
    )

    options = parser.parse_args()

    return options


##########################################
## Extract fastp metadata
##########################################


def extract_metadata(R1, R2, output_metadata_path, threads):

    seqkit = ["seqkit", "stats", "-Ta", "-j", threads, R1, R2]

    with open(output_metadata_path, "w") as output_file:
        subprocess.run(seqkit, check=True, stdout=output_file)


##########################################
## Control quality and trimming with fastp
##########################################


def run_fastp(
    threads: int, input1: str, input2: str, output1: str, output2: str, output_dir: str
) -> None:
    """
    Run Fastp for quality control and trimming of sequencing data.

    Args:
        threads (int): Number of threads/cores to use for the mapping process.
        sra_path (str): Path to the directory for storing Fastp output and intermediate files.
        sra_filtered (str): Path to the output filtered FASTQ file (single-end).
        sra_filtered_1 (str): Path to the output filtered first paired-end FASTQ file.
        sra_filtered_2 (str): Path to the output filtered second paired-end FASTQ file.
        sra (str): Path to the input single-end FASTQ file.
        sra1 (str): Path to the input first paired-end FASTQ file.
        sra2 (str): Path to the input second paired-end FASTQ file.
        adapter_file (str): Path to the adapter sequences FASTA file.

    Returns:
        str: A message indicating the conclusion of Fastp quality control and trimming.
    """
    # Define the paths for Fastp JSON and HTML output files
    json = os.path.join(output_dir, "fastp.json")
    html = os.path.join(output_dir, "fastp.html")

    # Check if filtered FASTQ files already exist; if not, perform Fastp processing

    fastp = [
        "fastp",
        "-w",
        threads,
        "-q",
        "20",
        "-l",
        "50",
        "--trim_tail1",
        "5",
        "--trim_front1",
        "9",
        "--trim_tail2",
        "5",
        "--trim_front2",
        "9",
        "-j",
        json,
        "-h",
        html,
        "--in1",
        input1,
        "--in2",
        input2,
        "--out1",
        output1,
        "--out2",
        output2,
    ]

    command = " ".join(fastp)
    print(f"The command used was: {command}")
    subprocess.run(fastp, check=True)


def main() -> None:
    """
    This main function automates the process of filtering and trimming of SRA data.
    """
    # Parse command line options
    options = get_options()

    output_dir = os.path.join(options.directory_path, options.sample)

    output_metadata_path = os.path.join(options.directory_path, options.sample, f"{options.sample}_metadata.tsv")

    output_fastp_metadata_path = os.path.join(options.directory_path, options.sample, f"{options.sample}_fastp_metadata.tsv")
    # Run Fastp for quality control and trimming
    
    extract_metadata(options.input1, options.input2, output_metadata_path, options.threads)
    
    run_fastp(
        options.threads,
        options.input1,
        options.input2,
        options.output1,
        options.output2,
        output_dir
    )

    extract_metadata(options.output1, options.output2, output_fastp_metadata_path, options.threads)


if __name__ == "__main__":
    main()
