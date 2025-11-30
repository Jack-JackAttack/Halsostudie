from sklearn.linear_model import LinearRegression
import numpy as np


class HealthAnalyzer:
    """
    En klass som jag använder för att hålla koden mer strukturerad så inte allt
    ligger i notebooken.
    """


    def __init__(self, df):
        """
        Tar emot en DataFrame med alla hälsodata. Tar bort tomma rader. Jag sparar den så jag kan
        använda den i andra metoder.
        """
        self.df = df.dropna()


    def pretty(self, value):
        """Använder denna bara för att formatera texten snyggt i notebooken"""

        return(
            f"Skräning: {value["Skärning"]:.2f}\n"
            f"Lutning: {value["Lutning"]:.2f}\n"
            f"R2: {value["R2"]:.2f}"
        )


    def regression(self, y_col, x_col):
        """
        Gör en linjär regrission där jag förklarar sambandet mellan blodtryck
        och (ålder/kolesterol).

        Returnerar en dictionary med skärning, lutning och R2.
        """

        X = self.df[[x_col]].values
        y = self.df[y_col].values

        model = LinearRegression()
        model.fit(X, y)

        self.model = model
        self.x_col = x_col
        self.y_col = y_col

        return{
            "Skärning": float(model.intercept_),
            "Lutning": float(model.coef_[0]),
            "R2": float(model.score(X, y))
        }
    