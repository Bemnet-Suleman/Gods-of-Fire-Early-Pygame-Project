# Fire Fighting — Architecture

This document explains the project's structure and how the main systems fit together so new readers can understand the game quickly.

## Purpose
Provide a concise, high-level overview to help contributors or reviewers understand game flow, major modules, assets, and data formats.

## High-level components
- `Fire_Fighting.py` — program entry. Initializes the window, loads resources, contains the main loop and top-level scene management.
- `flame.py` — fire entity and flame animation logic; handles fire behaviour and effects.
- `smoke_effect.py` — particle system for smoke; controls emitters, lifetime, and rendering for smoke visuals.
- `mim.py` — utility and UI/menu helpers (inspect for specific functions).
- `Images/` — sprite and UI assets organized by subfolders (Background, Enemy, Abilities, etc.).
- `Sounds/` — audio assets (music, SFX).
- `Game_map*.txt`, `map1.txt` — level data files. Plain-text maps used to spawn tiles, enemies and objects.

## File / module responsibilities
- Initialization: `Fire_Fighting.py` loads image/sound assets and parses map files.
- Update loop: each frame, input is processed, entities are updated, effects advance, collisions resolved, and the frame is rendered.
- Effects: `flame.py` and `smoke_effect.py` encapsulate visual effect creation and per-frame updates.

## Typical game loop (simplified)
1. Initialize display, clock, and load assets.
2. Parse selected map file and instantiate level objects (tiles, enemies, player, hazards).
3. Enter main loop:
   - Poll input/events
   - Update game state (player, enemies, effects)
   - Resolve collisions and game rules
   - Draw background, tiles, entities, UI, and effects
   - Tick clock and cap FPS
4. Clean up and exit.

## Maps and data
- Map files are plain text; parser reads rows/columns to determine tile types and spawn coordinates for entities. Check `Fire_Fighting.py` for exact parsing rules.

## Assets and paths
- Asset paths are relative to the project root. Keep `Images/` and `Sounds/` alongside `Fire_Fighting.py` to avoid path issues.

## Controls and gameplay (high-level)
- Player input, movement, and interactions are handled each frame by `Fire_Fighting.py` or helper modules — look for event loops and key handling in the main file.

## Packaging notes
- For distribution, bundle the following at minimum: `Fire_Fighting.py`, `Images/`, `Sounds/`, and map files.
- Use PyInstaller with data bundling to create executables; ensure non-Python assets are included.

## Where to look for more detail
- Read `Fire_Fighting.py` to see exact initialization, map parsing and game logic.
- Inspect `flame.py` and `smoke_effect.py` for visual effect implementation.

## Final-release note
This is the final published version; use a new branch when making future fixes or feature work.
