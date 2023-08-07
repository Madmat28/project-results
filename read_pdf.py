"""
pdf extract
"""

import tabula as tb
import pandas as pd
import PyPDF2
import re

# extract with PyPDF2

file_name = "ruka_Q.pdf"
pdf = open(file_name, "rb")
reader = PyPDF2.PdfReader(file_name)
page = reader.pages[0]
text = page.extract_text()


class AthleteResult:
    result = ""
    bib = ""
    fis_id = ""
    previous_year_rank = ""
    first_name = ""
    last_name = ""
    country = ""
    birth_year = ""
    time = ""
    time_points = ""
    top_air_judge1 = ""
    top_air_judge2 = ""
    top_air_trick = ""
    top_air_coefficient = ""
    bottom_air_judge1 = ""
    bottom_air_judge2 = ""
    bottom_air_trick = ""
    bottom_air_coefficient = ""
    air_points = ""
    ski_judge1 = ""
    ski_deduction_judge1 = ""
    ski_judge2 = ""
    ski_deduction_judge2 = ""
    ski_judge3 = ""
    ski_deduction_judge3 = ""
    ski_judge4 = ""
    ski_deduction_judge4 = ""
    ski_judge5 = ""
    ski_deduction_judge5 = ""
    base_score = ""
    ski_deduction_total = ""
    ski_points = ""
    total_points = ""

    def __init__(self, string):
        self.find_scores(string)

    # for extracting usefull scores and informations
    def find_scores(self, string: str) -> None:
        """One line descritpion

        Additionnal descritpion and comments

        ```python
        def func():
            return
        ```

        Args:
        ----
            string (str): Descrition of the parameter

        Returns:
        ---------
        ...

        Raises:
        -------
        ...

        """

        def scrape_a_score(
            string, stop_car, num_before_car, num_follow_car, delete_last_car=False
        ):
            i = 0
            output_score = ""

            # add the caracters to the output upto the targeted caracter
            while string[i - 1] != stop_car:
                output_score += string[i]
                i += 1
            rank_car = i - 1

            # add wanted caracters after the targeted caracter
            for n in range(num_follow_car):
                output_score += string[i]
                i += 1

            string = string[i:]
            rank_car = output_score.find(stop_car)

            # remove unwanted caracters before the targeted caracter
            output_score = output_score[rank_car - num_before_car :]
            if delete_last_car == True:
                output_score = output_score[:-1]

            return string, output_score

        # for deleting useless strings
        def delete_string(string, stop_car):
            i = 0
            while string[i - 1] != stop_car:
                i += 1
            string = string[i:]
            return string

        # for finding the length of a string
        def find_length_string(string):
            len_string = 0
            while (
                string[len_string].isupper() == True
                or string[len_string].islower() == True
            ):
                len_string += 1
            return len_string

        def extract_car_from_string(string, num_car):
            output_score = ""
            i = 0
            while i < num_car:
                output_score += string[i]
                i += 1
            string = string[i:]
            return string, output_score

        def find_jump(string, stop_car, delete_last_car=False):
            i = 0
            jump = ""
            while string[i - 1] != stop_car:
                jump += string[i]
                i += 1
            string = string[i:]
            if delete_last_car == True:
                jump = jump[:-1]
            return string, jump

        # Ski deductions judge 1
        string, self.ski_deduction_judge1 = scrape_a_score(string, ".", 2, 1)
        print(f"{self.ski_deduction_judge1=}")

        # Ski judge 1
        string, self.ski_judge1 = scrape_a_score(string, ".", 2, 1)
        print(f"{self.ski_judge1=}")

        string = delete_string(string, " ")
        # Total points
        string, self.total_points = scrape_a_score(string, ".", 2, 2)
        print(f"{self.total_points=}")

        string = delete_string(string, ":")
        string = delete_string(string, ":")

        string, self.country = scrape_a_score(string, "\n", 3, 0, True)
        print(f"{self.country=}")

        string, self.bottom_air_judge1 = scrape_a_score(string, ".", 1, 1)
        print(f"{self.bottom_air_judge1=}")

        string, self.bottom_air_judge2 = scrape_a_score(string, ".", 1, 1)
        print(f"{self.bottom_air_judge2=}")

        string = delete_string(string, " ")

        string, self.bottom_air_trick = scrape_a_score(string, " ", 3, 0, True)
        print(f"{self.bottom_air_trick=}")

        string, self.bottom_air_coefficient = scrape_a_score(string, ".", 1, 2)
        print(f"{self.bottom_air_coefficient=}")

        string, self.ski_points = scrape_a_score(string, ".", 2, 1)
        print(f"{self.ski_points=}")

        string, self.air_points = scrape_a_score(string, ".", 2, 2)
        print(f"{self.air_points=}")

        string, self.time_points = scrape_a_score(string, ".", 2, 2)
        print(f"{self.time_points=}")

        string, self.bib = scrape_a_score(
            string, " ", 1, 0, True
        )  # we have a problem with bib that are 1 carater and bibs with 2 caraters
        print(f"{self.bib=}")

        len_string = find_length_string(string)

        string, self.last_name = scrape_a_score(string, " ", len_string, 0, True)
        print(f"{self.last_name=}")

        len_string = find_length_string(string)

        string, self.first_name = scrape_a_score(string, " ", len_string, 0, True)
        print(f"{self.first_name=}")

        string, self.birth_year = scrape_a_score(string, " ", 4, 0, True)
        print(f"{self.birth_year=}")

        string, self.previous_year_rank = extract_car_from_string(string, 1)
        print(f"{self.previous_year_rank=}")

        string, self.fis_id = scrape_a_score(string, " ", 7, 0, True)
        print(f"{self.fis_id=}")

        string, self.top_air_judge1 = scrape_a_score(string, ".", 1, 1)
        print(f"{self.top_air_judge1=}")

        string, self.top_air_judge2 = scrape_a_score(string, ".", 1, 1)
        print(f"{self.top_air_judge2=}")

        string = delete_string(string, " ")

        string, self.top_air_trick = find_jump(string, " ", True)
        print(f"{self.top_air_trick=}")

        string, self.top_air_coefficient = scrape_a_score(string, ".", 1, 2)
        print(f"{self.top_air_coefficient=}")

        string, self.time = scrape_a_score(string, ".", 2, 2)
        print(f"{self.time=}")

        string, self.time_points = scrape_a_score(string, ".", 2, 2)
        print(f"{self.time_points=}")

        string, self.ski_deduction_judge2 = scrape_a_score(string, ".", 2, 1)
        print(f"{self.ski_deduction_judge2=}")

        string, self.ski_deduction_judge3 = scrape_a_score(string, ".", 2, 1)
        print(f"{self.ski_deduction_judge3=}")

        string, self.ski_deduction_judge4 = scrape_a_score(string, ".", 2, 1)
        print(f"{self.ski_deduction_judge4=}")

        string, self.ski_deduction_judge5 = scrape_a_score(string, ".", 2, 1)
        print(f"{self.ski_deduction_judge2=}")

        string, self.ski_judge2 = scrape_a_score(string, ".", 2, 1)
        print(f"{self.ski_judge2=}")

        string, self.ski_judge3 = scrape_a_score(string, ".", 2, 1)
        print(f"{self.ski_judge3=}")

        string, self.ski_judge4 = scrape_a_score(string, ".", 2, 1)
        print(f"{self.ski_judge4=}")

        string, self.ski_judge5 = scrape_a_score(string, ".", 2, 1)
        print(f"{self.ski_judge5=}")

        string, self.base_score = scrape_a_score(string, ".", 2, 1)
        print(f"{self.base_score=}")

        string, self.ski_deduction_total = scrape_a_score(string, ".", 2, 1)
        print(f"{self.ski_deduction_total=}")

        print(string)


string_test = "-1.017.6 79.06 B:\nD:CAN\n8.5 8.3 7op 0.88\n48.9 14.16 16.001 KINGSBURY Mikael 1992 12484937 7.6 7.8 bF 0.88 20.38 16.00\n-1.2 -1.1 -0.8-0.617.416.9 17.3 17.1 51.8\n-2.9"


KINGSBURY = AthleteResult(string_test)
