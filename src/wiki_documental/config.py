from __future__ import annotations

from pathlib import Path
import yaml


BASE_DIR = Path(__file__).resolve().parents[2]


def load_config() -> dict:
    """Load configuration from config.yaml."""
    cfg_file = BASE_DIR / "config.yaml"
    with cfg_file.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}

    paths_cfg = cfg.get("paths", {})
    if "wiki" not in paths_cfg:
        paths_cfg["wiki"] = "wiki"
    for key, rel in paths_cfg.items():
        paths_cfg[key] = BASE_DIR / rel
    cfg["paths"] = paths_cfg
    return cfg


def init_paths() -> None:
    """Create directory structure defined in ``cfg``."""
    for p in cfg.get("paths", {}).values():
        Path(p).mkdir(parents=True, exist_ok=True)


cfg = load_config()
