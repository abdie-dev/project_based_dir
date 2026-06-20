# setiap karyawan akan mendapatkan 0.5% tip dari setiap pembelian product

menu_items = {"Sauce": 100, "Indomie": 30, "Cocacola": 15}

a = menu_items["Sauce"]
print(a)


def kalkulator_tip(q_product: str):
    for item in menu_items:
        if q_product == item.lower():
            quantity_product: int = int(input("Masukan jumlah barang: "))
            price: int = menu_items[f"{item}"] * quantity_product
            tip: float = price * 0.005
            print("Barang:")
            print(
                f"{item} * {quantity_product}\nRaw Price: {int(price+tip)}\nTip: {tip}\nFinal Price: {price}"
            )


if __name__ == "__main__":
    keranjang_belanja: str = input("Masukan nama barang: ").lower()
    kalkulator_tip(keranjang_belanja)
