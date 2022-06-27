import os
import logging

def get_config():
    config_dict = {
        'local': {
            'this_api': 'http://local.asf.alaska.edu:5000',
            'bulk_download_api': 'https://bulk-download.asf.alaska.edu',
            'analytics_id': None,
            'cmr_base': 'https://cmr.uat.earthdata.nasa.gov',
            'cmr_health': '/search/health',
            'cmr_api': '/search/granules.echo10',
            'cmr_collections': '/search/collections',
            'cmr_headers': {
                'Client-Id': 'local_searchapi_asf'
            }
        },
        'devel': {
            'this_api': 'https://api-dev.asf.alaska.edu',
            'bulk_download_api': 'https://bulk-download.asf.alaska.edu',
            'analytics_id': 'UA-118881300-4',
            'cmr_base': 'https://cmr.uat.earthdata.nasa.gov',
            'cmr_health': '/search/health',
            'cmr_api': '/search/granules.echo10',
            'cmr_collections': '/search/collections',
            'cmr_headers': {
                'Client-Id': 'devel_vertex_asf'
            }
        },
        'devel-beanstalk': {
            'this_api': 'https://api-dev.asf.alaska.edu',
            'bulk_download_api': 'https://bulk-download.asf.alaska.edu',
            'analytics_id': 'UA-118881300-4',
            'cmr_base': 'https://cmr.uat.earthdata.nasa.gov',
            'cmr_health': '/search/health',
            'cmr_api': '/search/granules.echo10',
            'cmr_collections': '/search/collections',
            'cmr_headers': {
                'Client-Id': 'devel_searchapi_asf'
            }
        },
        'test': {
            'this_api': 'https://api-test.asf.alaska.edu',
            'bulk_download_api': 'https://bulk-download.asf.alaska.edu',
            'analytics_id': 'UA-118881300-3',
            'cmr_base': 'https://cmr.uat.earthdata.nasa.gov',
            'cmr_health': '/search/health',
            'cmr_api': '/search/granules.echo10',
            'cmr_collections': '/search/collections',
            'cmr_headers': {
                'Client-Id': 'test_vertex_asf'
            }
        },
        'test-beanstalk': {
            'this_api': 'https://api-test.asf.alaska.edu',
            'bulk_download_api': 'https://bulk-download.asf.alaska.edu',
            'analytics_id': 'UA-118881300-3',
            'cmr_base': 'https://cmr.uat.earthdata.nasa.gov',
            'cmr_health': '/search/health',
            'cmr_api': '/search/granules.echo10',
            'cmr_collections': '/search/collections',
            'cmr_headers': {
                'Client-Id': 'test_searchapi_asf'
            }
        },
        'prod': {
            'this_api': 'https://api.daac.asf.alaska.edu',
            'bulk_download_api': 'https://bulk-download.asf.alaska.edu',
            'analytics_id': 'UA-118881300-2',
            'cmr_base': 'https://cmr.earthdata.nasa.gov',
            'cmr_health': '/search/health',
            'cmr_api': '/search/granules.echo10',
            'cmr_collections': '/search/collections',
            'cmr_headers': {
                'Client-Id': 'searchapi_asf'
            }
        },
        'prod-private': {
            'this_api': 'https://api-prod-private.asf.alaska.edu',
            'bulk_download_api': 'https://bulk-download.asf.alaska.edu',
            'analytics_id': 'UA-118881300-5',
            'cmr_base': 'https://cmr.earthdata.nasa.gov',
            'cmr_health': '/search/health',
            'cmr_api': '/search/granules.echo10',
            'cmr_collections': '/search/collections',
            'cmr_headers': {
                'Client-Id': 'vertex_asf'
            }
        }
    }
    # If they don't set a maturity
    if 'MATURITY' not in os.environ.keys():
        # logging.warning('os.environ[\'MATURITY\'] not set! Defaulting to prod config.]')
        maturity = 'prod'
    # If we don't have that maturity
    elif os.environ['MATURITY'] not in config_dict:
        logging.warning('os.environ[\'MATURITY\'] is unknown! Defaulting to prod config.]')
        maturity = 'prod'
    else:
        maturity = os.environ['MATURITY']
    return config_dict[maturity]
