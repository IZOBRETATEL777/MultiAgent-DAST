from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def visit_page(url, driver, visited_urls, redirections, depth, max_depth):
    if depth > max_depth:
        return

    driver.get(url)
    current_url = driver.current_url

    if current_url not in visited_urls:
        visited_urls.add(current_url)
        print(f"Visiting: {current_url}")

        # Make Security Test
        input_fields = driver.find_elements(By.XPATH, '//input[@type="text"]')
        for field in input_fields:
            field.send_keys("hi")
        
        # Collect links to treat as redirections without following them
        if depth < max_depth:
            links = driver.find_elements(By.TAG_NAME, 'a')
            for link in links:
                href = link.get_attribute('href')
                if href and href.startswith('http'):
                    redirections.add(href)

def automate_browser(url, max_depth=1):
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    visited_urls = set()
    redirections = set()
    
    try:
        visit_page(url, driver, visited_urls, redirections, 0, max_depth)
    finally:
        driver.quit()
    
    print("Completed. Visited URLs:", visited_urls)
    print("Redirections:", redirections)
    return redirections

def run(link):
    redirections = automate_browser(link)
    return redirections

if __name__ == '__main__':
    print(run('http://localhost:3000/'))

