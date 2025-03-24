
# Project Structure

In Sync Game project is organized as follows:

```
InSync/
├── Docs/                    # Documentation
│   ├── install.md           # Installation instructions
│   └── structure.md         # Project Structure
│
├── games/                   # Game implementations
│   ├── plaingame.py         # Plain text version
│   └── styledgame.py        # Styled version with colors
│
│
├── utils/                   # Utility functions
│   └── utilities.py         # Shared utility functions
│
│
├── LICENSE                  # License
├── main.py                  # Entry point
└── README.md                # Brief overview
```

## Key Files:

- **main.py**: Entry point for the application allowing choice between styled and plain versions
- **games/plaingame.py**: Implementation with plain text (no styling)
- **games/styledgame.py**: Implementation with styled text (colors and effects)
- **utils/utilities.py**: Shared utility functions used by both implementations