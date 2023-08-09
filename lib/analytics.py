import os
from copy import deepcopy
from pprint import pprint

import pandas as pd

from lib.pdf_analyser import PdfAnalyser


class Analytics:
    def __init__(self) -> None:
        self.analyser = PdfAnalyser()
        self.data = {}

    def analyse_pdf(self, *pdf_names):
        full_analysis = {}
        for pdf_name in pdf_names:
            analysis = self.analyser.analayse_pdf(pdf_name)
            full_analysis = {**full_analysis, pdf_name: analysis}
        return full_analysis

    def aggregate(self, *pdf_names):
        full_analysis = self.analyse_pdf(*pdf_names)
        self.data = {**self.data, **full_analysis}
        return self.data

    def extract_attribute(self):
        new_data = deepcopy(self.data)
        for comp, athletes in self.data.items():
            for athlete, result in athletes.items():
                new_data[comp][athlete] = result.result
        return pd.DataFrame(new_data).T


if __name__ == "__main__":
    analytics = Analytics()
    res = analytics.aggregate(*os.listdir("data"))
    pprint(res)
    res = analytics.extract_attribute()
    print(res.loc["taivalkoskiMQ.pdf"].sort_values().dropna().convert_dtypes(int))
