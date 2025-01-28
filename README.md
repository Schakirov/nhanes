# NHANES Data Downloader and Glucose Analysis

This repository contains tools for downloading and analyzing data from the **National Health and Nutrition Examination Survey ([NHANES](https://wwwn.cdc.gov/nchs/nhanes/))**, including NHANES III and surveys from 1999 to 2019. The focus is on extracting and analyzing glucose data, but the tools are flexible and can be adapted for other analyses.

---

## Features

1. **Data Downloader (`download.py`)**:
   - Downloads structured NHANES datasets (Demographics, Laboratory, Examination, etc.) for all survey cycles (1999–2019) and NHANES III.
   - Organizes the data in a structured directory format.

2. **Glucose Analysis (`analyse-glucose.py`)**:
   - Extracts glucose and age data from the downloaded NHANES datasets.
   - Visualizes:
     - A scatter plot of glucose vs. age.
     - Percentile trends (10th, 20th, ..., 90th) of glucose levels across ages.

---

## How to Use

### Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- Required Python libraries: `numpy`, `pandas`, `matplotlib`.

Install dependencies using:
```bash
pip install numpy pandas matplotlib
```

### Step 1: Download NHANES Data
Run the `download.py` script to download NHANES datasets:

```bash
python download.py
```

- The script downloads data for all survey cycles (1999–2019) and NHANES III.
- Data is saved in a structured directory:
```python
data/ 1999/ Demographics/ Laboratory/ ... 2001/ ... nhanesIII/
```

**Note**: The download requires approximately **22GB** of storage.

### Step 2: Analyze Glucose Data
Run the `analyse-glucose.py` script to process the data and visualize glucose trends:

```bash
python analyse-glucose.py
```

- The script generates:
1. A scatter plot of glucose vs. age.
2. Line plots showing percentile trends of glucose levels by age.

---

## Example Output

### Scatter Plot
A scatter plot showing glucose values against age.

### Percentile Trends
Line plots of 10th, 20th, ..., 90th percentiles of glucose levels across different ages.

---

## Customization

### Modifying `analyse-glucose.py`
You can adapt the analysis script to work with other variables in the NHANES datasets:
1. Identify the variable names for your analysis in the downloaded files.
2. Update the script to extract and analyze your variable of interest.
3. The logic for extraction and visualization is provided in the script and can be reused.

For detailed instructions on adapting the script, refer to [this guide](https://rizzoma.com/topic/0178555743735eb69cb366683cd0b9ee/0_b_c495_br98b/).

---

## Notes

**Variable Names**:
- For glucose analysis, variable names like `LBXGLUSI` (early surveys) and `LBDGLUSI` (later surveys) are used.
- NHANES III uses fixed-width fields, and glucose data is extracted from positions `1871-1876`.

**File Names**:
- Glucose data is found in files like `LAB10AM`, `L10AM_B`, etc., for different survey years.
- NHANES III stores glucose data in `lab.dat`.

If you have compiled a database of variable/file names for NHANES cycles, please share - it would be greatly appreciated!

---

## Possible Errors

- **File Paths**:
- Update file paths in the scripts to match your system's directory structure if necessary.
- **Disk Space**:
- Ensure sufficient storage (~22GB) for downloading the full NHANES datasets.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
