from playwright.sync_api import Page, TimeoutError
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEST_FILES = PROJECT_ROOT / "test_data" / "test_files"

class Helper:
    @staticmethod
    def close_ads(page: Page):
        frames = page.locator("iframe[name^='aswift_']")

        for i in range(frames.count()):
            try:
                frame = frames.nth(i).content_frame
                if frame is None:
                    continue

                button = frame.get_by_role("button", name="Close ad")

                if button.is_visible(timeout=300):
                    button.click()
                    return
            except TimeoutError:
                continue
            except Exception:
                continue

    @staticmethod
    def get_test_file(file_name : str) -> Path:
        path = TEST_FILES / file_name

        if not path.exists():
            raise FileNotFoundError(f"Test File Was Not Found : {path}")
        
        return path
        