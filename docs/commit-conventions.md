# 📝 Commit Message Conventions

This project follows the **Conventional Commits** standard to keep history clean and meaningful.

---

## Prefix Reference

| Prefix | Use it when… | Example |
| --- | --- | --- |
| **`feat:`** | Adding a **new feature** — new function, module, or CLI option. | `feat(utils): add flex_buzz helper` |
| **`fix:`** | **Fixing a bug** — broken logic, incorrect output, failing test. | `fix(cli): handle invalid user input gracefully` |
| **`chore:`** | **Non-functional cleanup** — config, dependencies, formatting, repo hygiene. | `chore: remove __pycache__ and update .gitignore` |
| **`docs:`** | **Updating documentation** — README, docstrings, Sphinx docs. | `docs(README): update repo structure section` |
| **`refactor:`** | **Improving code structure** without changing behavior. | `refactor(utils): simplify histogram function` |
| **`test:`** | **Adding or improving tests** — unit tests, fixtures, mocks. | `test(utils): add edge cases for flex_buzz` |
| **`build:`** | **Build system changes** — CI configs, setup files, Dockerfiles. | `build(ci): add coverage badge to workflow` |
| **`perf:`** | **Performance improvements** — speedups, memory optimizations. | `perf(algos): optimize Dijkstra runtime` |
| **`style:`** | **Code style only** — formatting, whitespace, linting fixes. | `style: run black formatting on all files` |

---

## Commit Message Format

```text
<type>(optional scope): short summary in imperative mood

# Example:
feat(utils): add flex_buzz helper
```
