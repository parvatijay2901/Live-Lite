import unittest
import pandas as pd
from LiveLite.research.visualizations import research_analysis as ra


class TestResearchAnalysis(unittest.TestCase):
    """
    Class defining test suite for research_analysis
    """

    def setUp(self):
        self.nhanes_data = pd.read_parquet('../../LiveLite/data/files/NHANES_Background.parquet')
        self.ihme_data = pd.read_csv('../../LiveLite/data/files/IHME/number-of-deaths-by-risk-factor.csv')

    def test_background_information_nhanes(self):
        """
        Tests if background_information_nhanes runs and returns an object.
        """
        plt = ra.background_information_nhanes(data=self.nhanes_data, years=None)
        self.assertIsInstance(plt, object)

    def test_background_information_ihme(self):
        """
        Tests if background_information_ihme runs and returns an object.
        :return:
        """
        plt = ra.background_information_ihme(data=self.ihme_data)
        self.assertIsInstance(plt, object)

    def test_violin_plot(self):
        """
        Tests if violin_plot_manager runs and returns an object.
        """

        plt = ra.violin_plot_manager(data=self.nhanes_data)
        self.assertIsInstance(plt, object)

    def test_obesity_trends(self):
        """
        Tests if obesity_trends runs and returns an object.
        """
        plt = ra.obesity_trends(data=self.nhanes_data)
        self.assertIsInstance(plt, object)

    def test_invalid_year_background_information_nhanes(self):
        """
        Tests if background_information_nhanes raises the proper value error when passed invalid year(s)
        """
        with self.assertRaises(ValueError):
            ra.background_information_nhanes(data=self.nhanes_data, years=[2000, 2003])
