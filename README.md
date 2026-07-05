# Fire Fighting — Final Release

This repository contains the final release of a small 2D game project (last version — no further development planned).

## Summary
- A lightweight Python game using the project files in this repository.
- Entry point: `Fire_Fighting.py` (run from project root).

## Requirements
- Python 3.8+ recommended
- Install dependencies (likely uses pygame):

```
pip install pygame
```

If the project uses another library, install it the same way.

## Run
From the project root run:

```
python Fire_Fighting.py
```

If your environment requires `python3` instead of `python`, use that command.

## Project layout
- `Fire_Fighting.py` — main game entry
- `flame.py`, `smoke_effect.py` — visual / effect modules
- `mim.py`, `#test.py` — utilities / testing (some may be commented out)
- `Game_map*.txt`, `map1.txt` — level/map data files
- `Images/` — all game sprites and UI assets
- `Sounds/` — audio assets

## Assets
Keep `Images/` and `Sounds/` directories alongside the main script. Do not move or rename asset folders unless you also update the code asset paths.

## Packaging / Distribution
- To distribute, create a zip of the project root including `Images/` and `Sounds/`.
- Optionally use PyInstaller to build a standalone executable:

```
pip install pyinstaller
pyinstaller --onefile Fire_Fighting.py
```

## Notes
- This is the final version. No further changes are planned.
- If you want to re-open development later, include a changelog and incremental commits in a new branch.

## Contact
If you want help packaging or publishing to itch.io / GitHub Releases, I can assist.

## App Build

This README is written for GitHub visitors and players. The `build/` folder at the project root contains the standalone Android app package (APK) for this release.

- Build folder: [build/](build/)
- To use: download the APK from the `build/` folder to an Android phone and install it. The APK is a ready-to-run package; install on your device to play.

