import wikipedia as wp

def scrape(name="Microsoft",length=2):

    result = wp.summary(name,sentences=length)
    return name, result

usr_input,wiki_result = scrape()

print(f"Scrape result from Wikipedia for {usr_input} is \n --- {wiki_result} --- ")