import streamlit as st
import LiveLite
import pandas as pd

def display_nhanes_obesity_overweight_analysis(data):
    fig = LiveLite.plot_obesity_overweight_trends(data) 
    st.markdown("""In the charts plotted below, we can observe that, in the United States alone, the proportion of 
                overweight (including obese) and obese individuals has rapidly increased since 1999.""")
    st.plotly_chart(fig, use_container_width=True)
    
def display_obesity_trends(data):
    LiveLite.add_blank_lines(2)
    st.markdown("From the chart below, we can also observe that for both males and females, obesity has only increased since 1999.") 
    fig = LiveLite.plot_obesity_trends(data)
    st.plotly_chart(fig, use_container_width=True)

def display_health_consequences():
    st.markdown("""Being overweight or obese is associated with grave morbidity and mortality. 
                Obesity in adults has been previously shown to be associated with a drastic reduction in life expectancy 
                (Grover et al., 2015). Many studies across Europe and North America have shown that mortality increased by 
                30 percent for each 5kg/m<sup>2</sup> increase in BMI (Prospective Studies Collaboration, 2009)""", 
                unsafe_allow_html=True)
    
    data_NHANES = pd.read_csv("LiveLite/data/input_files/NHANES_Background.csv", low_memory=False)
    display_nhanes_obesity_overweight_analysis(data_NHANES)
    display_obesity_trends(data_NHANES)
    
    st.markdown("""Obesity has drastic implications on morbidity for obese individuals. The risks we will discuss can be categorized 
                into the following categories:""")
    st.markdown("""
                - Metabolic
                - Cardiovascular
                - Respiratory
                """)
    st.markdown("<h4 style='color:gold;'>Metabolic</h4>", unsafe_allow_html=True)
    st.markdown("""Increased BMI and obesity are also strongly associated with Type 2 Diabetes mellitus. Similar to obesity, 
                type 2 diabetes has been dramatically increasing in the United States, with the most common feature being 
                that most patients who develop type 2 diabetes are of increased weight (Sullivan et al., 2005)""")
    col1, _, col3 = st.columns([2, 0.1, 0.7])
    with col1:
        st.markdown("<h4 style='color:gold;'>Cardiovascular</h4>", unsafe_allow_html=True)
        st.markdown("""Blood pressures is also often increased in obese individuals and puts them at risk of heart disease. 
                    Obesity has been shown to be associated with increased risk of heart conditions such as coronary heart disease, 
                    heart failure, and atrial fibrillation (Aune et al., 2016). A well known study in the field known as the 
                    Framingham Heart Study showed that every unit increase in BMI was associated with about a 5 percent increase risk 
                    for developing atrial fibrillation (Wang et al., 2004). In the same study, the risk of heart failure was also 
                    examined and was found that the risk of heart failure increased about two-fold in individuals with obesity 
                    compared to their non-obese counterparts (Wang et al., 2004).""")
    with col3:
        st.image("LiveLite/streamlit_app/images/obesity_consequences.png",width=300)
        
    st.markdown("<h4 style='color:gold'>Respiratory</h4>", unsafe_allow_html=True)
    st.markdown("""The respiratory related health consequences of obesity were recently highlighted during the course of COVID-19 
                global pandemic. A study in New York City during the pandemic showed that patients with COVID-19 who were obese 
                were more at risk of requiring intuition and more at risk of mortality (Anderson et al., 2020). Another study 
                showed that obesity was associated with 113 percent higher risk of hospitalization, 74 percent higher risk of 
                ICU admission, and had a 48 percent higher risk of mortality (Popkin et al., 2020).""")
    st.markdown("""These risks are not tied to only COVID. Other respiratory conditions have similar increased risks of morbidity 
                in individuals who are obese versus non-obese. For example, adult obesity patients were found to have between two 
                to fourfold increased risk of being hospitalized for asthma exacerbations compared to their non-obese 
                counterparts (Holguin et al., 2011), (Mosen et al., 2008).""")