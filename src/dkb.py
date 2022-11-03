"""DKB Fetcher"""

from datetime import date, timedelta
from dkb_robo import DKBRobo

# logindata = dkb.last_login
# accounts = dkb.account_dic
def fetch_dkb(dkb_user, dkb_pw, since_days):
    """fetch DKB Transactions"""
    with DKBRobo(dkb_user, dkb_pw) as dkb:
        last_month = date.today() - timedelta(days=since_days)
        dkb_date_from = last_month.strftime("%d.%m.%Y")
        dkb_date_to = date.today().strftime("%d.%m.%Y")
        dkb_link = dkb.account_dic[0]['transactions']
        dkb_type = dkb.account_dic[0]['type']

        transactions = dkb.get_transactions(dkb_link, dkb_type, dkb_date_from, dkb_date_to)
    return transactions