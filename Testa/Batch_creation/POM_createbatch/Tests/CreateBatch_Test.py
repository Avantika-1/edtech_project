import pytest
from POM_createbatch.CreateBatch_page import CreateBatch_page


def test_create_batch(login):  # `login` fixture is automatically available
    driver = login  # Login fixture returns the logged-in driver

    driver.get("https://preprod.testaonline.com/exam-management/create-batch")

    batch_page = CreateBatchPage(driver)
    batch_page.enter_batch_details("BATCH123", "50", "03-25-2025", "10:00 AM", "04-10-2025", "12:00 PM")
    batch_page.select_scheme("Scheme A")
    batch_page.select_sub_scheme("Sub-Scheme 1")
    batch_page.select_batch_mode("Online")
    batch_page.select_exam_center("Exam Center 1")
    batch_page.submit_batch()

    assert "Batch created successfully" in driver.page_source
