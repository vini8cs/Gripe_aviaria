configfile : "config/config.yaml"

def remove_trailing_slash(path):
    if path.endswith("/"):
        path = path[:-1]
    return path

output_dir = remove_trailing_slash(congig['output_dir'])

samples = pd.read_table(config['sample_file'], sep='\t').set_index("sample", drop=False)

rule all:
    input:
        expand("{output_dir}/{sample}/{sample}_fastp_metadata.tsv", output_dir = output_dir, sample = samples['sample']),
        expand("{output_dir}/{sample}/{sample}_metadata.tsv", output_dir = output_dir, sample = samples['sample'])

rule fastp:
    input:
        input1 = "{output_dir}/{sample}/{sample}_R1_001.fastq.gz",
        input2 = "{output_dir}/{sample}/{sample}_R2_001.fastq.gz"
    output:
        output1 = "{output_dir}/{sample}/{sample}_R1_001.fastq",
        output2 = "{output_dir}/{sample}/{sample}_R2_001.fastq",
        json = temp(local("{output_dir}/{sample}/fastp.json")),
        html = temp(local("{output_dir}/{sample}/fastp.html")),
        output_metadata_fastp_path = "{output_dir}/{sample}/{sample}_fastp_metadata.tsv",
        output_metadata_path = "{output_dir}/{sample}/{sample}_metadata.tsv"
    params:
        threads = config['threads']
    conda:
        "../envs/environment_fastp.yml"
    log: "{output_dir}/{sample}/logs/{sra}.fastp.log"
    benchmark:
        "{path}/{sra}/benchmarks/fastp_pe.{sra}.RawSeq"
    shell:
        """
        python scripts/run_fastp.py --threads {params.threads} --directory_path {wildcards.output_dir} --sample {wildcards.sample} --input1 {input.input1} --input2 {input.input2} --output1 {output.output1} --output2 {output.output2} 2> {log}
        """ 
    

