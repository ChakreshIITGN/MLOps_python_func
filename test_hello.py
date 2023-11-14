from hello import add, sub
from bot_func.bot import scrape
from wikibot import cli
from click.testing import CliRunner


def test_add():
    assert 2 == add(1, 1)


def test_sub():
    assert -1 == sub(4, 5)


def test_scrape():
    assert "Microsoft" in scrape("Microsoft")


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(cli, ["--name", "Microsoft", "--length", "5"])
    assert result.exit_code == 0
    assert "Microsoft" in result.output
