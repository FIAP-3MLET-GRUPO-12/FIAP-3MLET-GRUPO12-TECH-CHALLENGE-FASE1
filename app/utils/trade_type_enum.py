from enum import Enum

class TradeType(Enum):
    IMPORT = "import"
    EXPORT = "export"
    
class TradeDerivatives(Enum):
    TABLE_WINES = "VINHOS DE MESA"
    SPARKLING_WINES = "ESPUMANTES"
    FRASH_GRAPES = "UVAS FRESCAS"
    RAISINS = "UVAS PASSAS"
    GRAPE_JUICE = "SUCO DE UVA"