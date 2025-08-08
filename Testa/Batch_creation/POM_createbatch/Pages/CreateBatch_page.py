import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.create_batch_page import CreateBatchPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Edge
    driver.maximize_window()
    yield driver
    driver.quit()


def test_create_batch(driver):
    driver.get("https://preprod.testaonline.com/exam-management/create-batch")

    batch_page = CreateBatchPage(driver)

    batch_page.enter_batch_details("BATCH123", "50", "03-25-2025", "10:00 AM", "04-10-2025", "12:00 PM")
    batch_page.select_scheme("Scheme A")
    batch_page.select_sub_scheme("Sub-Scheme 1")
    batch_page.select_batch_mode("Online")
    batch_page.select_exam_center("Exam Center 1")
    batch_page.submit_batch()

    # Verify success message
    success_message = "Batch created successfully"  # Update with actual message
    assert success_message in driver.page_source, "Batch creation failed!"
