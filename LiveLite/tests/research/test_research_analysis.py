"""
Test Suite for research analysis.
"""
import unittest

import numpy as np
import pandas as pd
from LiveLite.research.visualizations import compare_trends_over_time as trends
from LiveLite.research.visualizations import ihme_data_analysis as ihme
from LiveLite.research.visualizations import nhanes_obesity_overweight_analysis as nhanes
from LiveLite.research.visualizations import obesity_trends_analysis as obesity


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
        plt = nhanes.background_information_nhanes(data=self.nhanes_data, years=None)
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

    def test_obesity_trends(self):
        """
        Tests if obesity_trends runs and returns an object.
        """
        plt = obesity.plot_obesity_trends(data=self.nhanes_data)
        self.assertIsInstance(plt, object)

    def test_invalid_data_background_information_nhanes(self):
        """
        Tests if background_information_nhanes raises the type error when passed invalid data.
        """

        with self.assertRaises(TypeError):
            nhanes.background_information_nhanes(
                data=np.array([]), years=[1999, 2017]
            )

    def test_invalid_year_background_information_nhanes(self):
        """
        Tests if background_information_nhanes raises the proper value
        error when passed invalid year(s)
        """
        with self.assertRaises(ValueError):
            nhanes.background_information_nhanes(
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

    def test_invalid_data_obesity_trends(self):
        """
        Tests if obesity trends raises type error when passed invalid data type.
        """
        with self.assertRaises(TypeError):
            obesity.plot_obesity_trends(np.array([]))

    def test_invalid_year_obesity_trends(self):
        """
        Tests if obesity trends raises type error when passed invalid year type.
        """
        with self.assertRaises(TypeError):
            obesity.plot_obesity_trends(self.nhanes_data, years=2000)

    def test_invalid_data_trends(self):
        """
        Tests if trend over time raises type error when passed invalid data type.
        """
        with self.assertRaises(TypeError):
            trends.generate_violin_plot(np.array([]))

    def test_invalid_year_trends(self):
        """
        Tests if trend over time raises type error when passed invalid year type.
        """
        with self.assertRaises(TypeError):
            trends.generate_violin_plot(self.nhanes_data, years=2000)

    def test_invalid_plottype_trends(self):
        """
        Tests if trend over time raises type error when passed invalid plottype type.
        """

        with self.assertRaises(TypeError):
            trends.generate_violin_plot(self.nhanes_data, plot_type=2)

    def test_invalid_plot_trend(self):
        """
        Tests if trend over time raises value error when passed invalid plottype.
        """
        with self.assertRaises(ValueError):
            trends.generate_violin_plot(self.nhanes_data, plot_type='Height')
