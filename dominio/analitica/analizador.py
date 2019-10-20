"""
Generador de resultados del análisis
"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


class Analizador:

    def __init__(self, muestra):
        self._muestra = muestra
        self._clasificador = None
        return

    def clasificar_tamanio(self, X, Y):
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)
        scaler = StandardScaler()
        scaler.fit(X_train)
        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)
        self._clasificador = KNeighborsClassifier(n_neighbors=1)
        self._clasificador.fit(X_train, y_train)

        return

    def predicir_tamanio(self, escenarios, entidades, interfaces):
        return self._clasificador.predict([[escenarios, entidades, interfaces]])

