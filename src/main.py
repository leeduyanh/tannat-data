"""
Main script for processing raw data.

This script imports necessary functions from the services module and processes
the raw data stored in 'raw_data_c.json' when run as the main program.
"""

from services import *

if __name__ == '__main__':
    '''
    Usage:
        process_data() if data has not been crawled yet
        process_data('raw_data_c.json') if the json file already exists
    '''
    data = process_data('raw_data_c.json')
