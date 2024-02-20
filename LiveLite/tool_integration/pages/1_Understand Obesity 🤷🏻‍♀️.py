import streamlit as st
from streamlit_extras.switch_page_button import switch_page 

col0, col1 = st.columns([10, 0.5])
with col1:
    if st.button("🡆", use_container_width=True):
        switch_page("Home🏠")
        

st.markdown("""<div style="text-align:center;"><h2><span style='color:gold;'>Comprehensive Guide to Obesity: </span>Understanding, Prevention, and Management</h2></div>""", unsafe_allow_html=True)

st.markdown('\n')

st.markdown("<h3 style='color:gold;'>Background on Obesity</h3>", unsafe_allow_html=True)
st.markdown("Obesity is ever-growing issue in the modern world. Defined as 'weight that is considered higher than what is considered healthy for a given height' by the CDC. Body Mass Index (BMI) is a general method of defining obesity. BMI in the ranges of 25 to 29.9 kg/m<sup>2</sup> are considered overweight and BMI greater than or equal to 30 kg/m<sup>2</sup> are considered obese. Obesity is nowadays described as a chronic disease that is only increasing in prevalence in all ages and currently now considered to be an ongoing global epidemic of obesity.", unsafe_allow_html=True)
st.markdown("Using the NHANES data collected between the years of 1999 to 2018, we can observe that the prevalence of obesity in the United States has progressively increased from 30.5 to 42.4 %.", unsafe_allow_html=True)

st.markdown('\n')

st.markdown("<h3 style='color:gold;'>Health Consequences of Obesity</h3>", unsafe_allow_html=True)
st.markdown("Being overweight or obese is associated with grave morbidity and mortality. Obesity in adults has been previously shown to be associated with a drastic reduction in life expectancy (Grover et al., 2015). Many studies across Europe and North America have shown that mortality increased by 30 percent for each 5kg/m<sup>2</sup> increase in BMI (Prospective Studies Collaboration, 2009)", unsafe_allow_html=True)
st.markdown("Obesity has drastic implications on morbidity for obese individuals. The risks we will discuss can be categorized into the following categories:")
st.markdown("""
- Metabolic
- Cardiovascular
- Respiratory
""")

st.markdown("<h4 style='color:gold;'>Health Consequences of Obesity</h4>", unsafe_allow_html=True)
st.markdown("Increased BMI and obesity are also strongly associated with Type 2 Diabetes mellitus. Similar to obesity, type 2 diabetes has been dramatically increasing in the United States, with the most common feature being that most patients who develop type 2 diabetes are of increased weight (Sullivan et al., 2005)")

st.markdown("<h4 style='color:gold;'>Cardiovascular</h4>", unsafe_allow_html=True)
st.markdown("Blood pressures is also often increased in obese individuals and puts them at risk of heart disease. Obesity has been shown to be associated with increased risk of heart conditions such as coronary heart disease, heart failure, and atrial fibrillation (Aune et al., 2016). A well known study in the field known as the Framingham Heart Study showed that every unit increase in BMI was associated with about a 5 percent increase risk for developing atrial fibrillation (Wang et al., 2004). In the same study, the risk of heart failure was also examined and was found that the risk of heart failure increased about two-fold in individuals with obesity compared to their non-obese counterparts (Wang et al., 2004).")

st.markdown("<h4 style='color:gold'>Respiratory</h4>", unsafe_allow_html=True)
st.markdown("The respiratory related health consequences of obesity were recently highlighted during the course of COVID-19 global pandemic. A study in New York City during the pandemic showed that patients with COVID-19 who were obese were more at risk of requiring intuition and more at risk of mortality (Anderson et al., 2020). Another study showed that obesity was associated with 113 percent higher risk of hospitalization, 74 percent higher risk of ICU admission, and had a 48 percent higher risk of mortality (Popkin et al., 2020).")
st.markdown("These risks are not tied to only COVID. Other respiratory conditions have similar increased risks of morbidity in individuals who are obese versus non-obese. For example, adult obesity patients were found to have between two to fourfold increased risk of being hospitalized for asthma exacerbations compared to their non-obese counterparts (Holguin et al., 2011), (Mosen et al., 2008).")

st.markdown("<h3 style='color:gold'>Sources</h3>", unsafe_allow_html=True)
st.markdown("Anderson, M. R., Geleris, J., Anderson, D. R., Zucker, J., Nobel, Y. R., Freedberg, D., Small-Saunders, J., Rajagopalan, K. N., Greendyk, R., Chae, S.-R., Natarajan, K., Roh, D., Edwin, E., Gallagher, D., Podolanczuk, A., Barr, R. G., Ferrante, A. W., & Baldwin, M. R. (2020). Body Mass Index and Risk for Intubation or Death in SARS-CoV-2 Infection: A Retrospective Cohort Study. Annals of Internal Medicine, 173(10), 782–790. [https://doi.org/10.7326/M20-3214](https://doi.org/10.7326/M20-3214)")
st.markdown("Aune, D., Sen, A., Norat, T., Janszky, I., Romundstad, P., Tonstad, S., & Vatten, L. J. (2016). Body Mass Index, Abdominal Fatness, and Heart Failure Incidence and Mortality: A Systematic Review and Dose-Response Meta-Analysis of Prospective Studies. Circulation, 133(7), 639–649. [https://doi.org/10.1161/CIRCULATIONAHA.115.016801](https://doi.org/10.1161/CIRCULATIONAHA.115.016801)")
st.markdown("Grover, S. A., Kaouache, M., Rempel, P., Joseph, L., Dawes, M., Lau, D. C. W., & Lowensteyn, I. (2015). Years of life lost and healthy life-years lost from diabetes and cardiovascular disease in overweight and obese people: A modelling study. The Lancet. Diabetes & Endocrinology, 3(2), 114–122. [https://doi.org/10.1016/S2213-8587(14)70229-3](https://doi.org/10.1016/S2213-8587(14)70229-3)")
st.markdown("Popkin, B. M., Du, S., Green, W. D., Beck, M. A., Algaith, T., Herbst, C. H., Alsukait, R. F., Alluhidan, M., Alazemi, N., & Shekar, M. (2020). Individuals with obesity and COVID-19: A global perspective on the epidemiology and biological relationships. Obesity Reviews: An Official Journal of the International Association for the Study of Obesity, 21(11), e13128. [https://doi.org/10.1111/obr.13128](https://doi.org/10.1111/obr.13128)")
st.markdown("Prospective Studies Collaboration. (2009). Body-mass index and cause-specific mortality in 900 000 adults: Collaborative analyses of 57 prospective studies. Lancet, 373(9669), 1083–1096.[https://doi.org/10.1016/S0140-6736(09)60318-4](https://doi.org/10.1016/S0140-6736(09)60318-4)")
st.markdown("Sullivan, P. W., Morrato, E. H., Ghushchyan, V., Wyatt, H. R., & Hill, J. O. (2005). Obesity, inactivity, and the prevalence of diabetes and diabetes-related cardiovascular comorbidities in the U.S., 2000-2002. Diabetes Care, 28(7), 1599–1603. [https://doi.org/10.2337/diacare.28.7.1599](https://doi.org/10.2337/diacare.28.7.1599)")
st.markdown("Wang, T. J., Parise, H., Levy, D., D’Agostino, R. B., Wolf, P. A., Vasan, R. S., & Benjamin, E. J. (2004). Obesity and the risk of new-onset atrial fibrillation. JAMA, 292(20), 2471–2477. [https://doi.org/10.1001/jama.292.20.2471](https://doi.org/10.1001/jama.292.20.2471)")




