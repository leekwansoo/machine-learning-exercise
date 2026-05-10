import os
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

def make_pdf(pdf_path, title, desc_df, outliers_df, plot_files):
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(2*cm, height-2*cm, title)

    # Summary text
    c.setFont("Helvetica", 10)
    c.drawString(2*cm, height-3*cm, "This report was generated automatically from the Excel cohort dataset.")

    # Add a small table preview (top rows of describe)
    y = height - 4*cm
    c.setFont("Helvetica-Bold", 11)
    c.drawString(2*cm, y, "Summary Stats (preview)")
    y -= 0.8*cm

    c.setFont("Helvetica", 8)
    preview = desc_df.round(3).iloc[:8, :8]  # preview to fit page
    for i, row in enumerate(preview.reset_index().values.tolist()):
        line = " | ".join([str(x) for x in row])
        c.drawString(2*cm, y - i*0.45*cm, line)

    c.showPage()

    # Outliers page
    c.setFont("Helvetica-Bold", 14)
    c.drawString(2*cm, height-2*cm, "Outlier Counts (IQR method)")
    c.setFont("Helvetica", 9)

    y = height - 3*cm
    for i, (col, cnt) in enumerate(outliers_df.values.tolist()[:40]):
        c.drawString(2*cm, y - i*0.45*cm, f"{col}: {cnt}")
        if y - i*0.45*cm < 2*cm:
            c.showPage()
            y = height - 2*cm

    c.showPage()

    # Plots
    for pf in plot_files:
        if not os.path.exists(pf):
            continue
        c.setFont("Helvetica-Bold", 14)
        c.drawString(2*cm, height-2*cm, f"Plot: {os.path.basename(pf)}")
        c.drawImage(pf, 2*cm, 4*cm, width=17*cm, height=17*cm, preserveAspectRatio=True, anchor='c')
        c.showPage()

    c.save()