# Methods

## Experimental Design

I studied the Pasilla RNAi experiment in *Drosophila melanogaster* using the GTN training data. The original study is available as [GSE18508](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE18508); the training files are deposited in [Zenodo record 6457007](https://zenodo.org/records/6457007). Four samples belonged to the untreated condition and three to the treated condition. Sequencing layout was included as a technical factor.

| Sample | Treatment | Sequencing layout |
|---|---|---|
| GSM461176 | untreated | single-end |
| GSM461177 | untreated | paired-end |
| GSM461178 | untreated | paired-end |
| GSM461182 | untreated | single-end |
| GSM461179 | treated | single-end |
| GSM461180 | treated | paired-end |
| GSM461181 | treated | paired-end |

The primary contrast was treat versus untreat. The sequencing-layout factor controlled for the systematic difference between single-end and paired-end libraries rather than being interpreted as a biological condition.

## Reference-based Workflow

The FASTQ exercise used subsampled paired-end data from GSM461177 and GSM461180. The seven-sample differential-expression exercise used the supplied count files. I recorded the genome as Drosophila Release 6 and the annotation as `Drosophila_melanogaster.BDGP6.32.109_UCSC.gtf.gz`.

The intended genome-based workflow was:

1. organize single-end and paired-end FASTQ collections;
2. assess read quality;
3. trim low-quality sequence with Cutadapt;
4. align reads to the *D. melanogaster* reference genome with the splice-aware STAR aligner;
5. assign aligned reads to annotated genes with featureCounts;
6. fit a count-based differential-expression model with DESeq2;
7. annotate and filter differential-expression results;
8. test GO enrichment with goseq;
9. examine KEGG pathways, Pathview output, and a heatmap.

Cutadapt completed. Falco quality-control jobs failed, and STAR mapping failed after the output collections had been created. Because no usable STAR BAM files were available, the planned featureCounts step from those BAM files was not completed. I therefore used the seven GTN-provided featureCounts files for the downstream training analysis and kept this provenance explicit.

## Why Genome-based Mapping Matters

Genome-based RNA-seq mapping retains genomic coordinates and splice-junction information. Splice-aware aligners such as STAR or HISAT2 can place reads that cross exon junctions. Counts can then be generated with featureCounts or HTSeq-count using a GTF/GFF annotation.

An alternative reference-transcriptome workflow uses tools such as Salmon or Kallisto to estimate transcript abundance directly or by lightweight mapping. This is computationally efficient for expression quantification but does not provide the same genome-coordinate view as a full genome alignment.

## Reproducibility Note

The included `.ga` file is the official GTN QC, mapping, and counting workflow. It preserves 29 workflow steps, creator identifiers, an execution-report definition, and the original MIT license. My contribution was executing and troubleshooting the training analysis, not authoring this workflow.

This export covers the upstream workflow only. It is not an export of the repaired DESeq2/GO invocation. Its tool versions and reference-index labels may require changes on a current Galaxy server.
