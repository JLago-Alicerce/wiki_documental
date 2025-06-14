import subprocess
import shutil
import pytest

from wiki.utils.system import ensure_pandoc


def test_missing_pandoc(monkeypatch):
    monkeypatch.setattr(shutil, "which", lambda name: None)
    with pytest.raises(RuntimeError):
        ensure_pandoc()


def test_pandoc_execution_failure(monkeypatch):
    class DummyResult:
        def __init__(self):
            self.returncode = 1
    monkeypatch.setattr(subprocess, "run", lambda *args, **kwargs: DummyResult())
    monkeypatch.setattr(shutil, "which", lambda name: "/usr/bin/pandoc")
    with pytest.raises(RuntimeError):
        ensure_pandoc()
