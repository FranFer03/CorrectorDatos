import pandas as pd
import os


def join_csv(path="CSV_Ejes/", out_file=None):
    """
    Combina los archivos CSV existentes en una carpeta y devolverlo como un
    DataFrame.

    Parameters
    ----------
    path : string
        La ruta en la que se encuentran los archivos, si no se indica ninguna se
        usará la carpeta actual.
    out_file :string
        Archivo opcional en el que se guardará los resultados, en caso de que no
        se indique un nombre no se generará

    Returns
    -------
    DataFrame
        Obejto DataFrame con la unión de los archivos CSV
    """

    if path is None:
        files = [file for file in os.listdir() if '.csv' in file]
    else:
        files = [os.path.join(path, file) for file in os.listdir(path) if '.csv' in file]

    df = pd.concat(map(pd.read_csv, files), ignore_index=True)

    if out_file is not None:
        if path is None:
            df.to_csv(out_file, index=False)
        else:
            df.to_csv(os.path.join(path, out_file), index=False)

    return df


def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file = "QG_Ejes_Database.csv" in os.listdir()
    if file:
        os.remove("QG_Ejes_Database.csv")
    cvs_directory = os.path.join(current_directory, 'CSV_Ejes')
    join_csv(path=cvs_directory ,out_file="../QG_Ejes_Database.csv")


if __name__ == "__main__":
    main()