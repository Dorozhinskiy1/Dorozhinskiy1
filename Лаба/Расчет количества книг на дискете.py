StorageInMb: float = 1.44
pages: int = 100
lines: int = 50
symbols: int = 25
OneSymbolStorageInB: int = 4

TotalStorage: float = StorageInMb*1024*1024
OneBookStorage: float = pages*lines*symbols*OneSymbolStorageInB

result = TotalStorage//OneBookStorage
print("Количество книг, помещающихся на дискету:", int(result))
