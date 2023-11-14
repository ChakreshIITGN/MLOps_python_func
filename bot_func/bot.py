import wikipedia as wp

def scrape(name,length=2):

    try:
        result = wp.summary(name,sentences=length)
        return result
    except:
        return 'The Page doesn\'t exist RUN Again'