# Key Results and Run Status

## Sample Assignment

| Sample | Treatment | Sequencing layout |
|---|---|---|
| GSM461176 | untreated | single-end |
| GSM461177 | untreated | paired-end |
| GSM461178 | untreated | paired-end |
| GSM461182 | untreated | single-end |
| GSM461179 | treated | single-end |
| GSM461180 | treated | paired-end |
| GSM461181 | treated | paired-end |

## Completed Outputs

| Analysis | Reported output |
|---|---|
| DESeq2 result | 23,932 differential-expression rows and 7 columns |
| Normalized counts | 23,933 normalized-count rows and 8 columns |
| DESeq2 plots | Five-page PDF generated in Galaxy |
| goseq GO result | 12,215 GO-result rows and 9 columns |
| Overrepresented GO result | 60 significantly overrepresented GO terms reported; the retained dataset preview displays 60 lines |
| KEGG enrichment | Two significant pathway rows |
| Pathview | Two pathway PNG outputs |
| heatmap2 | PDF heatmap generated successfully |

## Incomplete Outputs

| Step | Status and consequence |
|---|---|
| Falco | Falco quality-control jobs failed; no quality plot was interpreted. |
| STAR | STAR mapping failed; no mapping statistics were reported. |
| featureCounts from STAR | Not run successfully because no usable STAR BAM was available. |

The downstream analysis used GTN-provided featureCounts files. This preserves the learning objective for DESeq2 and enrichment while keeping the incomplete upstream branch visible.

## Selected Enrichment Results

The public CSV contains four selected GO terms and two reported KEGG pathway rows. These are a compact record of the successful enrichment outputs, not a replacement for the complete Galaxy tables.

![Selected reported enrichment values](../figures/selected-enrichment-results.png)

Figure: A new visualization of values transcribed from the coursework, not a recovered Galaxy plot. Lower adjusted p-values indicate stronger evidence against the enrichment null hypothesis, not larger biological effects. GO terms and KEGG pathways are shown in separate panels and should not be ranked as a single family of tests.
