# Examples
This folder contains the files for various demonstrations including:
* [Running App Locally](#running-locally)
  * [1. Clone the Git Repo](#1-clone-the-git-repo)
  * [2. Local Environment Setup](#2-local-environment-setup)
  * [3. Run the App](#3-loading-data)
* [Deployment](#deployment)
* [Data and Model Preparation](#data-prep)
  * [1. Download Calories Data](#cal-data)
  * [2. Build ML Model](#build-model)
* [Text Guide](Tool_Text_Guide.md)
* [Video Demonstration](https://drive.google.com/file/d/1hY5_HA7097HUBgR-eCphhheE8aUItCNa/view)
<a id="running-locally"></a>
## Running Locally

<a id="1-clone-the-git-repo"></a>
### 1. Clone the Git Repo
Run the following `git` command:
```bash
git clone https://github.com/parvatijay2901/LiveLite
```

<a id="2-local-environment"></a>
### 2. Local Environment Setup
To create our specified `nothing` Conda environment, run the following command:
```bash
conda env create -f environment.yml
```
Once the Conda environment is created, it can be activated by:
```bash
conda activate livelite
```
After coding inside the environment, it can be deactivated with the command:
```bash
conda deactivate
```


<a id="4-run-the-app"></a>
### 3. Run the App
A local application can be generated with the code:
```bash
conda activate livelite
python -m streamlit run LiveLite/streamlit_app/app.py 
```

See LiveLite in your local browser!

<a id="data-prep"></a>
## Data and Model Preparation

<a id="cal-data"></a>
### Download Calories Data
Download calories burned with data exercise from Harvard Health with below code:
```bash
python LiveLite/data/scripts_to_generate/harvard_health_scraped_data.py
```

<a id="build-model"></a>
### Build ML Model
Raw data must be processed first and then model must be generated on processed data. Below code will build new model:
```bash
python LiveLite/data/scripts_to_generate/data_processor.py
python LiveLite/recommendation_tool/risk_assessment/ml_build_train.py
```

<a id="deployment"></a>
## Deployment
Our app was deployed using Streamlit Sharing via https://share.streamlit.io/. 
Learn more about [deploying](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app) and [sharing](https://docs.streamlit.io/streamlit-community-cloud/get-started/share-your-app#sharing-public-apps) a public Streamlit web app.

Public Website: **[nothing.streamlit.app](https://nothing.streamlit.app/)**
