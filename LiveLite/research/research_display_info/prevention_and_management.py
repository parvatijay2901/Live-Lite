"""
Module that displays weight change overtime of the US population and provides commentary
on prevention and management of obesity.

Provides:
    - display_weight_trends_over_time: Plots distribution of weight over time.
    - display_prevention_and_management: Calls display_weight_trends_over_time to plot in streamlit.
    Provides additional text commentary.
"""

import streamlit as st
import LiveLite  # pylint: disable=import-error


def display_weight_trends_over_time(data, years=None):
    """
    Plots and provides text commentary on BMI over time.
    Raises type or value error through plotting function if invalid data or year is passed.
    Args:
        data: NHANES dataframe.
        years: List of years to plot.

    Returns: None

    """
    fig = LiveLite.generate_violin_plot(data, plot_type="Weight", years=years)
    st.markdown("""
        In the chart below, BMI and weight are plotted along with their general distributions in
        the form of a violin plot. We can observe that over time
         BMI and weight have increased over time.
    """)
    LiveLite.add_blank_lines()
    _, col12, _ = st.columns([0.5, 2, 0.5])
    with col12:
        st.plotly_chart(fig, use_container_width=True)


def display_prevention_and_management():
    """
    Provides additional commentary on preventing and managing obesity.
    Raises no exceptions.
    Returns: None

    """
    st.markdown("<h4 style='color:gold;'>Treatment</h4>", unsafe_allow_html=True)
    st.markdown(
        """
        Treatment of obesity can generally be divided into two stages.
        The initial treatment and subsequent treatments.
        While we cannot recommend any form of medical advice,
        we can lay out the general process of common weight-loss therapies.
        """
    )
    display_weight_trends_over_time(st.session_state['data_nhanes'], years=[1999, 2017])

    st.markdown("<h4 style='color:gold;'>Initial Treatments</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 0.5])
    with col1:
        st.markdown(
            """
            Initial treatments of obesity fall under comprehensive lifestyle changes.
            These changes involve a combination of diet, physical activity (exercise),
            and modification of the individuals behavior (behavior therapy).
            Modification of behavior refers to facilitating adherence to diet and exercise programs.
            Examples of behavior therapy are modifying and monitoring food intake,
            modifying physical activity, and to address
            causes and stimuli that may trigger eating / overeating.

            Usually these treatments involve discussing with a medical professional
            and setting weight-loss goals and behavior goals. An example of dietary weight-loss
            goals would be reducing energy intake by a certain amount of kcal/day
            which may done through portion control, food provisions, or even diet instruction.

            Exercise is perhaps the most well-known aspect of weight-loss.
            It is generally recommended that an individual perform some form of exercise
            for at least half an hour, for at least five days a week to simply prevent weight
            gain (Piercy et al., 2018). Behavior goals are equally important.
            These goals should within the individuals control
            and also be SMART (Specific, Measurable, Achievable, Reasonable, and Time-bound).
            A simple example of a behavior goal would be to eat junk /
            fast food less than once per week.

            Those who could benefit from weight loss would benefit from counseling on
            diet, exercise, and goals for weight loss.
            """
        )
    with col2:
        st.image("LiveLite/streamlit_app/images/initial_treatment.png", use_column_width=True)

    st.markdown("<h4 style='color:gold;'>Subsequent Treatments</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 0.4])
    with col1:
        st.markdown(
            """
            If the individual cannot reach their weight-loss goals from their
            comprehensive lifestyle changes in the initial treatment, other options such as
            pharmacologic, medical devices, and surgical options exist.
            Most common drug therapy options are GLP-1 agonists which result in a
            complex downstream effect on various organ functions.
            One of these effects is that these drugs decrease appetite and increase satiety,
            which ideally leads to less consumption of food.

            Medical devices is a broad term for the various treatment options for those
            unwilling to undergo bariatric surgeries. Some examples of some medical
            devices that may be prescribed are the intragastric balloonand hydrogels.
            The intragastric balloon are balloons filled with saline
            that are placed into the stomach -
            which then produces the feeling of being satiated.
            Hydrogels are products taken orally which then expand in the stomach
            to produce a feeling of satiety.

            Lastly, there is bariatric surgery. Bariatric surgery refers to a group
            of techniques used to treat obesity. Perhaps the most commonly known is gastric bypass
            which essentially involves the creation of smaller stomach
            and reconnecting the small intestine (and the rest of the GI tract) to the
            new, smaller, stomach pouch, bypassing the stomach - hence the name.
            """
        )
    with col2:
        st.image("LiveLite/streamlit_app/images/medications_obesity.png", use_column_width=True)

    st.markdown("<h4 style='color:gold;'>Not Recommended Treatments</h4>", unsafe_allow_html=True)
    st.markdown(
        """
        Liposuction is another option available for individuals seeking to lose weight.
        However, this technique has mixed reviews from medical professionals.

        This is due to studies that have shown that weight loss by liposuction does
        not seem to bring the benefits that usually come with weight loss.
        For example, a study that examined the effects of liposuction found that
        although subject waist circumference improved, no improvements in risk
        factors of coronary heart disease such as high blood pressure or
        glucose presence in plasma were observed (Klein et al., 2004).
        """
    )

    st.markdown("<h4 style='color:gold;'>Prevention</h4>", unsafe_allow_html=True)
    st.markdown(
        """
        Preventing obesity generally aligns with the initial treatments of obesity,
        but in a less extreme form.
        Maintaining a well-balanced diet, accompanied with healthy eating habits,
        and regular physical activity is the
        best method for ensuring a healthy body and preventing obesity.

        Understanding your current health status and potential risk for obesity can
        provide valuable insights for personalized prevention strategies.
        Click the button below to assess your current risk and gain personalized
        insights into maintaining a healthy weight.
        """
    )
