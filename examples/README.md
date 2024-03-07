# Examples
This folder contains the files for various demonstrations including:
* [Running Locally](#running-locally)
  * [1. Clone the Git Repo](#1-clone-the-git-repo)
  * [2. Local Environment Setup](#2-local-environment-setup)
  * [3. Loading Data](#3-loading-data)
* [Deployment](#deployment)
* [Web Application](#web-application)


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
python -m streamlit run LiveLite/streamlit_app/Home.py 
```

See An Analysis of Nothing in your local browser!

<a id="deployment"></a>
## Deployment
Our app was deployed using Streamlit Sharing via https://share.streamlit.io/. 
Learn more about [deploying](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app) and [sharing](https://docs.streamlit.io/streamlit-community-cloud/get-started/share-your-app#sharing-public-apps) a public Streamlit web app.

Public Website: **[nothing.streamlit.app](https://nothing.streamlit.app/)**

<a id="web-application"></a>
## Web Application
* Click [here](./site_navigation.md) for a website walk-through with text.
* There is also a visual **[Video Demonstration](https://drive.google.com/file/d/1KPQyFiidUAzbk1oaAdEksbGXqCCfxCCf/view)** for accessibility.