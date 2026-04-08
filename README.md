# Lean 4 & Mathlib Setup Guide

## Prerequisites

### 1\. VS Code (The Required Engine)

While other editors exist, **VS Code** is currently the only environment that fully supports the **Lean Infoview**.

  * **Install:** [Visual Studio Code](https://code.visualstudio.com/).
  * **Extension:** Search the Marketplace for **"Lean 4"** (by the Lean FRO) and install it.

### 2\. Elan (The Version Manager)

Lean is updated frequently. `elan` ensures your project always uses the correct version of the compiler.

  * **Linux/macOS:** `curl https://elan.lean-lang.org/elan-init.sh -sSf | sh`
  * **Windows:** Follow the instructions at [elan.lean-lang.org](https://www.google.com/search?q=https://elan.lean-lang.org/).

## Project Initialization

To start a research project with **Mathlib** (the essential library for complex analysis and linear algebra), do not just create a `.lean` file. Create a **Lake** project:

```bash
# 1. Create the project folder
lake +leanprover-community/mathlib4:lean-toolchain new project math
cd project

# 2. Initialize Mathlib dependencies
lake update
```

## The "No-Melt" Build Strategy

Mathlib is massive. Compiling it from scratch can take hours and peg your CPU at 100%. **Always use the cache.**

### The Recovery Sequence

If you see a build count increasing indefinitely (e.g., `[408/8000+]`), stop the process with `Ctrl+C` and run:

```bash
# Force-download pre-compiled binaries from the cloud
lake exe cache get!

# Verify the build (should now take seconds)
lake build
```

> **Note:** The `!` is critical if you have half-finished build artifacts. It forces Lean to overwrite them with the clean, cached versions.

## Navigating the Workspace

### The Infoview (The "Truth" Panel)

The Infoview is your most important tool. It appears on the right side of VS Code.

  * **Tactic State:** Shows the current goal (`⊢`).
  * **Expected Type:** Shows what Lean is looking for.
  * **Messages:** Displays errors (like "Unknown identifier").

### Key Tactics

| Tactic | Use Case |
| :--- | :--- |
| `rw` | Rewriting a goal using a known theorem. |
| `aesop` | Automated proof search (the "white flag" for complex logic). |

## Troubleshooting

  * **"Unknown identifier":** Check your imports at the top of the file.
  * **"Server crashed":** Use the Command Palette (`Ctrl+Shift+P`) and type `Lean 4: Restart Server`.
  * **"No goals to be solved":** This usually means there is an error *above* your current line that is preventing Lean from reaching your proof. Check for red squiggles\!