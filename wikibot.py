from bot_func.bot import scrape
import click  # pylint: disable=unused-import

## this part is good for a test function but now we implement using click library which is a neater way of passing args.

# def scrape(name="Microsoft",length=2):

#     result = wp.summary(name,sentences=length)
#     return name, result

# usr_input,wiki_result = scrape()

# print(f"Scrape result from Wikipedia for {usr_input} is \n --- {wiki_result} --- ")


@click.command()
@click.option(
    "--name",
    prompt="Wikipedia page name : ",
    help="Scrapes the wikipedia page for the name you enter",
)
@click.option(
    "--length",
    prompt="Length of the Scrape : ",
    help="number of sentences that you want in the scrape",
)
def cli(name, length):
    result = scrape(name, length)
    click.echo(click.style(result, bg="white", fg="cyan"))
    return result


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
