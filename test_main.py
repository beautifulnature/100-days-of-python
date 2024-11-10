# test_main.py
import sys
import io
import unittest
from printing import print_recipe

class TestRecipeOutput(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_output = io.StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset redirect.
        sys.stdout = sys.__stdout__

    def test_output(self):
        print_recipe()  # Call the function that prints the recipe
        output = self.held_output.getvalue()  # Get the printed output
        expected_output = (
            "1. Mix 500g of flour, 10g yeast and 300ml water in a bowl.\n"
            "2. Knead the dough for 10 minutes.\n"
            "3. Add 3g of salt.\n"
            "4. Leave to rise for 2 hours.\n"
            "5. Bake at 200 degrees C for 30 minutes.\n"
        )
        self.assertEqual(expected_output, output,
                         "Output does not match expected output.")

if __name__ == "__main__":
    unittest.main()