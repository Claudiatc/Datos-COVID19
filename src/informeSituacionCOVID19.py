'''
MIT License

Copyright (c) 2020 Sebastian Cornejo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

"""
Los productos que salen del informe Situaion COVID19 son:
21
22
"""

import pandas as pd
import utils
from shutil import copyfile


def prod21_22(fte, producto):
    copyfile(fte, producto + '.csv')
    HospitalizadosEtario_T = utils.transpone_csv(producto + '.csv')
    HospitalizadosEtario_T.to_csv(producto + '_T.csv', header=False)


if __name__ == '__main__':
    print('Generando producto 21')
    prod21_22('../input/InformeSituacionCOVID19/SintomasCasosConfirmados.csv', '../output/producto21/SintomasCasosConfirmados')
    prod21_22('../input/InformeSituacionCOVID19/SintomasHospitalizados.csv', '../output/producto21/SintomasHospitalizados')

    print('Generando producto 22')
    prod21_22('../input/InformeSituacionCOVID19/HospitalizadosGeneroEtario.csv', '../output/producto22/HospitalizadosEtario')

