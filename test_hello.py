from hello import add,sub 
from wikibot import scrape

def test_add():

    assert 2 == add(1,1)

def test_sub():

    assert -1 == sub(4,5)

# def test_scrape():

#     assert "Microsoft" in scrape("Microsoft")