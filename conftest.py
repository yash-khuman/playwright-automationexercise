import pytest
from pathlib import Path
from datetime import datetime
from typing import Generator
from playwright.sync_api import (
    sync_playwright,
    Browser,
    BrowserContext,
    Page,
)


# --------------------------
# Browser (one per session)
# --------------------------
@pytest.fixture(scope="session")
def browser_fixture() -> Generator[Browser, None, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False
        )

        yield browser

        browser.close()


# --------------------------
# Fresh browser context
# --------------------------
@pytest.fixture
def context_fixture(
    browser_fixture,
) -> Generator[BrowserContext, None, None]:

    context = browser_fixture.new_context()

    yield context

    context.close()



# --------------------------
# Trace wrapper
# --------------------------
@pytest.fixture
def traced_context_fixture(
    context_fixture,
    request,
) -> Generator[BrowserContext, None, None]:

    context_fixture.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    yield context_fixture

    failed = (
        hasattr(request.node, "rep_call")
        and request.node.rep_call.failed
    )

    if failed:
        trace_dir = Path("traces")
        trace_dir.mkdir(exist_ok=True)

        trace_path = (
            trace_dir
            / f"{request.node.name}-{datetime.now():%Y%m%d-%H%M%S}.zip"
        )

        context_fixture.tracing.stop(
            path=str(trace_path)
        )

        print(f"\nTrace saved: {trace_path}")

    else:
        context_fixture.tracing.stop()


# --------------------------
# Page fixture
# --------------------------
@pytest.fixture
def page_fixture(
    traced_context_fixture,
) -> Generator[Page, None, None]:

    page = traced_context_fixture.new_page()

    yield page

    page.close()
