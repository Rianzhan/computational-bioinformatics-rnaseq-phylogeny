# Evidence and Reproducibility

I assembled this public archive from my saved coursework report, run-status notes, workflow file, and embedded figures. I have separated transcribed values from original binary artefacts so that the evidence can be assessed at its actual level of detail.

| Material | Provenance | What can be verified here |
|---|---|---|
| RNA-seq sample table | Saved report; GTN training data | Seven sample assignments, including GSM461182 as single-end |
| Enrichment CSV | Rounded values transcribed from the report | Four selected GO rows and two KEGG rows; not the complete output |
| Enrichment figure | Newly plotted from the public CSV | Plot values and labels can be rebuilt with the included script |
| Four phylogeny PNGs | Exact embedded image bytes extracted from the coursework | Original tree drawing and visible labels; no missing labels have been invented |
| Galaxy workflow | Retained GTN upstream workflow | Workflow structure, tools, creator metadata, and license |
| Portfolio PDF | Newly written public summary | Methods, selected evidence, and explicit limitations |

## Corrections Made During Archiving

- **RNA-seq rows:** 23,932 DESeq2 rows are not 23,932 significant genes. Galaxy row counts have not been re-counted from raw tables here.
- **GO total:** the report and full-size dataset preview both record 60 filtered rows. This archived count has not been independently recomputed from the full table.
- **Phylogeny sequence count:** the report's prose says five sequences, but the MEGA-generated ML caption records 10 sequences and 245 sites. The latter is the direct software record.
- **Phylogeny support:** missing tip labels mean that a 99 value next to OsaGPX1 cannot be treated as 99 support for a rice-barley clade. Some original coursework interpretations have been withdrawn rather than repeated.
- **IQ-TREE:** the job failed. A server-load or format explanation was speculative, so no confirmed cause is asserted here.

## Available and Missing Materials

The original Galaxy session was no longer authenticated when this archive was assembled, so standalone DESeq2 plots, the heatmap, full enrichment tables, and a repaired downstream workflow export were not recovered. Their earlier completion is documented in the saved report, but their contents cannot be inspected in full in this repository. I have not used a tutorial's example plot as a substitute for my own output.

The public release excludes original DOCX files and interface screenshots containing account information. Raw reads, BAM files, full count matrices, aligned protein sequences, and Newick trees are not included. Consequently this is an educational research archive with a reproducible summary plot, not a complete end-to-end reproducibility package.

## Rebuilding the Summary Figure

Run `python scripts/build_enrichment_figure.py` after installing `reportlab` and `pypdfium2`. This uses only `rnaseq/results/enrichment-summary.csv` and regenerates the public PNG and vector PDF. No Galaxy credentials or data downloads are required.
