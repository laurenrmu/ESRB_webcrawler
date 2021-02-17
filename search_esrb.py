from selenium import webdriver

def search(missing):
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    driver.implicitly_wait(9) # gives an implicit wait for 9 seconds
    url = r'https://www.esrb.org/search/?searchKeyword='
    tup=[]
    for i in missing['Rank']:
        name=missing['Name'].loc[missing['Rank']==i]
        name=repr(name).split('   ')[1].split('\nName:')[0]
        driver.get(url+name)
        try:
            element = driver.find_element_by_xpath('//*[@id="results"]/div[1]/div[2]/table/tbody/tr[2]/td[1]/img')
            esrb_img=element.get_attribute("src")
            esrb_rating = esrb_img.split('/')[-1].split('.')[0]
            tup.append((i,name,esrb_rating))
        except:
            tup.append((i,name,'Unknown'))
    return tup
