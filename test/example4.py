__author__ = 'pretty moon'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://appexchange.salesforce.com/listingDetail?listingId=a0N300000026fvXEAQ')
try:

    # scrape elements from OVERVIEW page
    ###################################

    consultantTitle = "CONSULTANT TITLE" #browser.find_element_by_xpath("//h1[@id='listingName']/span/h5")
    consultant = browser.find_element_by_xpath("//h1[@id='listingName']") #.find_element_by_xpath("//strong")
    print(consultantTitle + ' : ' + consultant.text)

    releasedTitle = browser.find_element_by_class_name('hidden-phone').find_element_by_xpath("//h5")
    released = browser.find_element_by_class_name('hidden-phone').find_element_by_xpath("//strong")
    print(releasedTitle.text + ' : ' + released.text)

    cerProfTitle = browser.find_element_by_xpath("//span[@id='listingDetailPage:AppExchangeLayout:listingDetailForm:listingDetailOverviewTab:listingDetailOverviewTabComp:svcDetails']/h5[1]")
    cerProf = browser.find_element_by_xpath("//span[@id='listingDetailPage:AppExchangeLayout:listingDetailForm:listingDetailOverviewTab:listingDetailOverviewTabComp:svcDetails']/p[1]/strong") #.find_element_by_xpath("//strong")
    print(cerProfTitle.text + ' : ' + cerProf.text)

    prjHisTitle = browser.find_element_by_xpath("//span[@id='listingDetailPage:AppExchangeLayout:listingDetailForm:listingDetailOverviewTab:listingDetailOverviewTabComp:svcDetails']/h5[2]")
    prjHis = browser.find_element_by_xpath("//span[@id='listingDetailPage:AppExchangeLayout:listingDetailForm:listingDetailOverviewTab:listingDetailOverviewTabComp:svcDetails']/p[2]/strong")
    print(prjHisTitle.text + ' : ' + prjHis.text)

    partnerLevelTitle = browser.find_element_by_xpath("//span[@id='listingDetailPage:AppExchangeLayout:listingDetailForm:listingDetailOverviewTab:listingDetailOverviewTabComp:svcDetails']/h5[3]")
    partnerLevel = browser.find_element_by_xpath("//span[@id='listingDetailPage:AppExchangeLayout:listingDetailForm:listingDetailOverviewTab:listingDetailOverviewTabComp:svcDetails']/p[4]/strong")
    print(partnerLevelTitle.text + ' : ' + partnerLevel.text)

    typeOfServiceTitle = browser.find_element_by_xpath("//span[@id='listingDetailPage:AppExchangeLayout:listingDetailForm:listingDetailOverviewTab:listingDetailOverviewTabComp:j_id285']/span/h5")
    #typeOfService = browser.find_element_by_xpath("//span[@id='listingDetailPage:AppExchangeLayout:listingDetailForm:listingDetailOverviewTab:listingDetailOverviewTabComp:j_id285']/span/p/a[1]/strong")
    #print(typeOfServiceTitle.text + ' : ' + typeOfService.text)

    typeOfServices = browser.find_elements_by_xpath("//span[@id='listingDetailPage:AppExchangeLayout:listingDetailForm:listingDetailOverviewTab:listingDetailOverviewTabComp:j_id285']/span/p/a")
    for tos in typeOfServices:
        print(tos.find_element_by_tag_name('strong').text)

    # scrape elements from DETAILS page
    ###################################

    detailsBotton = browser.find_element_by_xpath("//a [@id='tab_content_details']/span")
    print(detailsBotton.text)
    detailsBotton.click()

    lang= browser.find_elements_by_xpath("//div[@id='languagesSpoken']/h5")
    print(lang.text)
    languagesSpoken = browser.find_elements_by_xpath("//div[@id='languagesSpoken']/p/a")
    print(len(languagesSpoken))
    for langSpk in languagesSpoken:
        print(langSpk.find_element_by_tag_name('span').text)

    ####################################################################################
    #menu = browser.find_element_by_css_selector(".nav")
    #hidden_submenu = browser.find_element_by_css_selector("#tab_content_provider")

    #actions = ActionChains(browser)
    #actions.move_to_element(menu).click(hidden_submenu).perform()
    ##############################################################

    # scrape elements from PROVIDER page
    ###################################
    providerBotton = browser.find_element_by_xpath("//a[@id='tab_content_provider']/span")
    print(providerBotton.text)
    providerBotton.click()

    #browser.close()


except:
    print('Was not able to scrape this page.')