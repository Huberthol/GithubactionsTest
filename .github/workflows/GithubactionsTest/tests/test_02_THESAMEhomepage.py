import time


def test_main_page_text(driver):
    driver.get("https://ideaxpose.com/en")

    assert "Design your future with ideaXPOSE" in driver.page_source

def testTEST_main_page_text(driver):
    driver.get("https://ideaxpose.com/en")

    assert "Design your future with ideaXPOSE" in driver.page_source
