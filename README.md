# Package Sorter

A simple Python utility to dispatch packages into the correct handling stacks based on their volume and mass, according to Thoughtful’s robotic automation factory rules.

## Features

- Determines if a package is **bulky** (volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm).
- Determines if a package is **heavy** (mass ≥ 20 kg).
- Classifies packages into three stacks:
  - **STANDARD**: Neither bulky nor heavy.
  - **SPECIAL**: Either bulky or heavy (but not both).
  - **REJECTED**: Both bulky and heavy.

