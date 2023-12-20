from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# set up the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Method for checking if a feature is MANE Select
def check_mane_select(feature):
    url = f"https://www.ncbi.nlm.nih.gov/nuccore/{feature}"
    driver.get(url)
    driver.implicitly_wait(10)
    try:
        # track down the genbank_pre element
        genbank_pre = driver.find_element(By.CLASS_NAME, 'genbank')
        if 'MANE Select' in genbank_pre.text:
            return True
    except:
        return False
    return False

#clear previous data
with open('MANE_select.txt', 'w') as file:
    file.write('')
file.close()    

# Read the data from the txt file
with open('data.txt', 'r') as file:
    lines = file.readlines()

# skip the first line which is the header
lines = lines[1:]
features_list = []

# loop through each line in the file, save all the unique column 8, "feature"
for line in lines:
    columns = line.split('\t')
    feature = columns[8]
    if feature not in features_list:
        features_list.append(feature)
print(features_list)

mane_select_list = []
# check mane select for each feature
# save the MANE Select information
for feature in features_list:
    if check_mane_select(feature):
        mane_select_list.append(feature)

# Loop through each line in the file and check for 'MANE Select'
for line in lines:
    columns = line.split('\t')
    feature = columns[8]
    if feature in mane_select_list:
        #print(line)  # or save the information as needed
        #save the infromation to a new file
        with open('MANE_select.txt', 'a') as file:
            file.write(line)

print('Done!')
file.close()

# close the browser
driver.quit()