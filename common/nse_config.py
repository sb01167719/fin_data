import os
import sys
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from settings import CONFIG_DIR

# --------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # 1. NSE symbols & indices
    nse_symbol_urls = [
        'https://archives.nseindia.com/content/equities/EQUITY_L.csv',
        'https://archives.nseindia.com/content/indices/ind_nifty50list.csv',
        'https://archives.nseindia.com/content/indices/ind_nifty100list.csv',
        'https://archives.nseindia.com/content/indices/ind_niftymidcap150list.csv',
        'https://archives.nseindia.com/content/indices/ind_niftysmallcap250list.csv',
        'https://archives.nseindia.com/content/indices/ind_nifty500list.csv',
        'https://archives.nseindia.com/content/indices/ind_niftymicrocap250_list.csv',
        'https://archives.nseindia.com/content/indices/ind_niftytotalmarket_list.csv'
    ]

    for url in nse_symbol_urls:
        print('Downloading', f'{os.path.basename(url)}', end=' ... ')
        df = pd.read_csv(url)
        df.to_csv(CONFIG_DIR + f'/02_nse_symbols/{os.path.basename(url)}', index=False)
        print('Done, shape:', df.shape)

    # 2. NSE symbol changes
    print('Downloading nse_symbolchanges.csv', end=' ... ')
    nse_symbol_changes_url = 'https://archives.nseindia.com/content/equities/symbolchange.csv'
    df = pd.read_csv(nse_symbol_changes_url, encoding='cp1252')
    df.to_csv(CONFIG_DIR + '/02_nse_symbols/nse_symbol_changes.csv', index=False)
    print('Done, shape:', df.shape)

    # 3. FO market lots
    print('Downloading fo_mktlots.csv', end=' ... ')
    nse_symbol_changes_url = 'https://archives.nseindia.com/content/fo/fo_mktlots.csv'
    df = pd.read_csv(nse_symbol_changes_url, encoding='cp1252')
    df.to_csv(CONFIG_DIR + '/02_nse_symbols/fo_mktlots.csv', index=False)
    print('Done, shape:', df.shape)

    # TO DO: BSE_CODES