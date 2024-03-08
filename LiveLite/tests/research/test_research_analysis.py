"""
Test Suite for research analysis.

Implements a unit test class for research analysis portion.
Provides:
    - setUp: reads in NHANES and IHME data for testing plotting data.
    - test_background_information_nhanes: smoke test to see if NHANES background plot function runs.
    - test_background_information_ihme: smoke test to see if IHME background plot function runs.
    - test_violin_plot: smoke test to see if violin plot properly runs with BMI plot type.
    - test_violin_plot_weight: smoke test to see if violin plot properly runs with weight plot type.
    - test_obesity_trends: smoke test to see if NHANES obesity trends plot properly runs.
"""
import unittest

import numpy as np
import pandas as pd
import LiveLite.research.visualizations.ihme_data_analysis as ihme
import LiveLite.research.visualizations.obesity_trends_analysis as obesity
import LiveLite.research.visualizations.compare_trends_over_time as trends
import LiveLite.research.visualizations.nhanes_obesity_overweight_analysis as nhanes
# from LiveLite.research.visualizations import compare_trends_over_time as trends
# from LiveLite.research.visualizations import ihme_data_analysis as ihme
# from LiveLite.research.visualizations import nhanes_obesity_overweight_analysis as nhanes
# from LiveLite.research.visualizations import obesity_trends_analysis as obesity


class TestResearchAnalysis(unittest.TestCase):
    """
    Class defining test suite for research_analysis
    """

    def setUp(self):
        """
        Sets up the test by loading in the data.
        """
        self.nhanes_data = pd.read_parquet(
            '../../LiveLite/data/files/NHANES_Background.parquet'
        )
        self.ihme_data = pd.read_csv(
            '../../LiveLite/data/files/IHME/number-of-deaths-by-risk-factor.csv'
        )

    def test_background_information_nhanes(self):
        """
        Tests if background_information_nhanes runs and returns an object.
        """
        plt = nhanes.plot_obesity_overweight_trends(data=self.nhanes_data, years=None)
        self.assertIsInstance(plt, object)

    def test_background_information_ihme(self):
        """
        Tests if background_information_ihme runs and returns an object.
        """
        plt = ihme.plot_ihme_data(data=self.ihme_data)
        self.assertIsInstance(plt, object)

    def test_violin_plot(self):
        """
        Tests if violin_plot_manager runs and returns an object.
        """

        plt = trends.generate_violin_plot(data=self.nhanes_data)
        self.assertIsInstance(plt, object)

    def test_violin_plot_weight(self):
        plt = trends.generate_violin_plot(data=self.nhanes_data, plot_type='Weight')
        self.assertIsInstance(plt, object)

    def test_obesity_trends(self):
        """
        Tests if obesity_trends runs and returns an object.
        """
        plt = obesity.plot_obesity_trends(data=self.nhanes_data)
        self.assertIsInstance(plt, object)

    def test_invalid_data_type_background_information_nhanes(self):
        """
        Tests if plot_obesity_overweight_trends raises the type error when passed invalid data.
        """

        with self.assertRaises(TypeError):
            nhanes.plot_obesity_overweight_trends(
                data=np.array([]), years=[1999, 2017]
            )

    def test_invalid_year_type_background_information_nhanes(self):
        """
        Tests if plot_obesity_overweight_trends raises proper type error when passed
        year of invalid type.
        """
        with self.assertRaises(TypeError):
            nhanes.plot_obesity_overweight_trends(
                data=nhanes.plot_obesity_overweight_trends(
                    data=self.nhanes_data, years=1999
                )
            )

    def test_invalid_year_value_background_information_nhanes(self):
        """
        Tests if plot_obesity_overweight_trends raises the proper value
        error when passed invalid year(s)
        """
        with self.assertRaises(ValueError):
            nhanes.plot_obesity_overweight_trends(
                data=self.nhanes_data, years=[2000, 2003]
            )

    def test_invalid_data_type_ihme(self):
        """
        Tests if ihme raises type error when passed invalid data.
        """
        with self.assertRaises(TypeError):
            ihme.plot_ihme_data(np.array([]), years=[2000, 2001])

    def test_invalid_year_type_ihme(self):
        """
        Tests if ihme raises type error when passed invalid year type.
        """
        with self.assertRaises(TypeError):
            ihme.plot_ihme_data(data=self.ihme_data, years=2000)

    def test_invalid_year_value_ihme(self):
        """
        Tests if ihme raises value error when passed invalid year.
        """
        with self.assertRaises(ValueError):
            ihme.plot_ihme_data(data=self.ihme_data, years=1800)

    def test_invalid_data_type_obesity_trends(self):
        """
        Tests if obesity trends raises type error when passed invalid data type.
        """
        with self.assertRaises(TypeError):
            obesity.plot_obesity_trends(np.array([]))

    def test_invalid_year_type_obesity_trends(self):
        """
        Tests if obesity trends raises type error when passed invalid year type.
        """
        with self.assertRaises(TypeError):
            obesity.plot_obesity_trends(self.nhanes_data, years=2000)

    def test_invalid_year_value_obesity_trends(self):
        """
        Tests if obesity trends raises type error when passed invalid year.
        """
        with self.assertRaises(ValueError):
            obesity.plot_obesity_trends(self.nhanes_data, years=1800)

    def test_invalid_data_trends(self):
        """
        Tests if trend over time raises type error when passed invalid data type.
        """
        with self.assertRaises(TypeError):
            trends.generate_violin_plot(np.array([]))

    def test_invalid_year_type_trends(self):
        """
        Tests if trend over time raises type error when passed invalid year type.
        """
        with self.assertRaises(TypeError):
            trends.generate_violin_plot(self.nhanes_data, years=2000)

    def test_invalid_year_value_trends(self):
        """
        Tests if trend over time raises type error when passed invalid year.
        """
        with self.assertRaises(ValueError):
            trends.generate_violin_plot(self.nhanes_data, years=1800)

    def test_invalid_type_plottype_trends(self):
        """
        Tests if trend over time raises type error when passed invalid plottype type.
        """

        with self.assertRaises(TypeError):
            trends.generate_violin_plot(self.nhanes_data, plot_type=2)

    def test_invalid_value_plot_trend(self):
        """
        Tests if trend over time raises value error when passed invalid plottype value.
        """
        with self.assertRaises(ValueError):
            trends.generate_violin_plot(self.nhanes_data, plot_type='Height')
