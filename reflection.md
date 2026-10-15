\# Reflection on Static Code Analysis



The README refers to four reflection questions, but those questions are not included in the supplied handout. The following four points summarize my experience with this lab.



\## 1. What I learned



I learned that a program can run successfully and still contain security risks, bugs, and formatting problems. The original demonstration worked, but static analysis found unsafe SQL construction, pickle usage, and a shared default playlist.



\## 2. How the tools helped



Pylint helped identify problems with naming, documentation, default arguments, and exception handling. Bandit identified security-related patterns. Flake8 helped improve formatting and readability.



\## 3. The most useful fixes



Parameterized SQL separated input values from the query, and JSON removed the need for unsafe pickle loading. Changing the default playlist from an empty list to None also prevented separate calls from sharing the same list.



\## 4. Verification and limitations



After the fixes, the demonstration still worked, Pylint scored 10.00/10, and Bandit and Flake8 reported no findings. These results improve confidence in the code, but they do not prove that every possible bug is absent. Functional testing is still needed.

