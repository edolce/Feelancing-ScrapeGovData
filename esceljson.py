import json

import openpyxl as openpyxl

if __name__ == '__main__':

    # Specify the path of the Excel file
    file_path = "data.xlsx"

    # Specify the column name to fetch the data
    column_name = "UID"

    def get_column_data(file_path, column_name):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        column_data = []

        # Get the column index based on the column name
        column_index = None
        for row in sheet.iter_rows(min_row=1, max_row=1):
            for cell in row:
                if cell.value == column_name:
                    column_index = cell.column_letter
                    break
            if column_index:
                break

        # If the column is found, fetch its data
        if column_index:
            for cell in sheet[column_index]:
                if cell.row != 1:  # Skip the header row
                    column_data.append(cell.value)

        workbook.close()

        return column_data

    get_column_data(file_path, column_name)