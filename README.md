# ATS-APP

## Setting up the Conda Environment

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution) if you don't have it installed already.
2. Create a new conda environment with Python 3.8 (or your preferred version):
   ```bash
   conda create --name ats-app python=3.8
   ```
3. Activate the conda environment:
   ```bash
   conda activate ats-app
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Make sure the conda environment is activated:
   ```bash
   conda activate ats-app
   ```
2. Run the `app.py` script:
   ```bash
   python app.py
   ```
