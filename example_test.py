import unittest
import requests
from unittest.mock import patch
from birds import get_recent_observations


class TestGetRecentObservations(unittest.TestCase):
    # for the purposes of this test we are going to be using the following parameters:
    def setUp(self):
        self.region_code = 'US-CA'
        self.api_key = 'epcc2hvf2vd7'

    # check for valid API call / response by checking for succesful status code

    # we use this patch thing to "mock" the requests.get method in the birds module
    # so basically we replace whatever output (object) we would get from this method
    # with a mock or fake object so we can just test if the request was valid
    # this is so we avoid having to actually make the API call twice (after calling once 
    # for the sample observations call to be tested)
    @patch('birds.requests.get') # 
    def test_valid_api_call(self, mock_get):
        try:
            observations = get_recent_observations(self.region_code, api_key=self.api_key)      # call the function (should be no errors)       
        except Exception as e:
            self.fail(f"Unexpected exception raised: {e}")
    
    # check for invalid status code due to bad parameters (api key and region code). These are the next two tests defined
    @patch('birds.requests.get') # 
    def test_invalid_api_key(self, mock_get):
        mock_get.return_value.status_code = 401    
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()
        with self.assertRaises(requests.exceptions.HTTPError):
            get_recent_observations(self.region_code, api_key = 'YO MAMA')

    @patch('birds.requests.get') # 
    def test_invalid_region_code(self, mock_get):
        mock_get.return_value.status_code = 400
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()
        with self.assertRaises(requests.exceptions.HTTPError):
            get_recent_observations(region_code = 'DEEZ', api_key = self.api_key)


if __name__ == '__main__':
    unittest.main()