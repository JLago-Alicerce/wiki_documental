from __future__ import annotations

from pathlib import Path
import yaml


ROOT = Path(__file__).resolve().parents[2]


def load_config() -> dict:
    """Load configuration from config.yaml and ensure directories exist."""
    cfg_file = ROOT / "config.yaml"
    with cfg_file.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}

    paths_cfg = cfg.get("paths", {})
    if "wiki" not in paths_cfg:
        paths_cfg["wiki"] = "wiki"
    for key, rel in paths_cfg.items():
        p = ROOT / rel
        p.mkdir(parents=True, exist_ok=True)
        paths_cfg[key] = p
    cfg["paths"] = paths_cfg
    return cfg


cfg = load_config()
