from apscheduler.schedulers.background import BackgroundScheduler
from cryptofolio.models import User
from cryptofolio.views import BalanceViewset
from binance.client import Client
# import logging

# logging.basicConfig()
# logging.getLogger('apscheduler').setLevel(logging.DEBUG)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_user_balances,
                      "interval", minutes=1,
                      id=f'balance_updater',
                      replace_existing=True)
    scheduler.start()

def update_user_balances():
    users = User.objects.all()
    balance = BalanceViewset()
    for user in users:
        balance.save_balance_data(user)
