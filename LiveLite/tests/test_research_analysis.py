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
from pathlib import Path

import numpy as np
import pandas as pd
from LiveLite import plot_ihme_data
from LiveLite import plot_obesity_trends
from LiveLite import plot_obesity_overweight_trends
from LiveLite import generate_violin_plot

THIS_DIR = Path(__file__).parent


class TestResearchAnalysis(unittest.TestCase):
    """
    Class defining test suite for research_analysis
    """

    def setUp(self):
        """
        Sets up the test by loading in the data.
        """
        nhanes_path = THIS_DIR.parent / 'data/input_files/NHANES_Background.csv'
        ihme_path = THIS_DIR.parent / 'data/input_files/IHME/number-of-deaths-by-risk-factor.csv'
        self.nhanes_data = pd.read_csv(nhanes_path)
        self.ihme_data = pd.read_csv(ihme_path)

    def test_background_information_nhanes(self):
        """
        Tests if background_information_nhanes runs and returns an object.
        """
        plt = plot_obesity_overweight_trends(data=self.nhanes_data, years=None)
        self.assertIsInstance(plt, object)

    def test_background_information_ihme(self):
        """
        Tests if background_information_ihme runs and returns an object.
        """
        plt = plot_ihme_data(data=self.ihme_data)
        self.assertIsInstance(plt, object)

    def test_violin_plot(self):
        """
        Tests if violin_plot_manager runs and returns an object.
        """

        plt = generate_violin_plot(data=self.nhanes_data)
        self.assertIsInstance(plt, object)

    def test_violin_plot_weight(self):
        """ Test if box plots are returned
        """
        plt = generate_violin_plot(data=self.nhanes_data, plot_type='Weight')
        self.assertIsInstance(plt, object)

    def test_obesity_trends(self):
        """
        Tests if obesity_trends runs and returns an object.
        """
        plt = plot_obesity_trends(data=self.nhanes_data)
        self.assertIsInstance(plt, object)

    def test_invalid_data_type_background_information_nhanes(self):
        """
        Tests if plot_obesity_overweight_trends raises the type error when passed invalid data.
        """

        with self.assertRaises(TypeError):
            plot_obesity_overweight_trends(
                data=np.array([]), years=[1999, 2017]
            )

    def test_invalid_year_type_background_information_nhanes(self):
        """
        Tests if plot_obesity_overweight_trends raises proper type error when passed
        year of invalid type.
        """
        with self.assertRaises(TypeError):
            plot_obesity_overweight_trends(
                data=self.nhanes_data, years=1999
            )

    def test_invalid_year_value_background_information_nhanes(self):
        """
        Tests if plot_obesity_overweight_trends raises the proper value
        error when passed invalid year(s)
        """
        with self.assertRaises(ValueError):
            plot_obesity_overweight_trends(
                data=self.nhanes_data, years=[2000, 2003]
            )

    def test_invalid_data_type_ihme(self):
        """
        Tests if ihme raises type error when passed invalid data.
        """
        with self.assertRaises(TypeError):
            plot_ihme_data(np.array([]), years=[2000, 2001])

    def test_invalid_year_type_ihme(self):
        """
        Tests if ihme raises type error when passed invalid year type.
        """
        with self.assertRaises(TypeError):
            plot_ihme_data(data=self.ihme_data, years=2000)

    def test_invalid_year_value_ihme(self):
        """
        Tests if ihme raises value error when passed invalid year.
        """
        with self.assertRaises(ValueError):
            plot_ihme_data(data=self.ihme_data, years=[1800, 1810])

    def test_invalid_data_type_obesity_trends(self):
        """
        Tests if obesity trends raises type error when passed invalid data type.
        """
        with self.assertRaises(TypeError):
            plot_obesity_trends(np.array([]))

    def test_invalid_year_type_obesity_trends(self):
        """
        Tests if obesity trends raises type error when passed invalid year type.
        """
        with self.assertRaises(TypeError):
            plot_obesity_trends(self.nhanes_data, years=2000)

    def test_invalid_year_value_obesity_trends(self):
        """
        Tests if obesity trends raises type error when passed invalid year.
        """
        with self.assertRaises(ValueError):
            plot_obesity_trends(self.nhanes_data, years=[1800, 1810])

    def test_invalid_data_trends(self):
        """
        Tests if trend over time raises type error when passed invalid data type.
        """
        with self.assertRaises(TypeError):
            generate_violin_plot(np.array([]))

    def test_invalid_year_type_trends(self):
        """
        Tests if trend over time raises type error when passed invalid year type.
        """
        with self.assertRaises(TypeError):
            generate_violin_plot(self.nhanes_data, years=2000)

    def test_invalid_year_value_trends(self):
        """
        Tests if trend over time raises type error when passed invalid year.
        """
        with self.assertRaises(ValueError):
            generate_violin_plot(self.nhanes_data, years=[1800, 1810])

    def test_invalid_type_plottype_trends(self):
        """
        Tests if trend over time raises type error when passed invalid plottype type.
        """

        with self.assertRaises(TypeError):
            generate_violin_plot(self.nhanes_data, plot_type=2)

    def test_invalid_value_plot_trend(self):
        """
        Tests if trend over time raises value error when passed invalid plottype value.
        """
        with self.assertRaises(ValueError):
            generate_violin_plot(self.nhanes_data, plot_type='Height')
