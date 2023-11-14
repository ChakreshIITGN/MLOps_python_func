import wikipedia as wp
import click

## this part is good for a test function but now we implement using click library which is a neater way of passing args. 

# def scrape(name="Microsoft",length=2):

#     result = wp.summary(name,sentences=length)
#     return name, result

# usr_input,wiki_result = scrape()

# print(f"Scrape result from Wikipedia for {usr_input} is \n --- {wiki_result} --- ")

@click.command()
@click.option('--name', prompt='Wikipedia page name : ',
              help='Scrapes the wikipedia page for the name you enter')
def scrape(name,length=2):

    result = wp.summary(name,sentences=length)
    click.echo(click.style(result, bg='white', fg='cyan'))
    return result

if __name__ == '__main__':
    scrape()