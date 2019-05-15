
# ## NASA Mars News
# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd

def scrape():
    base_url = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    response_news = requests.get(base_url)

    soup_news = BeautifulSoup(response_news.text, 'html.parser')

    # Examine the results, then determine element that contains sought info
    #print(soup_news.prettify())

    #str(soup_news.find_all('div', class_="image_and_description_container")[0].a).split('''"''')[1]

    start_url = "https://mars.nasa.gov" + str(soup_news.find_all('div', class_="image_and_description_container").a)[0].split('''"''')[1]
    #start_url

    # Retrieve page with the requests module
    response_start_news = requests.get(start_url)

    soup_start_news = BeautifulSoup(response_start_news.text, 'html.parser')

    # Examine the results, then determine element that contains sought info
    #print(soup_start_news.prettify())

    #str(soup_start_news.find_all('a', class_ = 'article_nav_block next')[0]).split(" ")

    #str(soup_start_news.select('meta[name="description"]')[0]).split('''"''')[1]


    link = soup_start_news.find_all('a', class_ = 'article_nav_block next')
    #str(link[0]).split(" ")[3].split('''"''')[1]

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(start_url)

    news_titles = []
    news_paragraphs = []

    html = browser.html
    soup_item = BeautifulSoup(html, 'html.parser')

    news_title = soup_item.find('h1').text
    news_titles.append(news_title)

    news_paragraph = str(soup_item.select('meta[name="description"]')[0]).split('''"''')[1]
    news_paragraphs.append(news_paragraph)

    # for x in range(0, 86):

    #     html = browser.html
    #     soup_item = BeautifulSoup(html, 'html.parser')

    #     news_title = soup_item.find('h1').text
    #     news_titles.append(news_title)
    #     link = soup_item.find_all('a', class_ = 'article_nav_block next')
    #     news_paragraph = str(soup_item.select('meta[name="description"]')[0]).split('''"''')[1]
    #     news_paragraphs.append(news_paragraph)

        # print('page:', x, '-------------')    
        # print(news_title) 
        # print('  ')
        # print(news_paragraph)
        # print('  ')    

        #browser.click_link_by_href(str(link[0]).split(" ")[3].split('''"''')[1])

    latest_new_title = news_titles[0].replace("\n", "")
    #latest_new_title

    latest_new_paragraph = news_paragraphs[0]
    #latest_new_paragraph


    # ## JPL Mars Space Images - Featured Image

    images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(images_url)

    browser.click_link_by_partial_text("FULL IMAGE")


    html = browser.html

    soup_images = BeautifulSoup(html, 'html.parser')

    #print(soup_images.prettify())


    #featured_image_url = soup.find_all("article", class_="carousel_item")
    featured_image_url = str(soup_images.find_all("a", class_="button fancybox")[0]).split('''"''')[7]
    full_featured_image_url = "https://www.jpl.nasa.gov" + featured_image_url
    #full_featured_image_url


    # ## Mars Weather

    mars_weather_url = "https://twitter.com/marswxreport?lang=en"

    response_weather = requests.get(mars_weather_url)

    soup_weather = BeautifulSoup(response_weather.text, 'html.parser')

    #print(soup_weather.prettify())

    mars_weather = soup_weather.find_all("div", class_="js-tweet-text-container")[0].p.contents[0].replace("\n", " ")
    #mars_weather


    # ## Mars Facts

    mars_facts_url = "https://space-facts.com/mars/"

    tables = pd.read_html(mars_facts_url)
    tables

    mar_facts_df = tables[0]
    mar_facts_df.columns = ['Parameter', 'Value']
    mar_facts_df

    mars_fact_html_table = mar_facts_df.to_html()
    #mars_fact_html_table


    # ## Mars Hemispheres

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    hemisphere_image_urls = []

    browser.visit(mars_hemispheres_url)

    browser.click_link_by_partial_text("Cerberus Hemisphere Enhanced")

    html_cerberus_hemisphere = browser.html

    soup_cerberus_hemisphere = BeautifulSoup(html_cerberus_hemisphere, 'html.parser')

    #print(soup_cerberus_hemisphere.prettify())

    #str(soup_cerberus_hemisphere.body.div.li.a).split('''"''')[1]

    cerberus_hemisphere_dict = {"title": "Cerberus Hemisphere",
                            "img_url": str(soup_cerberus_hemisphere.body.div.li.a).split('''"''')[1]}
    #cerberus_hemisphere_dict

    hemisphere_image_urls.append(cerberus_hemisphere_dict)
    #hemisphere_image_urls

    browser.visit(mars_hemispheres_url)
    browser.click_link_by_partial_text("Schiaparelli Hemisphere Enhanced")

    html_schiaparelli_hemisphere = browser.html
    soup_schiaparelli_hemisphere = BeautifulSoup(html_schiaparelli_hemisphere, 'html.parser')
    #print(soup_schiaparelli_hemisphere.prettify())

    #str(soup_schiaparelli_hemisphere.body.div.li.a).split('''"''')[1]

    schiaparelli_hemisphere_dict = {"title": "Schiaparelli Hemisphere",
                            "img_url": str(soup_schiaparelli_hemisphere.body.div.li.a).split('''"''')[1]}
    #schiaparelli_hemisphere_dict

    hemisphere_image_urls.append(schiaparelli_hemisphere_dict)
    #hemisphere_image_urls

    browser.visit(mars_hemispheres_url)
    browser.click_link_by_partial_text("Syrtis Major Hemisphere Enhanced")

    html_syrtis_major_hemisphere = browser.html
    soup_syrtis_major_hemisphere = BeautifulSoup(html_syrtis_major_hemisphere, 'html.parser')
    #print(soup_syrtis_major_hemisphere.prettify())

    #str(soup_syrtis_major_hemisphere.body.div.li.a).split('''"''')[1]

    syrtis_major_hemisphere_dict = {"title": "Syrtis Major Hemisphere",
                            "img_url": str(soup_syrtis_major_hemisphere.body.div.li.a).split('''"''')[1]}
    #syrtis_major_hemisphere_dict

    hemisphere_image_urls.append(syrtis_major_hemisphere_dict)
    #hemisphere_image_urls

    browser.visit(mars_hemispheres_url)
    browser.click_link_by_partial_text("Valles Marineris Hemisphere Enhanced")

    html_valles_marineris_hemisphere = browser.html
    soup_valles_marineris_hemisphere = BeautifulSoup(html_valles_marineris_hemisphere, 'html.parser')
    #print(soup_valles_marineris_hemisphere.prettify())

    #str(soup_valles_marineris_hemisphere.body.div.li.a).split('''"''')[1]

    valles_marineris_hemisphere_dict = {"title": "Valles Marineris Hemisphere",
                            "img_url": str(soup_valles_marineris_hemisphere.body.div.li.a).split('''"''')[1]}
    #valles_marineris_hemisphere_dict

    hemisphere_image_urls.append(valles_marineris_hemisphere_dict)

    results_dict = {"latest_news": {"title": latest_new_title,
                                    "paragraph": latest_new_paragraph
                                    },
                    "featured_mars_image": full_featured_image_url,
                    "mars_weather": mars_weather,
                    "mars_facts": mars_fact_html_table,
                    "mars_hemispheres": hemisphere_image_urls
                    }
    return results_dict

