class AthleteResult:
    result = ""
    bib = ""
    fis_id = ""
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
    ski_judge1 = "NaN"
    ski_deduction_judge1 = "NaN"
    ski_judge2 = "NaN"
    ski_deduction_judge2 = "NaN"
    ski_judge3 = "NaN"
    ski_deduction_judge3 = "NaN"
    ski_judge4 = "NaN"
    ski_deduction_judge4 = "NaN"
    ski_judge5 = "NaN"
    ski_deduction_judge5 = "NaN"
    ski_total = ""
    ski_deduction_total = ""
    ski_points = ""
    total_points = ""
    race_points = "NaN"

    def __init__(self, string: str, qualification: bool) -> None:
        self.analyse_string(string, qualification)
        self.result = int(self.result)
        self.bib = int(self.bib)
        self.fis_id = int(self.fis_id)
        self.birth_year = int(self.birth_year)
        if len(self.time.split(".")[1]) != 2:
            error_msg = f"Error: Expected time to have 2 decimals, got {len(self.time.split('.')[1])}"
            raise ValueError(error_msg)
        self.time = float(self.time)

        if len(self.time_points.split(".")[1]) != 2:
            error_msg = f"Error: Expected time points to have 2 decimals, got {len(self.time_points.split('.')[1])}"
            raise ValueError(error_msg)
        self.time_points = float(self.time_points)

        if len(self.top_air_judge1.split(".")[1]) != 1:
            error_msg = f"Error: Expected top_air_judge1 to have 1 decimal, got {len(self.top_air_judge1.split('.')[1])}"
            raise ValueError(error_msg)
        self.top_air_judge1 = float(self.top_air_judge1)

        if len(self.top_air_judge2.split(".")[1]) != 1:
            error_msg = f"Error: Expected top_air_judge2 to have 1 decimal, got {len(self.top_air_judge2.split('.')[1])}"
            raise ValueError(error_msg)
        self.top_air_judge2 = float(self.top_air_judge2)

        if len(self.top_air_coefficient.split(".")[1]) not in [2, 3]:
            error_msg = f"Error: Expected top_air_coefficient to have 2 or 3 decimals, got {len(self.top_air_coefficient.split('.')[1])}"
            raise ValueError(error_msg)
        self.top_air_coefficient = float(self.top_air_coefficient)

    def __str__(self) -> str:
        string = "Athlete Results:\n"
        string += f"Result: {self.result}\n"
        string += f"Bib: {self.bib}\n"
        string += f"FIS ID: {self.fis_id}\n"
        string += f"Athlete Name: {self.last_name} {self.first_name}\n"
        string += f"Country: {self.country}\n"
        string += f"Birth Year: {self.birth_year}\n"
        string += f"Time: {self.time}\n"
        string += f"Time Points: {self.time_points}\n"
        string += f"Top Air Judge 1: {self.top_air_judge1}\n"
        string += f"Top Air Judge 2: {self.top_air_judge2}\n"
        string += f"Top Air Trick: {self.top_air_trick}\n"
        string += f"Top Air Coefficient: {self.top_air_coefficient}\n"
        string += f"Bottom Air Judge 1: {self.bottom_air_judge1}\n"
        string += f"Bottom Air Judge 2: {self.bottom_air_judge2}\n"
        string += f"Bottom Air Trick: {self.bottom_air_trick}\n"
        string += f"Bottom Air Coefficient: {self.bottom_air_coefficient}\n"
        string += f"Air Points: {self.air_points}\n"
        string += f"Ski Judge 1: {self.ski_judge1}\n"
        string += f"Ski Deduction Judge 1: {self.ski_deduction_judge1}\n"
        string += f"Ski Judge 2: {self.ski_judge2}\n"
        string += f"Ski Deduction Judge 2: {self.ski_deduction_judge2}\n"
        string += f"Ski Judge 3: {self.ski_judge3}\n"
        string += f"Ski Deduction Judge 3: {self.ski_deduction_judge3}\n"
        string += f"Ski Judge 4: {self.ski_judge4}\n"
        string += f"Ski Deduction Judge 4: {self.ski_deduction_judge4}\n"
        string += f"Ski Judge 5: {self.ski_judge5}\n"
        string += f"Ski Deduction Judge 5: {self.ski_deduction_judge5}\n"
        string += f"Ski Total: {self.ski_total}\n"
        string += f"Ski Deduction Total: {self.ski_deduction_total}\n"
        string += f"Ski Points: {self.ski_points}\n"
        string += f"Total Points: {self.total_points}\n"
        string += f"Race Points: {self.race_points}\n"
        return string

    def skip_until(self, string, char, pos):
        if pos not in [0, 1, 2]:
            error_msg = f"pos must be in [0, 1, 2], got {pos}"
            raise ValueError(error_msg)

        match pos:
            case 0:
                current_char = 0
                while string[current_char] != char:
                    if current_char == len(string) - 1:
                        return self.strip(string, current_char + 1)
                    current_char += 1
                return self.strip(string, current_char)
            case 1:
                current_char = 1
                last_char = 0
                while string[last_char] != char:
                    current_char += 1
                    last_char += 1
                return self.strip(string, current_char + 1)
            case 2:
                current_char = 2
                last_char = 1
                before_last_char = 0

                while string[before_last_char] != char:
                    current_char += 1
                    last_char += 1
                    before_last_char += 1
                return self.strip(string, current_char + 1)

    def process_jump(self, string):
        if string[:4] in ["10op", "14op"]:
            return self.strip(string, 4)
        if string[:3] in ["7op", "7oG", "bdF", "3oG", "DTS", "10o"]:
            return self.strip(string, 3)
        if string[:2] in ["NJ", "bF", "bp", "bG", "bT", "7o", "IG", "3G", "lG", "bL", "3o", "3p", "fT"]:
            return self.strip(string, 2)
        if string[:1] in ["K", "S", "l", "3"]:
            return self.strip(string, 1)
        error_msg = f"Error: Expected trick but got {string[:4]}."
        raise ValueError(error_msg)

    def pdf_type(self, splited: list, qualification: bool):
        if "B:" in splited[0]:
            match len(splited[0].split(".")):
                case 1:
                    return 1
                case 2:
                    return 2
                case 3:
                    return 3
                case 4:
                    return 4
        elif "B:" in splited[1]:
            if not qualification:
                return 5
            return 6

        error_msg = "Error: Unknown pdf type."
        raise ValueError(error_msg)

    def analyse_string(self, string: str, qualification: bool):  # noqa
        splited = string.split("\n")
        pdf_type = self.pdf_type(splited, qualification)
        string = string.replace("\n", " ")
        string = string.replace(" Q1:", "")
        string = string.replace("PH:", "")
        match pdf_type:
            case 3:
                self.ski_deduction_judge1, string = self.skip_until(string=string, char=".", pos=1)

                self.ski_judge1, string = self.skip_until(string=string, char=".", pos=1)

            case 4:
                self.ski_deduction_judge1, string = self.skip_until(string=string, char=".", pos=1)

                self.ski_judge1, string = self.skip_until(string=string, char=".", pos=1)

                self.total_points, string = self.skip_until(string=string, char=".", pos=2)

            case 5 | 6:
                self.bottom_air_judge1, string = self.skip_until(string=string, char=".", pos=1)

                self.bottom_air_judge2, string = self.skip_until(string=string, char=".", pos=1)

                self.bottom_air_trick, string = self.process_jump(string=string)

                self.bottom_air_coefficient, string = self.skip_until(string=string, char=" ", pos=0)

                self.ski_points, string = self.skip_until(string=string, char=" ", pos=0)

                self.air_points, string = self.skip_until(string=string, char=".", pos=2)

                self.time_points, string = self.skip_until(string=string, char=".", pos=2)

                self.ski_deduction_judge1, string = self.skip_until(string=string, char=".", pos=1)

                self.ski_deduction_judge2, string = self.skip_until(string=string, char=".", pos=1)

                self.ski_deduction_judge3, string = self.skip_until(string=string, char=".", pos=1)

                self.ski_deduction_total, string = self.skip_until(string=string, char=".", pos=1)

        if string[:3] == "B: ":
            string = string[3:]
        else:
            error_msg = "Error: Expected B: but got " + string[:2]
            raise ValueError(error_msg)

        if string[:2] == "D:":
            string = string[2:]
        else:
            error_msg = "Error: Expected D: but got " + string[:2]
            raise ValueError(error_msg)

        self.country, string = self.strip(string, 3)

        match pdf_type:
            case 1 | 2 | 3 | 4:
                self.bottom_air_judge1, string = self.skip_until(string=string, char=".", pos=1)

                self.bottom_air_judge2, string = self.skip_until(string=string, char=".", pos=1)

                self.bottom_air_trick, string = self.process_jump(string=string)

                self.bottom_air_coefficient, string = self.skip_until(string=string, char=" ", pos=0)

                self.ski_points, string = self.skip_until(string=string, char=" ", pos=0)

                self.air_points, string = self.skip_until(string=string, char=".", pos=2)

                self.time_points, string = self.skip_until(string=string, char=".", pos=2)

                self.result, string = self.skip_until(string=string, char=" ", pos=0)

        current_char = 0
        while string[current_char] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            current_char += 1

        full_name = string[:current_char]
        string = string[current_char:]
        full_name = full_name.split(" ")
        for element in full_name:
            if element == "":
                full_name.remove("")

        found = False
        for index, name in enumerate(reversed(full_name)):
            if name == "":
                continue
            caps_letters = 0
            for char in name:
                if char.isupper():
                    caps_letters += 1
                if caps_letters > 1:
                    last_sirname = index
                    found = True
                    break
            if found:
                break
        last_names = full_name[: len(full_name) - last_sirname]
        first_names = full_name[len(full_name) - last_sirname :]

        self.first_name = " ".join(first_names)
        self.last_name = " ".join(last_names)

        self.birth_year, string = self.skip_until(string=string, char=" ", pos=0)

        bib_and_id, string = self.skip_until(string=string, char=" ", pos=0)
        if len(bib_and_id) > 7:
            self.fis_id = bib_and_id[-7:]

            self.bib = bib_and_id[:-7]
        else:
            self.bib = bib_and_id
            self.fis_id, string = self.skip_until(string=string, char=" ", pos=0)

        self.top_air_judge1, string = self.skip_until(string=string, char=".", pos=1)

        self.top_air_judge2, string = self.skip_until(string=string, char=".", pos=1)

        self.top_air_trick, string = self.process_jump(string=string)

        self.top_air_coefficient, string = self.skip_until(string=string, char=" ", pos=0)

        self.time, string = self.skip_until(string=string, char=".", pos=2)

        match pdf_type:
            case 1 | 3 | 5 | 6:
                self.total_points, string = self.skip_until(string=string, char=".", pos=2)

        self.time_points, string = self.skip_until(string=string, char=".", pos=2)

        match pdf_type:
            case 1:
                self.ski_deduction_judge1, string = self.skip_until(string=string, char=".", pos=1)
            case 5:
                self.race_points, string = self.skip_until(string=string, char=" ", pos=0)
                self.race_points = self.race_points.replace(".", "")
                self.race_points = self.race_points.replace("…", "")

        match pdf_type:
            case 1 | 3 | 4:
                self.ski_deduction_judge2, string = self.skip_until(string=string, char=".", pos=1)

                self.ski_deduction_judge3, string = self.skip_until(string=string, char=".", pos=1)

                self.ski_deduction_judge4, string = self.skip_until(string=string, char=".", pos=1)

                self.ski_deduction_judge5, string = self.skip_until(string=string, char=".", pos=1)
            case 5 | 6:
                self.total_points, string = self.skip_until(string=string, char=".", pos=2)

        match pdf_type:
            case 1 | 5 | 6:
                self.ski_judge1, string = self.skip_until(string=string, char=".", pos=1)

        self.ski_judge2, string = self.skip_until(string=string, char=".", pos=1)

        self.ski_judge3, string = self.skip_until(string=string, char=".", pos=1)

        match pdf_type:
            case 1 | 3 | 4:
                self.ski_judge4, string = self.skip_until(string=string, char=".", pos=1)

                self.ski_judge5, string = self.skip_until(string=string, char=".", pos=1)

        self.ski_total, string = self.skip_until(string=string, char=".", pos=1)
        match pdf_type:
            case 1 | 3 | 4:
                self.ski_deduction_total, string = self.skip_until(string=string, char=".", pos=1)
            case 5 | 6:
                self.result, string = self.skip_until(string=string, char=" ", pos=0)

    def strip(self, string: str, end: int):
        attr = string[0:end]
        string = string[end:]

        while len(string) > 0 and string[0] == " ":
            string = string[1:]
        return attr, string


if __name__ == "__main__":
    full_name = "OFFEL VILLAUCOURT de Arthur"
    full_name = full_name.split(" ")
    print(full_name)
    for index, name in enumerate(reversed(full_name)):
        if name == "":
            continue
        caps_letters = 0
        for char in name:
            if char.isupper():
                caps_letters += 1
            if caps_letters > 1:
                last_sirname = index
                break
    last_names = full_name[: len(full_name) - last_sirname]
    first_names = full_name[len(full_name) - last_sirname :]

    first_name = " ".join(first_names)
    last_name = " ".join(last_names)
    print(first_name) + "|"
    print(last_name) + "|"
