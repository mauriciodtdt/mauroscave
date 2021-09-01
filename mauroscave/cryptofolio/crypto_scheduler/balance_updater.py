from apscheduler.schedulers.background import BackgroundScheduler
from cryptofolio.models import Balance, User
from cryptofolio.views import BalanceViewset
from binance.client import Client
# import logging

# logging.basicConfig()
# logging.getLogger('apscheduler').setLevel(logging.DEBUG)


def start():
    scheduler = BackgroundScheduler()
    balance = BalanceViewset()
    users = User.objects.all()
    for user in users:
        client = Client(user.api_key, user.api_secret)
        scheduler.add_job(balance.save_balance_data,
                          "interval", minutes=1,
                          kwargs={'user_client': client},
                          id=f'balance_updater_{user.username}',
                          replace_existing=True)
        scheduler.start()
