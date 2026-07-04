from playwright.sync_api import Page, TimeoutError

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