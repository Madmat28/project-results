import os

from PyPDF2 import PdfReader
import sys

from lib.athlete_result import AthleteResult


class PdfAnalyser:
    def analayse_pdf(self, pdf_name):
        reader = PdfReader(f"data/{pdf_name}")
        athlete_list = []
        for page in reader.pages:
            athlete_list += self.analyse_page(page)
        return athlete_list

    def analyse_page(self, page):
        text = page.extract_text()
        qualification = "QUALIFICATION" in text
        print(text)
        start_of_athlete_line = []
        for index, line in enumerate(text.split("\n")):
            if line.endswith("B:") and len(line.split(".")) <= 4:
                start_of_athlete_line.append(index)
            elif line.endswith("B:") and len(line.split(".")) == 8:
                start_of_athlete_line.append(index - 1)
        start_of_athlete_line.append(len(text.split("\n")))
        athlete_list = []
        for i in range(len(start_of_athlete_line) - 1):
            athlete_line = "\n".join(
                text.split("\n")[
                    start_of_athlete_line[i] : start_of_athlete_line[i + 1]
                ]
            )
            athlete = AthleteResult(string=athlete_line, qualification=qualification)
            print(athlete)
        return athlete_list


if __name__ == "__main__":
    for file_name in os.listdir("data"):
        analyser = PdfAnalyser()
        analyser.analayse_pdf(file_name)
    file_name = "taivalkoskiM.pdf"
    # file_name = "alpe.pdf"
    analyser = PdfAnalyser()
    analyser.analayse_pdf(file_name)
