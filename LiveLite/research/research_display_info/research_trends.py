import streamlit as st
import pandas as pd
import research

def display_ihme_data_analysis(data, years):
    fig = research.plot_ihme_data(data, years=years) 
    st.plotly_chart(fig, use_container_width=True, width=1200, height=600)
    st.markdown("""From the figure above, we can observe that Deaths attributed to high body-mass index (BMI) 
                has rapidly increased since 1990 - going from around 4.3 million to around 10 million.""")
    
def display_nhanes_obesity_overweight_analysis(data):
    fig = research.plot_obesity_overweight_trends(data) 
    st.pyplot(fig) # Seaborn -> plotly
    st.markdown("""In the figure above, we can observe that, in the United States alone, the proportion of 
                overweight (including obese) and obese individuals has rapidly increased since 1999.""")
    
def display_obesity_trends(data):
    fig = research.plot_obesity_trends(data)
    st.pyplot(fig) # Seaborn -> plotly
    st.markdown("From the figure above, we can observe that for both males and females, obesity has only increased since 1999.")    

def display_trends_over_time(data, years):
    fig = research.generate_violin_plot(data, years=years)
    st.plotly_chart(fig) # Move this to the centre?
    st.markdown("""The figure above displays the overall distribution of BMI in the NHANES data set between 1999 and 2017. 
                The mean BMI in 1999 was 24.89. The mean BMI in 2017 was 26.58. From 1999 to 2017, there was a 6.76% increase in 
                overall BMI in the United States. In addition, in 1999, the average BMI was still under the category of 
                'Healthy Weight'. However, in 2017 with the increase in BMI to 26.58, the average BMI is no longer considered 
                'Healthy' and is now firmly in the 'Overweight' category.""")
    
def display_research_trends():
    st.markdown("""According to data published by the Institute for Health Metrics and Evaluation (IHME), 
                obesity is a major risk factor for mortality in not just the United States but globally as well.""")
    
    data_IHME = pd.read_csv("./data/input_files/IHME/number-of-deaths-by-risk-factor.csv")
    data_NHANES = pd.read_csv("./data/input_files/NHANES_Background.csv", low_memory=False)
    
    display_ihme_data_analysis(data_IHME, years = [1990, 2019])
    display_nhanes_obesity_overweight_analysis(data_NHANES)
    display_obesity_trends(data_NHANES)
    display_trends_over_time(data_NHANES, years = [1999, 2017])