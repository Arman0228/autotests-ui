import allure
from playwright.sync_api import Playwright, Page
from config import settings

def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        storage_state: str | None = None
) -> Page:
    browser = playwright.chromium.launch(headless=settings.headless, args=["--ignore-certificate-errors"])
    context = browser.new_context(storage_state=storage_state,ignore_https_errors=True, record_video_dir=settings.videos_dir)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
    browser.close()

    # Прикрепляем файл с трейсингом к Allure отчету
    allure.attach.file(settings.tracing_dir.joinpath(f'{test_name}.zip'), name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)