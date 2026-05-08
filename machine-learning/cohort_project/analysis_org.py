import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# ===============================
# 📁 CONFIG
# ===============================
INPUT_FILE = "어린이코호트 임상데이터.xlsx"
OUTPUT_FILE = "어린이코호트_자동분석리포트.xlsx"
LOG_SHEET = "ChatLog"

# ===============================
# ✅ CHAT LOG FUNCTION
# ===============================
def log_chat(message, speaker):
    new_entry = pd.DataFrame([[
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        speaker,
        message
    ]], columns=["Timestamp", "Speaker", "Message"])

    try:
        old_log = pd.read_excel(INPUT_FILE, sheet_name=LOG_SHEET, engine='openpyxl')
        updated_log = pd.concat([old_log, new_entry], ignore_index=True)
    except:
        updated_log = new_entry

    with pd.ExcelWriter(INPUT_FILE, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        updated_log.to_excel(writer, sheet_name=LOG_SHEET, index=False)

# ===============================
# ✅ DATA LOAD
# ===============================
def load_data():
    log_chat("Load data from Excel", "Copilot")
    df = pd.read_excel(INPUT_FILE, sheet_name=0, engine='openpyxl')
    return df

# ===============================
# ✅ BASIC ANALYSIS
# ===============================
def basic_analysis(df):
    log_chat("Run basic statistics (describe)", "Copilot")
    
    num_df = df.select_dtypes(include=['number'])

    # Stats
    desc = num_df.describe()

    # Correlation
    corr = num_df.corr()

    return desc, corr, num_df

# ===============================
# ✅ OUTLIER DETECTION
# ===============================
def detect_outliers(num_df):
    log_chat("Detect outliers (IQR)", "Copilot")

    outlier_summary = {}
    for col in num_df.columns:
        Q1 = num_df[col].quantile(0.25)
        Q3 = num_df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers = num_df[(num_df[col] < lower) | (num_df[col] > upper)][col]
        outlier_summary[col] = len(outliers)

    outlier_df = pd.DataFrame(list(outlier_summary.items()),
                              columns=['Column', 'Outlier_Count'])

    return outlier_df

# ===============================
# ✅ VISUALIZATION
# ===============================
def generate_plots(num_df):
    log_chat("Generate plots", "Copilot")

    plot_cols = ['ALT', 'AST', 'HbA1c', 'TSH']
    plot_files = []

    for col in plot_cols:
        if col in num_df.columns:
            plt.figure()
            num_df[col].hist()
            plt.title(f"{col} distribution")

            filename = f"{col}_hist.png"
            plt.savefig(filename)
            plt.close()

            plot_files.append(filename)

    return plot_files

# ===============================
# ✅ SAVE REPORT
# ===============================
def save_report(df, desc, corr, outliers):
    log_chat("Save analysis report", "Copilot")

    with pd.ExcelWriter(OUTPUT_FILE, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='RawData', index=False)
        desc.to_excel(writer, sheet_name='SummaryStats')
        corr.to_excel(writer, sheet_name='Correlation')
        outliers.to_excel(writer, sheet_name='Outliers')

# ===============================
# ✅ MAIN PIPELINE
# ===============================
def main():
    print("🚀 Analysis started...")

    log_chat("User started analysis.py", "User")

    df = load_data()
    desc, corr, num_df = basic_analysis(df)
    outliers = detect_outliers(num_df)
    plots = generate_plots(num_df)

    save_report(df, desc, corr, outliers)

    log_chat("Analysis completed successfully", "Copilot")

    print("✅ Done!")
    print(f"📁 Report saved: {OUTPUT_FILE}")
    print(f"📊 Plots generated: {plots}")


# ===============================
# ✅ RUN
# ===============================
if __name__ == "__main__":
    main()