Deforestation Detection Using Satellite Imagery (Deep Learning, Synthetic Data)

This project simulates deforestation detection using synthetic satellite-like data and applies deep learning methods to classify land cover changes. By generating synthetic RED and NIR reflectance bands, the project computes NDVI before and after disturbance to label samples as deforested or non-deforested.

Features

Generates synthetic tabular dataset with >100 samples.

Includes before/after reflectance bands (RED, NIR).

Computes NDVI before, NDVI after, and NDVI difference.

Labels data automatically as deforested (1) or not deforested (0).

Saves dataset in both Excel (.xlsx) and CSV (.csv) formats.

Ready for use in machine learning or deep learning workflows.

Installation

Clone this repository and install dependencies:

git clone https://github.com/yourusername/Deforestation-Detection-Using-Satellite-Imagery-Deep-Learning.git
cd Deforestation-Detection-Using-Satellite-Imagery-Deep-Learning
pip install -r requirements.txt


Dependencies:

Python 3.8+

NumPy

Pandas

OpenPyXL (for Excel export)

Usage

Generate the dataset by running:

python generate_synthetic_deforestation_dataset.py --n 300 --seed 42 --out outputs


Arguments:

--n: Number of samples (default: 300, must be >100).

--seed: Random seed for reproducibility (default: 42).

--out: Output folder (default: outputs).

Example Output

outputs/synthetic_deforestation_dataset.xlsx

outputs/synthetic_deforestation_dataset.csv

Dataset Columns

sample_id

RED_before, NIR_before

RED_after, NIR_after

NDVI_before, NDVI_after, NDVI_diff

label_deforested (1 = deforested, 0 = not deforested)

Applications

Benchmarking deforestation detection models.

Experimenting with vegetation indices (NDVI).

Testing deep learning pipelines without requiring real imagery.

Author

Agbozu Ebingiye Nelvin

License

This project is released under the MIT License. See LICENSE for details.
