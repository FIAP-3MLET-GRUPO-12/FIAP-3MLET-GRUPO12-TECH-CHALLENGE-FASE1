
import logging
from app.config import settings
from app.models.trade_model import Trade
from app.utils.csv_downloader import download_csv_from_url
from app.utils.json_utils import parse_data_frame_to_trade_json
from app.utils.trade_type_enum import TradeType


async def trade_setup():
    if await trade_exist():
        return

    base_url = settings.BASE_URL_CSV_VITIBRASIL
    csv_files = [
        ("/ImpVinhos.csv", TradeType.IMPORT, 'VINHOS DE MESA', ';'),
        ("/ImpEspumantes.csv", TradeType.IMPORT, 'ESPUMANTES', ';'),
        ("/ImpFrescas.csv", TradeType.IMPORT, 'UVAS FRESCAS', ';'),
        ("/ImpPassas.csv", TradeType.IMPORT, 'UVAS PASSAS', ';'),
        ("/ImpSuco.csv", TradeType.IMPORT, 'SUCO DE UVA', ';'),
        ("/ExpVinho.csv", TradeType.EXPORT, 'VINHOS DE MESA', ';'),
        ("/ExpEspumantes.csv", TradeType.EXPORT, 'ESPUMANTES', ';'),
        ("/ExpUva.csv", TradeType.EXPORT, 'UVAS FRESCAS', ';'),
        ("/ExpSuco.csv", TradeType.EXPORT, 'SUCO DE UVA', ';'),
    ]

    trades = []
    logging.info(" - Downloading trade data...")
    for file_suffix, trade_type, category, delimiter in csv_files:
         logging.info(f" - Downloading {file_suffix}...")
         df = download_csv_from_url(base_url + file_suffix, delimiter)
         json_data = parse_data_frame_to_trade_json(df, trade_type, category)
         trades.extend([Trade(**trade) for trade in json_data])

    logging.info(" - Inserting trade data...")
    await insert_all_trades(trades)
    logging.info(" - Trade data inserted successfully!")

async def trade_exist() -> bool:
    trade = await Trade.find_all().to_list()
    return bool(trade)

async def insert_all_trades(trades: list[Trade]):
    await Trade.insert_many(trades)