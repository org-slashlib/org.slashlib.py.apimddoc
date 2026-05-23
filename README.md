[Bottom](#license) [AI](AI.md) [CHANGELOG](CHANGELOG.md) [LICENSE](LICENSE.md)

# org.slashlib.py.apimddoc

`org.slashlib.py.apimddoc` is a robust, template-driven documentation engine designed to transform Python source code into structured Markdown documentation. It leverages Jinja2 for flexible rendering and provides a plugin-based architecture to customize how your API structure is processed and exported[cite: 2].

[![PyPI version](https://img.shields.io/pypi/v/org.slashlib.py.apimddoc.svg?color=blue)](https://pypi.org/project/org.slashlib.py.apimddoc/) [![PyPI-Test version](https://img.shields.io/badge/pypitest-latest-blue)](https://test.pypi.org/project/org.slashlib.py.apimddoc/) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

## 1. Overview & Architecture

The project is built around a centralized `ProjectRegistry` that decouples code analysis from documentation output.
- **Core Models**:
  Uses specialized models (`ModuleModel`, `ClassModel`, `FunctionModel`, etc.) to represent the API structure.
- **Rendering Pipeline**:
  Employs a `MarkdownRenderer` singleton that uses `Jinja2` templates to generate documentation.
- **RenderingPolicy**:
  A flexible policy layer that dictates which entities to render and how to map them to filenames, supporting custom plugin overrides.

---

## 2. Prerequisites

*   **Python 3.10+**
*   `pip` for package management.
*   An existing project structure you wish to document.

---

## 3. Installation

### Production / Standard
```bash
pip install org.slashlib.py.apimddoc
```

---

## 4. Configuration

The library provides built-in templates, which are used by default if no custom directory is specified.

### CLI Usage
For most use cases, you can simply run the CLI tool:

```bash
python -m org.slashlib.py.apimddoc --input ./src --output ./docs
```

### Programmatic Usage

If you need to initialize the renderer manually within your own scripts:

```python
from org.slashlib.py.apimddoc.renderer.markdown import MarkdownRenderer

# Initializes with default built-in templates
MarkdownRenderer.setup()

# Or override with a custom path
MarkdownRenderer.setup(template_dir="path/to/your/templates")
```

---

## 5. Usage Example

```python
from org.slashlib.py.apimddoc.renderer.markdown import MarkdownRenderer

# Configure the renderer
MarkdownRenderer.setup(template_dir="docs/templates")

# Trigger the rendering process
MarkdownRenderer.render(output_dir="docs/api")
```

---

## 6. RenderingPolicy - Plugin

You can customize the rendering behavior by implementing a custom policy and registering it via entry points.

```toml
# Configuration for custom RenderingPolicy plugins
# This allows other packages to override the default documentation policy
[project.entry-points."apimddoc.renderer.policy"]
custom_policy = "your_package.path.to.module:YourCustomRenderingPolicy"
```

## 7. Development & Testing

### Testing with Pytest

```bash
pytest tests/
```

### Logging
The adapter logs under the namespace `org.slashlib.py.apimddoc`.
Configure your logging to see detailed initialization and rendering progress.

---

## 8. Documentation & Obsidian

The project root is fully prepared as an **Obsidian Vault**.
You can open the directory directly in Obsidian to navigate the documentation structure and project notes.

---

## License

Distributed under the **MIT License**. See `LICENSE.md` for more information.

---
© 2026 org.slashlib