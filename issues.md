\# Static Analysis Issue Table



| Issue | Type | Line(s) | Description | Fix Approach |

|-------|------|---------|-------------|--------------|

| SQL injection risk — Bandit B608, Medium | Security | 10 | Song values were inserted directly into an SQL string. Quotes in input could break the query or change its meaning. | Used SQL placeholders and passed values separately. |

| Unsafe deserialization — Bandit B301, Medium | Security | 33 | Loading untrusted pickle data could execute malicious code. | Replaced pickle.loads with json.loads. |

| Pickle import — Bandit B403, Low | Security | 1 | The program imported pickle for playlist serialization. | Removed pickle and used JSON for saving and loading playlists. |

| Standard random generator — Bandit B311, Low | Security tool finding | 17 | Bandit flagged random.choice because it is unsuitable for security-sensitive randomness. Song selection itself does not require cryptographic randomness. | Used secrets.choice to satisfy the lab requirement to resolve all Bandit findings. |

| Mutable default argument — Pylint W0102 | Bug | 9 | The default playlist list was shared between calls, so separate playlists could accidentally share songs. | Changed the default to None and created a new list inside the function. |

| Bare exception — Pylint W0702 and Flake8 E722 | Error handling | 39 | A bare except could hide unrelated programming errors and intercept interruptions. | Caught sqlite3.Error specifically. |

| Invalid function names — Pylint C0103 | Naming | 9, 15, 28, 32, 36 | Several function names did not follow Python snake\_case conventions. | Renamed the functions and updated their calls. |

| Missing documentation — Pylint C0114 and C0116 | Maintainability | 1, 9, 15, 20, 28, 32, 36, 43 | The module and functions lacked docstrings. | Added a module docstring and function docstrings. |

| Unnecessary else — Pylint R1705 | Code quality | 22–25 | The else block followed an if block that already returned. | Removed else and returned the classification directly. |

| Ambiguous variable — Flake8 E741 | Readability | 47 | The variable name l was difficult to distinguish from the number 1. | Renamed it to loaded\_playlist. |

| Multiple statements on one line — Pylint C0321 and Flake8 E701 | Formatting | 48 | The condition and print statement were written on the same line. | Moved the print statement to an indented line. |

| Long lines — Pylint C0301 and Flake8 E501 | Formatting | 6, 10, 21, 49 | Several statements exceeded the tools' line-length limits. | Split statements across lines using parentheses. |



\## Final Verification



\- The demonstration runs successfully.

\- Pylint score: 10.00/10.

\- Bandit: no issues identified.

\- Flake8: no findings.

\- Original reports are stored in reports/before/.

\- Final reports are stored in reports/after/.

\- Three separate commits record the Bandit, Pylint, and Flake8 fixes.

