from django.apps import AppConfig


class CryptofolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cryptofolio'

    def ready(self):
        print(f"Starting scheduler ...")
        from .crypto_scheduler import balance_updater
        balance_updater.start()