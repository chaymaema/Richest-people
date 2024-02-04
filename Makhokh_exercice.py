import csv
import shutil

# Extraire le fichier zip

zip_file_path = "D:/test/data.zip"

destination_folder = "D:/test"

shutil.unpack_archive(zip_file_path, destination_folder, "zip")

# Explanation of each column:
# column a      : contains the index for each row in the dataset.
# column b      : it appears to be a description.
# column c      : contains the first name of individuals.
# column d      : contains the last name of individuals.
# columns e,f,g : contains a numerical value, it's not specified what this value represents,
# but one of them or the sum of two or three of them can represent a person's salary for example.


def read_file(path: str) -> None:
    with open(path, "r", newline="", encoding="utf-8") as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv)

        # variable :
        NUMBER_PEOPLE_RICH: int = 3

        # cancel the first unusable lines
        for _ in range(9):
            next(lecteur_csv)

        # reset variables
        ligne: any = next(lecteur_csv)

        # based on the column : 4
        list_max_column_4: list[int] = [ligne[4], ligne[4], ligne[4]]
        list_max_column_4_info: list[list] = [ligne, ligne, ligne]

        # based on the column : 5
        list_max_column_5: list[int] = [ligne[5], ligne[5], ligne[5]]
        list_max_column_5_info: list[list] = [ligne, ligne, ligne]

        # based on the column : 5
        list_max_column_6: list[int] = [ligne[6], ligne[6], ligne[6]]
        list_max_column_6_info: list[list] = [ligne, ligne, ligne]

        # based on the columns : 4 & 5
        sum_column_4_5: int = int(ligne[4]) + int(ligne[5])
        list_max_column_4_5: list[int] = [
            sum_column_4_5,
            sum_column_4_5,
            sum_column_4_5,
        ]
        list_max_column_4_5_info: list[list] = [ligne, ligne, ligne]

        # based on the column  : 4 & 6
        sum_column_4_6: int = int(ligne[4]) + int(ligne[6])
        list_max_column_4_6: list[int] = [
            sum_column_4_6,
            sum_column_4_6,
            sum_column_4_6,
        ]
        list_max_column_4_6_info: list[list] = [ligne, ligne, ligne]

        # based on the column  : 5 & 6
        sum_column_5_6: int = int(ligne[5]) + int(ligne[6])
        list_max_column_5_6: list[int] = [
            sum_column_5_6,
            sum_column_5_6,
            sum_column_5_6,
        ]
        list_max_column_5_6_info: list[list] = [ligne, ligne, ligne]

        # based on the column  : 4 & 5 & 6
        sum_column_4_5_6: int = int(ligne[4]) + int(ligne[5]) + int(ligne[6])
        list_max_column_4_5_6: list[int] = [
            sum_column_4_5_6,
            sum_column_4_5_6,
            sum_column_4_5_6,
        ]
        list_max_column_4_5_6_info: list[list] = [ligne, ligne, ligne]

        max_state: bool = False
        for ligne in lecteur_csv:
            # The three richest people based on the column : 4
            for index in range(NUMBER_PEOPLE_RICH):
                if int(ligne[4]) > int(list_max_column_4[index]):
                    list_max_column_4[index] = ligne[4]
                    list_max_column_4_info[index] = ligne
                    max_state = True
                if max_state:
                    break
            max_state = False

            # The three richest people based on the column : 5
            for index in range(NUMBER_PEOPLE_RICH):
                if int(ligne[5]) > int(list_max_column_4[index]):
                    list_max_column_5[index] = ligne[5]
                    list_max_column_5_info[index] = ligne
                    max_state = True
                if max_state:
                    break
            max_state = False

            # The three richest people based on the column : 6
            for index in range(NUMBER_PEOPLE_RICH):
                if int(ligne[6]) > int(list_max_column_4[index]):
                    list_max_column_6[index] = ligne[6]
                    list_max_column_6_info[index] = ligne
                    max_state = True
                if max_state:
                    break
            max_state = False

            # The three richest people based on the columns : 4 & 5
            sum_column_4_5: int = int(ligne[4]) + int(ligne[5])
            for index in range(NUMBER_PEOPLE_RICH):
                if sum_column_4_5 > list_max_column_4_5[index]:
                    list_max_column_4_5[index] = sum_column_4_5
                    list_max_column_4_5_info[index] = ligne
                    max_state = True
                if max_state:
                    break
            max_state = False

            # The three richest people based on the column  : 4 & 6
            sum_column_4_6: int = int(ligne[4]) + int(ligne[6])
            for index in range(NUMBER_PEOPLE_RICH):
                if sum_column_4_6 > list_max_column_4_6[index]:
                    list_max_column_4_6[index] = sum_column_4_6
                    list_max_column_4_6_info[index] = ligne
                    max_state = True
                if max_state:
                    break
            max_state = False

            # The three richest people based on the column  : 5 & 6
            sum_column_5_6: int = int(ligne[5]) + int(ligne[6])
            for index in range(NUMBER_PEOPLE_RICH):
                if sum_column_5_6 > list_max_column_5_6[index]:
                    list_max_column_5_6[index] = sum_column_5_6
                    list_max_column_5_6_info[index] = ligne
                    max_state = True
                if max_state:
                    break
            max_state = False

            # The three richest people based on the column  : 4 & 5 & 6
            sum_column_4_5_6: int = int(ligne[4]) + int(ligne[5]) + int(ligne[6])
            for index in range(NUMBER_PEOPLE_RICH):
                if sum_column_4_5_6 > list_max_column_4_5_6[index]:
                    list_max_column_4_5_6[index] = sum_column_4_5_6
                    list_max_column_4_5_6_info[index] = ligne
                    max_state = True
                if max_state:
                    break
            max_state = False

        print(list_max_column_4_5_6)
        print(list_max_column_4_5_6_info)
        print("------------------------------------------")
        print(list_max_column_4_5)
        print(list_max_column_4_5_info)
        print("------------------------------------------")
        print(list_max_column_4_6)
        print(list_max_column_4_6_info)
        print("------------------------------------------")
        print(list_max_column_5_6)
        print(list_max_column_5_6_info)
        print("------------------------------------------")
        print(list_max_column_4)
        print(list_max_column_4_info)
        print("------------------------------------------")
        print(list_max_column_5)
        print(list_max_column_5_info)
        print("------------------------------------------")
        print(list_max_column_6)
        print(list_max_column_6_info)


read_file("D:/test/Data.csv")