import matplotlib
import pandas as panda
import json
import datetime


class Regression:
    def __init__(self):
        self.file_filled = False
        self.window_height = 800
        self.window_width = 800
        self.data_storage = "data_storage.json"
        self.clean_up_data()

    def clean_up_data(self):
        if not self.file_filled:
            with open('electric_bill_data.json', 'r') as file:
                data = json.load(file)

            # Clean up actual data
            for record in data:
                # Deleting the cost variable
                del record['COST']
                # Formatting the start date and end date to make it readable
                start_date_index = record['START DATE'].index('T')
                record['START DATE'] = record['START DATE'][:start_date_index]
                end_time_index = record['END DATE'].index('T')
                record['END DATE'] = record['END DATE'][:end_time_index]

                # Making the temperature data into actual integers
                record['Average temp(High)'] = float(record['Average temp(High)'].strip('FC'))
                record['Average temp(Low)'] = float(record['Average temp(Low)'].strip('FC'))

                # Clear up all inconsistent data
                self.change_inconsistent_data(record)

            # Saves up in a json file to not have to redo the data changing everytime the program is run
            with open(self.data_storage, "w") as filing:
                filing.write("[\n")  # Start the JSON array
                self.data_length = 0
                for i, entry in enumerate(data):
                    json.dump(entry, filing, indent=4)
                    if i < len(data) - 1:
                        filing.write(",\n")  # Add a comma and a newline after each entry except the last
                    else:
                        filing.write("\n")  # Just a newline after the last entry
                    self.data_length+=1

                filing.write("]\n")  # Close the JSON array

    def change_inconsistent_data(self, record):
        # Fix up any timing issues like half month/ 10 days etc.
        # Saving the start and end dates in start_date and end_date
        start_date = datetime.datetime.strptime(record['START DATE'], "%Y-%m-%d")
        end_date = datetime.datetime.strptime(record['END DATE'], "%Y-%m-%d")
        difference = end_date - start_date

        # Cleaning up consumption and solar export inconsistencies coming from timing inconsistencies
        if difference.days != 30:
            percent_of_days = difference.days / 30
            multiplier = 1 / percent_of_days
            # Changing the Data
            record['USAGE (kWh)'] = round(record['USAGE (kWh)'] * multiplier, 1)
            record['Consumption (kWH)'] = round(record['Consumption (kWH)'] * multiplier, 1)
            record['Solar Export(kWH)'] = round(record['Solar Export(kWH)'] * multiplier, 1)


    def create_x_equations(self):
        input = []
        output = []
        with open('data_storage.json', 'r') as file:
            data = json.load(file)

        for record in data:
            x = record['Average temp(High)']-record['Average temp(Low)']


        pass


if __name__ == "__main__":
    sol = Regression()
