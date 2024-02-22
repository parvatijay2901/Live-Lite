import streamlit as st
import os, sys

path = '././.'
sys.path.append(os.path.abspath(path))
from research.visualizations.research_analysis import background_information_ihme, background_information_nhanes, obesity_trends, violin_plot_manager

def display_background_information_ihme(years):
    fig = background_information_ihme(years=years) 
    st.plotly_chart(fig, use_container_width=True, width=1200, height=600)
    st.markdown("From the figure above, we can observe that Deaths attributed to high body-mass index (BMI) has rapidly increased since 1990 - going from around 4.3 million to around 10 million.")
    
def display_background_information_nhanes():
    fig = background_information_nhanes() 
    st.pyplot(fig) # Seaborn -> plotly
    st.markdown("In the figure above, we can observe that, in the United States alone, the proportion of overweight (including obese) and obese individuals has rapidly increased since 1999.")
    
def display_obesity_trends():
    fig = obesity_trends()
    st.pyplot(fig) # Seaborn -> plotly
    st.markdown("From the figure above, we can observe that for both males and females, obesity has only increased since 1999.")    

def display_violin_plot(years):
    fig = violin_plot_manager(years=years)
    st.plotly_chart(fig) # Move this to the centre?
    st.markdown("The figure above displays the overall distribution of BMI in the NHANES data set between 1999 and 2017. The mean BMI in 1999 was 24.89. The mean BMI in 2017 was 26.58. From 1999 to 2017, there was a 6.76% increase in overall BMI in the United States. In addition, in 1999, the average BMI was still under the category of 'Healthy Weight'. However, in 2017 with the increase in BMI to 26.58, the average BMI is no longer considered 'Healthy' and is now firmly in the 'Overweight' category.")
    
def display_research_trends():
    st.markdown("According to data published by the Institute for Health Metrics and Evaluation (IHME), obesity is a major risk factor for mortality in not just the United States but globally as well.")
    
    display_background_information_ihme(years = [1990, 2019])
        
    display_background_information_nhanes()
    
    display_obesity_trends()
    
    display_violin_plot(years = [1999, 2017])