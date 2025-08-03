from __future__ import annotations

from pathlib import Path

import yaml

from config_models import SystemConfig


def test_system_config_round_trip(tmp_path: Path) -> None:
    with open("system_config.yaml", "r", encoding="utf-8") as fh:
        original_data = yaml.safe_load(fh)
    original_config = SystemConfig.from_dict(original_data)

    dumped_data = original_config.model_dump()

    temp_file = tmp_path / "temp_config.yaml"
    with temp_file.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(dumped_data, fh, sort_keys=False)

    with temp_file.open("r", encoding="utf-8") as fh:
        reloaded_data = yaml.safe_load(fh)
    reloaded_config = SystemConfig.from_dict(reloaded_data)

    # ensure no extra fields were introduced
    assert reloaded_data == dumped_data
    # ensure the reloaded object matches the original
    assert reloaded_config == original_config
