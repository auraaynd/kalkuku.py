import math


def tampilkan_menu():
    print("\n=== Kalkulator Scientific ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Pangkat")
    print("6. Akar kuadrat")
    print("7. Logaritma")
    print("8. Sin")
    print("9. Cos")
    print("10. Tan")
    print("11. Derajat ke radian")
    print("12. Radian ke derajat")


def input_angka(pesan="Masukkan angka: "):
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input tidak valid. Masukkan angka.")


def main():
    tampilkan_menu()
    pilihan = input("Pilihan: ").strip()

    try:
        if pilihan in {"1", "2", "3", "4", "5"}:
            a = input_angka("Angka pertama: ")
            b = input_angka("Angka kedua: ")

            if pilihan == "1":
                hasil = a + b
            elif pilihan == "2":
                hasil = a - b
            elif pilihan == "3":
                hasil = a * b
            elif pilihan == "4":
                if b == 0:
                    raise ZeroDivisionError
                hasil = a / b
            else:
                hasil = math.pow(a, b)

            print("Hasil:", hasil)

        elif pilihan == "6":
            a = input_angka("Angka: ")
            if a < 0:
                raise ValueError("akar kuadrat tidak boleh negatif")
            print("Hasil:", math.sqrt(a))

        elif pilihan == "7":
            a = input_angka("Angka: ")
            if a <= 0:
                raise ValueError("logaritma hanya untuk angka positif")
            print("Hasil:", math.log10(a))

        elif pilihan in {"8", "9", "10"}:
            a = input_angka("Sudut (derajat): ")
            radian = math.radians(a)

            if pilihan == "8":
                hasil = math.sin(radian)
            elif pilihan == "9":
                hasil = math.cos(radian)
            else:
                hasil = math.tan(radian)

            print("Hasil:", hasil)

        elif pilihan == "11":
            a = input_angka("Sudut (derajat): ")
            print("Hasil:", math.radians(a))

        elif pilihan == "12":
            a = input_angka("Sudut (radian): ")
            print("Hasil:", math.degrees(a))

        else:
            print("Pilihan tidak tersedia.")

    except ZeroDivisionError:
        print("Kesalahan: tidak bisa membagi dengan nol.")
    except OverflowError:
        print("Kesalahan: hasil terlalu besar.")
    except ValueError as kesalahan:
        print("Kesalahan:", kesalahan)


if __name__ == "__main__":
    main()