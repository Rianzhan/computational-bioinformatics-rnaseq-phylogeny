"""Plot the selected, rounded coursework values without recomputing enrichment."""

import csv
import math
from pathlib import Path

import pypdfium2 as pdfium
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from reportlab.graphics.shapes import Drawing, String
from reportlab.lib.colors import HexColor
from reportlab.pdfgen.canvas import Canvas


ROOT = Path(__file__).resolve().parents[1]


def panel(rows, title, color, y, height):
    drawing = Drawing(780, 600)
    drawing.add(String(32, y + height + 28, title, fontName="Helvetica-Bold", fontSize=13))
    ordered = list(reversed(rows))
    chart = HorizontalBarChart()
    chart.x, chart.y, chart.width, chart.height = 365, y, 300, height
    chart.data = [[-math.log10(float(row["adjusted_p_value"])) for row in ordered]]
    chart.categoryAxis.categoryNames = [f'{row["identifier"]}  {row["term"]}' for row in ordered]
    chart.categoryAxis.labels.fontName = "Helvetica"
    chart.categoryAxis.labels.fontSize = 9
    chart.categoryAxis.labels.boxAnchor = "e"
    chart.categoryAxis.labels.dx = -8
    chart.categoryAxis.strokeWidth = 0
    chart.valueAxis.valueMin, chart.valueAxis.valueMax, chart.valueAxis.valueStep = 0, 5, 1
    chart.valueAxis.labels.fontSize = 9
    chart.valueAxis.strokeColor = HexColor("#9AA4A6")
    chart.valueAxis.gridStrokeColor = HexColor("#E4E8E8")
    chart.valueAxis.visibleGrid = True
    chart.bars[0].fillColor = HexColor(color)
    chart.bars[0].strokeColor = None
    chart.barWidth, chart.groupSpacing = 15, 13
    drawing.add(chart)
    step = height / len(ordered)
    for i, row in enumerate(ordered):
        drawing.add(String(685, y + (i + 0.5) * step - 3, row["adjusted_p_value"], fontSize=9))
    drawing.add(String(365, y - 30, "-log10(adjusted p-value)", fontSize=9))
    drawing.add(String(685, y + height + 8, "Reported padj", fontSize=9))
    return drawing


def main():
    source = ROOT / "rnaseq/results/enrichment-summary.csv"
    with source.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 6 or any(not 0 < float(row["adjusted_p_value"]) <= 1 for row in rows):
        raise ValueError("Expected six valid selected enrichment rows")
    fig = Drawing(780, 600)
    fig.add(String(32, 565, "Selected enrichment results", fontName="Helvetica-Bold", fontSize=23))
    fig.add(String(32, 542, "Values transcribed from the saved Galaxy coursework report", fontSize=11,
                   fillColor=HexColor("#526267")))
    fig.add(panel([r for r in rows if r["source"] == "GO"], "A   Gene Ontology (four selected terms)", "#187B80", 310, 168))
    fig.add(panel([r for r in rows if r["source"] == "KEGG"], "B   KEGG (two reported pathways)", "#BD5D4F", 115, 100))
    fig.add(String(32, 39, "Selected results only. Bar lengths show statistical evidence, not biological effect size.",
                   fontSize=10, fillColor=HexColor("#526267")))
    fig.add(String(32, 22, "GO and KEGG are separate analyses. Rounded values are preserved as reported.",
                   fontSize=10, fillColor=HexColor("#526267")))
    output = ROOT / "rnaseq/figures"
    output.mkdir(parents=True, exist_ok=True)
    pdf = output / "selected-enrichment-results.pdf"
    canvas = Canvas(str(pdf), pagesize=(780, 600), invariant=1)
    canvas.setTitle("Selected reported enrichment results")
    canvas.setAuthor("Rianzhan")
    canvas.setCreator("Enrichment summary plot")
    renderPDF.draw(fig, canvas, 0, 0)
    canvas.showPage()
    canvas.save()
    document = pdfium.PdfDocument(str(pdf))
    page = document[0]
    bitmap = page.render(scale=3)
    bitmap.to_pil().save(output / "selected-enrichment-results.png")
    bitmap.close()
    page.close()
    document.close()
    print("Selected enrichment figure created from six CSV rows")


if __name__ == "__main__":
    main()
