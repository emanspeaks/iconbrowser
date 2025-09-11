from unittest import TestCase, main as utmain, TextTestRunner, mock
import sys
from os import environ
from pathlib import Path

HERE = Path(__file__).expanduser().resolve().parent
REPOROOT = HERE.parent
if __name__ == '__main__':
    sys.path.append(str(REPOROOT))

    # so we can get testing constants without importing iconbrowser
    sys.path.insert(0, str(REPOROOT/'iconbrowser/_testing'))

from _iconbrowser_testing import (  # noqa: E402
    ENV_ICONBROWSER_UNITTEST_ACTIVE,
)


@mock.patch.dict(environ, {ENV_ICONBROWSER_UNITTEST_ACTIVE: '1'})
class TestIconBrowser(TestCase):
    def test_import(self):
        import iconbrowser  # noqa: F401


if __name__ == '__main__':
    ttr = TextTestRunner(stream=sys.stdout,
                         verbosity=9,
                         failfast=True)
    try:
        utmain(testRunner=ttr)
    except SystemExit:
        pass
