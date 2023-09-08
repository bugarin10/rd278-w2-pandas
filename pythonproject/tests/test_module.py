"""Import appropriate modules to select src filepath since it isnt in the test director"""
import unittest
import sys
import os
import pandas as pd

def is_csv_valid(file_path):
    try:
        # Attempt to read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Check if all columns contain numeric data
        if df.select_dtypes(include=['number']).shape[1] == len(df.columns):
            return True
        else:
            return False

    except (pd.errors.EmptyDataError, pd.errors.ParserError, FileNotFoundError):
        # Handle exceptions for empty files, parsing errors, and missing files
        return False

#As the module src is not in the test directory I'll append it
sys.path.append('/workspaces/rd278-w2-pandas/pythonproject/src')
print(sys.path)
import source_code


#class TestSourceCode(unittest.TestCase):
#    """unit test class which will test source code"""
#    class TestOutput(unittest.TestCase):
#        def test_validity_output(self):
#           
#            data=pd.read_csv("pythonproject/src/data/spotify-2023.csv",encoding="ISO-8859-1")
#            cls='pandas.core.frame.DataFrame'
#            result=type(source_code.descriptive_statistics(data))           
#            self.assertIsInstance(result,cls, msg='This is not the expected output')
#
#    class TestComputeDescriptiveStatistics(unittest.TestCase):
#        def test_csv_validity(self):
#            
#            valid_csv_path = "pythonproject/src/data/spotify-2023.csv"  # Replace with the path to a valid CSV file
#            invalid_csv_path = "pythonproject/src/data/test_fail.csv"  # Replace with the path to an invalid CSV file
#
#            self.assertTrue(is_csv_valid(valid_csv_path), "Valid CSV file check failed.")
#            self.assertFalse(is_csv_valid(invalid_csv_path), "Invalid CSV file check failed.")



if __name__ == "__main__":
    unittest.main()
