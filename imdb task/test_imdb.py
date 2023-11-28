import pytest
from Task_26  import Imdb_Search  # Replace with the actual name of your script file

@pytest.fixture
def imdb_search_instance():
    imdb_search = Imdb_Search()
    yield imdb_search
    imdb_search.driver.quit()

def test_imdb_search_button_click(imdb_search_instance):
    # Access the data and perform the search
    imdb_search_instance.access_data()

    # Assert that the search button is clicked
    expected_url = "https://www.imdb.com/search/name/result_page_url"  # Replace with the expected URL
    assert imdb_search_instance.driver.current_url == expected_url, "Search button not clicked!"
