# DESeq2, GO, and KEGG Analysis

## DESeq2 Design

I modelled treatment while accounting for sequencing layout. The primary comparison was treat versus untreat across seven gene-count files.

| Sample | Treatment | Sequencing layout |
|---|---|---|
| GSM461176 | untreated | single-end |
| GSM461177 | untreated | paired-end |
| GSM461178 | untreated | paired-end |
| GSM461182 | untreated | single-end |
| GSM461179 | treated | single-end |
| GSM461180 | treated | paired-end |
| GSM461181 | treated | paired-end |

DESeq2 estimates size factors, fits negative-binomial models, and reports p-values adjusted for multiple testing. Conceptually, the design was `~ Sequencing + Treatment`, with `untreat` as the reference for the treatment contrast. Raw integer counts are the model input; normalized counts are an output used for comparison and visualization, not a replacement input for the count model. See the [DESeq2 documentation](https://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html).

The saved report records **23,932 differential-expression rows** and **23,933 normalized-count rows**, as displayed by Galaxy. These are dataset row counts, not counts of significant genes. Header handling and the number of tested or significant genes have not been recalculated from the original tables for this archive.

## Troubleshooting The Grouping Error

My first DESeq2 workflow run failed because the dataset collection did not contain the requested `treat` label. The filenames had four underscore-separated components:

```text
GSM461176_untreat_single_featureCounts
```

The original expression, `(.*)_(.*)_(.*)`, captured only three groups. Its greedy matching absorbed the treatment token into the first group and left labels such as `single`, `paired`, and `featureCounts`. I corrected the parsing rule to `(.*)_(.*)_(.*)_(.*)`, regenerated the treatment and sequencing-layout tags, and reran DESeq2 successfully.

This was a useful workflow lesson: the statistical tool was not the source of the error. The failure originated in metadata extraction upstream, and inspecting the valid collection tags revealed the cause.

## GO Enrichment With goseq

The saved report records **12,215 GO-result rows** and **60 significantly overrepresented GO terms**. The retained Galaxy preview also displays 60 lines for the filtered dataset. These are archived observations, not newly recomputed totals. The public CSV contains four selected terms transcribed from the report: extracellular region, response to stress, oxidoreductase activity, and small molecule metabolic process.

goseq can account for gene-length-related selection bias, because long genes can have a greater chance of being called differentially expressed. Its inputs include a gene-level differential-expression indicator, gene lengths, and gene-to-category mappings. The relevant background is the eligible tested gene set, rather than every gene in a database. See [Young et al. (2010)](https://doi.org/10.1186/gb-2010-11-2-r14).

The tutorial uses an adjusted-p-value threshold of 0.05 in the enrichment workflow. The public archive does not contain a complete job-parameter export, so the exact submitted filter, background size, and multiple-testing settings still require verification from the original history. Enrichment is an association with a category, not evidence of pathway activation or a causal mechanism.

## KEGG And Visual Outputs

The reported KEGG table contained two significant rows: Glycolysis / Gluconeogenesis and the broader Metabolic pathways category. Pathview produced two pathway images, and heatmap2 produced a PDF heatmap. These outputs supported functional interpretation but were treated as exploratory summaries rather than causal proof.

The exact selected values used in the public summary figure are stored in [`results/enrichment-summary.csv`](results/enrichment-summary.csv).

These p-values are rounded values transcribed from the coursework, not newly calculated values. `14/47` and `96/871` are reported selected-gene/category-gene counts; they are not fold-enrichment estimates. The two Pathview identifiers were `dme00010` and `dme03040`. A pathway being visualized does not mean it passed the enrichment filter: the reported significant rows were `00010` and `01100`.

## Limitations

- STAR mapping failed, so no mapping percentage, splice-junction count, or STAR-derived gene-count summary is reported.
- Falco quality-control jobs failed, so no Falco quality plot is presented.
- The downstream count files were tutorial inputs rather than counts generated from my failed mapping jobs.
- The public repository contains selected enrichment values, not the complete result matrices.
