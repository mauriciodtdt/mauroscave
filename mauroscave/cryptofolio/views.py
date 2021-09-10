from django.shortcuts import render
from rest_framework import viewsets
from .models import Balance, User
from .serializer import BalanceSerializer
from binance.client import Client
from dataclasses import dataclass


# Create your views here.
@dataclass
class Coin:
    name: str
    free: float
    locked: float
    usdt_ticker: float
    aud_ticker: float
    btc_ticker: float


class BalanceViewset(viewsets.ModelViewSet):
    serializer_class = BalanceSerializer

    def get_queryset(self):
        data = Balance.objects.all()
        return data

    # def get_user_balances(self, user_client: Client):
    #     balances = user_client.get_account().get('balances')
    #     return balances

    def save_balance_data(self, user: User):
        total_usdt_balance = total_aud_balance = total_btc_balance = 0
        # user_balances = self.get_coins_balances(user_client)
        # if user_balances is not None:
            # print(f'Balance: {user_balance}')
        user_client = Client(user.api_key, user.api_secret)
        coins = self.get_coins_balances(user_client)
        for coin in coins:
            coin_usdt_value = (coin.free + coin.locked) * coin.usdt_ticker
            coin_aud_value = (coin.free + coin.locked) * coin.aud_ticker
            coin_btc_value = (coin.free + coin.locked) * coin.btc_ticker
            # print(f'coin:{coin} - udst balance: {coin_usdt_value}')
            total_usdt_balance += coin_usdt_value
            total_aud_balance += coin_aud_value
            total_btc_balance += coin_btc_value

        print(f'Total USDT Balance: {total_usdt_balance}\n'
              f'Total AUD Balance: {total_aud_balance}\n'
              f'Total BTC Balance: {total_btc_balance}\n')
        user_balance = Balance(user=user,
                               usdt_balance=total_usdt_balance, 
                               aud_balance=total_aud_balance,
                               btc_balance=total_btc_balance)
        user_balance.save()

    def get_coins_balances(self, client):
        coins = []
        audusdt_ticker = float(client.get_symbol_ticker(symbol="AUDUSDT").get('price'))
        btcusdt_ticker = float(client.get_symbol_ticker(symbol="BTCUSDT").get('price'))

        for asset_balance in client.get_account().get('balances'):
            asset = asset_balance.get('asset')
            free_asset = float(asset_balance.get('free'))
            locked_asset = float(asset_balance.get('locked'))
            if (free_asset == locked_asset == 0) or asset == 'LDUSDT' or asset == 'NFT':
                continue
            # print(f'Getiing ticker for symbol {asset}USDT with balance {free_asset} and {locked_asset}')
            if 'LD' in asset:
                asset = asset.replace('LD', '')
            if 'BETH' in asset:
                asset = asset.replace('B', '')
            if 'PPT' == asset:
                btc_ticker = float(client.get_symbol_ticker(symbol=f"{asset}BTC").get('price'))
                asset = 'BTC'
                free_asset = free_asset * btc_ticker
            usdt_ticker = 1 if asset == 'USDT' else float(client.get_symbol_ticker(symbol=f"{asset}USDT").get('price'))
            coins.append(Coin(
                name=asset,
                free=free_asset,
                locked=locked_asset,
                usdt_ticker=usdt_ticker,
                aud_ticker=(usdt_ticker / audusdt_ticker),
                btc_ticker=(usdt_ticker / btcusdt_ticker)
            ))
            # print(asset_balance.get('asset') + ': ' + asset_balance.get('free') + ': ' + asset_balance.get('locked'))
        return coins

