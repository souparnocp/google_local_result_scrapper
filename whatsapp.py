import json
import csv
import argparse
from outscraper import ApiClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()


def save_to_file(dict_json, file_name):

    header = ['name', 'full_address', 'phone', 'site', 'rating']

    data = []
   
    for dict in dict_json:
            data.append([dict['name'], dict['full_address'], dict['phone'], dict['site'], dict['rating']])
    
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)

    print("csv file created")
    
def filterWhatsapp(filename):
    file = open(filename)
    csvreader = csv.reader(file)
    data=[]
    
    driver.get("https://web.whatsapp.com")
    time.sleep(5)
    rows = []
    for row in csvreader:
        rows.append(row)
    print(rows,"rows")    
    for dict in rows:
        phone=dict[2].replace(" ","").replace("+","")
        driver.get("https://web.whatsapp.com/send?phone=$"+ phone + "&text&app_absent=0")
        time.sleep(5)
        print(dict)
        if len(driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/span[2]/div[1]/span/div[1]/div/div/div")) == 0: 
             #print(response.status_code)
            data.append([dict[0], dict[1], dict[2], dict[3], dict[4]])
        else:
            #print(response.status_code)
            data.append([dict[0], dict[1],'',dict[3], dict[4]])
    print(data,"data")        
    return data

def save_to_file2(data,file_name):
    header = ['name', 'full_address', 'phone', 'site', 'rating']
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        print(f,"f")
        writer = csv.writer(f)
        
        #write the header
        #writer.writerow(header)

        #write multiple rows
        writer.writerows(data)

    print("csv file created")
def main():
    ap = argparse.ArgumentParser()

    
    ap.add_argument('-o', help='csv output file',  required=True)


    args = ap.parse_args()

    
    data2=filterWhatsapp(args.o)
    new_args=args.o.split("\\."); 
    save_to_file2(data2,new_args[0]+"_filter.csv")
    print("succefully completed")


if __name__ == '__main__':
    main()