from pathlib import Path
import pandas as pd
import openpyxl
from zipfile import BadZipFile


def _detect_excel_engine(excel_path: Path) -> str:
    """Detect likely Excel engine using file signature and extension."""
    ext = excel_path.suffix.lower()
    with excel_path.open("rb") as f:
        signature = f.read(8)

    is_zip = signature.startswith(b"PK\x03\x04")
    is_ole = signature.startswith(b"\xD0\xCF\x11\xE0")

    # Signature takes precedence over extension for mislabeled files.
    if is_zip:
        return "openpyxl"
    if is_ole:
        return "xlrd"

    if ext in {".xlsx", ".xlsm"}:
        return "openpyxl"
    if ext == ".xls":
        return "xlrd"

    raise ValueError(
        f"Unsupported Excel extension: {ext}. Use .xls, .xlsx, or .xlsm"
    )

def convert_excel_to_csv(excel_file_path):
    excel_path = Path(excel_file_path)

    if not excel_path.exists():
        raise FileNotFoundError(f"File not found: {excel_path.resolve()}")

    if excel_path.stat().st_size == 0:
        raise ValueError(
            f"{excel_path} is empty (0 bytes). Save/export the Excel file again and retry."
        )

    engine = _detect_excel_engine(excel_path)

    try:
        excel_file = pd.ExcelFile(excel_path, engine=engine)
    except ImportError as e:
        if engine == "xlrd":
            raise ImportError(
                "Reading .xls files requires 'xlrd'. Install it with: pip install xlrd"
            ) from e
        raise
    except BadZipFile as e:
        # If extension/signature mismatch slips through, retry once with xlrd.
        if engine == "openpyxl":
            try:
                excel_file = pd.ExcelFile(excel_path, engine="xlrd")
                engine = "xlrd"
            except ImportError as ie:
                raise ImportError(
                    "This file is not a valid .xlsx zip workbook. It may be .xls. "
                    "Install 'xlrd' with: pip install xlrd"
                ) from ie
            except Exception:
                raise e
        else:
            raise

    csv_files = []
    for sheet in excel_file.sheet_names:
        df = pd.read_excel(excel_path, sheet_name=sheet, engine=engine)
        output_csv = excel_path.with_name(f"{excel_path.stem}_{sheet}.csv")
        df.to_csv(output_csv, index=False, encoding="utf-8-sig")
        csv_files.append(output_csv)
    return csv_files