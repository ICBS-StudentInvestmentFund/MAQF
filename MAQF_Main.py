import datetime as dt
import os
import sys
import warnings
from datetime import datetime

import dateutil.relativedelta as rd
import pandas as pd
from pandas.tseries.offsets import MonthEnd

sys.path.insert(0, os.path.normpath(os.path.join(os.environ['GIT_TOP'],'')))

from cache import cache

from core.arp import arp_object, arp_model, descriptive_stats
from core.generic import get_cloest_index_values
from core import db_connection as dbutil

# Backtesting module
from core.oos_backtester.targets_determination import target_determination
from core.oos_backtester.backtester import backtester, process_backtest_specification
from core.oos_backtester.backtest_results_overview import backtester_results_overview
from core.oos_backtester.decorate_desc_stats import decorate_desc_stats

# Import other module
from tools.utility_functions import save_file_in, get_pricing_source_dict, monthend
from tools.desc_stats import run_desc_stats

warnings.simplefilter(action='ignore', category=FutureWarning)
pd.options.mode.chained_assignment = None

####################
# HELPER FUNCTIONS #
####################

#
@cache.cache(cache_name='ts_object_instance')
def source_prices(conf)

    prices_source = get_pricing_source_dict(conf['peers'], conf)
    timeseries = list(prices_source.keys())


    return ts_object_instance

@cache.cache(cache_name='desc_stats_instance')
def sample_dist_characteristics(conf):

    return sample_desc_stats_instance

@cache.cache(cache_name='oos_backtest_results')
def run_oos_portfolio_backtester(conf,ts_object_instance,desc_stats_instance)

    return oos_backtest_results

###############################
# SPECIFIC INPUTS AND OUTPUTS #
###############################

conf = ['config_research_MA_port','config_securities_MA_port']

ext_data_fname = conf['ext_data_fname']
start_date = pd.to_datetime(conf['start_date'])
offset = pd.tseries.offsets.BusinessDay(n=1)
if conf['end_date'] is None:
    end_date = pd.to_datetime(datetime.today().strftime('%Y-%m-%d')) - offset
else:
    end_date = pd.to_datetime(conf['end_date'])

save_file_in(os.path.join(conf['output_dname'], "Output Files"))

###########################
# LOAD AND MERGE ALL DATA #
###########################

ts_object_instance = source_daily_prices(conf)
ts_object_instance.daily_prices.to_csv(os.path.join(conf['output_dname'], "Output Files", "daily_prices.csv"))

#########################################
# ESTIMATE DISTRIBUTION CHARACTERISTICS #
#########################################

desc_stats_instance = sample_dist_characteristics(conf)

##########################
# PORTFOLIO CONSTRUCTION #
##########################

backtest_output= {}

if conf['run_backtest']:
    oos_backtest_results = run_oos_portfolio_backtester(conf,ts_object_instance,desc_stats_instance)
    backtest_output = oos_backtest_results

################
# LOAD MODULES #
################

# Descriptive Statistics #
df_stats = run_desc_stats(df_prices.copy(),df_stats.copy(),
                          conf['descriptive statistics']['frequency'],
                          conf['benchmarks']['traditional_bms'],
                          ['USGG10YR_INDEX','USGG10YR Index'],
                          conf['descriptive statistics']['vol_scaling'],
                          conf['descriptive statistics']['lookback'],
                          conf['descriptive statistics']['SR_improve_alloc'],
                          conf['descriptive statistics']['frequency'],
                          conf['run_figures'],
                          conf['descriptive statistics']['plot_PFs'],
                          conf['descriptive statistics']['cust_corr_idxs'],
                          upload_index_type = 'level',
                          start_date = None,
                          as_of_date = datetime.strftime(end_date,'%Y-%m-%d'),
                          to_excel = True,
                          output_path = conf['output_dname'],
                          stress_dates = conf['descriptive statistics']['stress_dates'],
                          strategy_backtest_result = strategy_backtest_result,
                          crisis_vol_scaling = conf['descriptive statistics'].get('DS_vol_scaling_crisis', conf['descriptive statistics']....,
                          scaled_y_cp = False,
                          ui_client = False,
                          cash_levels = shared_data_inst.cash_levels)

# Generate a summary report of all of the output generated above #
