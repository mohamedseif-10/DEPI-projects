import time
import regex as re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

print("--------------------------------------------------------------------------------")
print("Hello, This application will help you to scrape jobs from WUZZUUF website")
while True:
    userChoice = int(input("1. Data Science\n2. Engineering\n3. Software Development\n4. Back-End Development\n5. Front-End Development\n6. Full-Stack Development\n7. Mobile Development\n8. Web Development\n9. DevOps\n10. Cloud Computing\n11. Cyber Security\n12. Artificial Intelligence\nPlease chose the job title you want to search for: "))
    if userChoice in range(1, 13):
        break
    else:
        print("Invalid choice, Please try again")


JobsDict = {
    1: "data%20science",
    2: "engineering",
    3: "software%20development",
    4: "back-end%20development",
    5: "front-end%20development",
    6: "full-stack%20development",
    7: "mobile%20development",
    8: "web%20development",
    9: "devops",
    10: "cloud%20computing",
    11: "cyber%20security",
    12: "artificial%20intelligence",
}
baseURL = f"https://wuzzuf.net/search/jobs/?a=spbl&q={JobsDict[userChoice]}"
numPages = int(input("Enter the number of pages you want to scrape: "))


jobs = []
for page in range(numPages):
    url = f"{baseURL}&start={page}" if page > 0 else baseURL
    print(f"Scraping page: {page + 1} of {numPages}")
    driver.get(url)
    time.sleep(10)

    jobsList = driver.find_elements(By.CLASS_NAME, "css-pkv5jc")
    for job in jobsList:
        try:
            jobTitle = job.find_element(By.CLASS_NAME, "css-o171kl").text
            CompanyName = job.find_element(By.CLASS_NAME, "css-17s97q8").text
            CompanyLocation = job.find_element(By.CLASS_NAME, "css-5wys0k").text
            jobType = job.find_element(By.CLASS_NAME, "css-1ve4b75").text

            try:
                element = job.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div[2]/div[2]")
                links = element.find_elements(By.TAG_NAME, "a")
                texts = []
                for link in links:
                    texts.append(link.text)
                all_text = " ".join(texts)
                Requirements = re.sub(r"[^\x00-\x7F]+", " ", all_text)
                Requirements = re.sub(r"\s+-\s+", ", ", Requirements).strip()
                Requirements = re.sub(r"\s+", " ,", Requirements)

            except Exception as e:
                print(f"Error finding or processing Requirements: {e}")
                Requirements = ""

            CompanyName = CompanyName.replace(" -", "")

            jobs.append((jobTitle, CompanyName, CompanyLocation, jobType, Requirements))
        except Exception as e:
            print(f"Error extracting job data: {e}")


df = pd.DataFrame(
    jobs,
    columns=[
        "Job Title",
        "Company Name",
        "Company Location",
        "Job Type",
        "Requirements",
    ],
)

df.to_csv("jobs_data.csv", index=False)

for job in jobs:
   print("--------------------------------------------------------------------------------")
   print(f"Job Title: {job[0]} \nCompany Name: {job[1]} \nCompany Location: {job[2]} \nJob Type: {job[3]} \nRequirements: {job[4]}")
print("--------------------------------------------------------------------------------")


driver.quit()
