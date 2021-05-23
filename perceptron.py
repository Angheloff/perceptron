import xlrd
import pandas as pd


def entrenar(theta, fac_ap, w1, w2, epoch, x1, x2, d, n_muestras):
    errores = True
    while errores:
        errores = False
        for i in range(n_muestras):
            z = ((x1[i] * w1)+(x2[i] * w2)) - theta  # calculamos z

            if z >= 0:
                z = 1
            else:
                z = 0

            if z != d[i]:
                errores = True
                # calcular errores
                error = (d[i] - z)
                # ajustar theta
                theta = theta + (-(fac_ap * error))
                # ajustar pesos
                w1 = w1 + (x1[i] * error * fac_ap)
                w2 = w2 + (x2[i] * error * fac_ap)
                epoch += 1
    return w1, w2, epoch, theta

# ciclo principal


if __name__ == "__main__":
    # leer el archivo de excel
    arhivo_excel = pd.read_excel("tablaOR.xlsx")
    theta = 0.4
    fac_ap = 0.2
    w1 = 0.3
    w2 = 0.5
    epoch = 0
    x1 = arhivo_excel["x1"]
    x2 = arhivo_excel["x2"]
    d = arhivo_excel["d"]
    n_muestras = len(d)
    w1, w2, epoch, theta, = entrenar(
        theta, fac_ap, w1, w2, epoch, x1, x2, d, n_muestras)

    print("w1 = ", w1)
    print("w2 = ", w2)
    print("theta = ", theta)
    print("epoch = ", epoch)
