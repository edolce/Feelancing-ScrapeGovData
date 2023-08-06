import requests
import json
import pandas as pd
import os

directory = 'input_excel_files'
csv_file = "final_results.csv"

def get_json(uud):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,ar;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://electoralsearch.eci.gov.in',
        'Pragma': 'no-cache',
        'Referer': 'https://electoralsearch.eci.gov.in/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'applicationName': 'ELECTORAL_SEARCH',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-gpc': '1',
    }

    json_data = {
        'isPortal': True,
        'epicNumber': uud,
    }

    response = requests.post(
        'https://gateway.eci.gov.in/api/v1/elastic/search-by-epic-from-national-display',
        headers=headers,
        json=json_data,
    )
    data = response.json()
    i = 0
    value_list = []
    for ele in data:
        i = i + 1
        content = ele["content"]
        NO = str(i)
        epicNumber = content["epicNumber"]
        applicantFirstName = content["applicantFirstName"]
        applicantFirstNameL1 = content["applicantFirstNameL1"]
        age = content["age"]
        relationName = content["relationName"]
        relationNameL1 = content["relationNameL1"]
        stateName = content["stateName"]
        district = str(content["districtNo"]) + "-" + str(content["districtValue"])
        assemble = str(content["acNumber"]) + "-" + str(content["asmblyName"])
        Part = str(content["partNumber"]) + "-" + str(content["partName"])
        psbuildingName = content["psbuildingName"]
        partSerialNumber = content["partSerialNumber"]
        value_list.append([NO, epicNumber, applicantFirstName, applicantFirstNameL1, age, relationName, relationNameL1,
                      stateName, district, assemble, Part, psbuildingName, partSerialNumber])
    return value_list

value_list = ["S. NO.","Epic Number","Name","Name1","Age","Relative Name","Relative Name1","State","District","Assembly Constituency","Part","Polling Station","Part Serial Number"]
df = pd.DataFrame([value_list])
df.to_csv(csv_file, mode='w', header=False, index=False)

column_b_values = []
for filename in os.listdir(directory):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(directory, filename)
        data = pd.read_excel(file_path)  # Read the XLSX file
        column_b_values.extend(data['UID'].tolist())  # Append column B values to the list
a = len(column_b_values)
for value in column_b_values:
    a = a - 1
    print(a,value)
    try:
        value_list = get_json(value)

        df = pd.DataFrame(value_list)
        df.to_csv(csv_file, mode='a', header=False, index=False, encoding="utf-8-sig")
    except Exception as e:
        print(e)

df = pd.read_csv(csv_file)

# Convert DataFrame to XLSX
df.to_excel(csv_file.replace("csv","xlsx"), index=False)

"SGU6791008.json"