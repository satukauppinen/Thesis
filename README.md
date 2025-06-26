# Threat Modeling-as-Code: Evaluation and Extension Thesis

This repository supports my bachelor's thesis project on evaluating and extending threat modeling-as-code tools for identifying security and ethical risks in Infrastructure-as-Code (IaC) environments.

---

##  Project Goals

- Compare current tools for threat modeling / static analysis of IaC
- Evaluate effectiveness in detecting ethical and deceptive patterns
- Extend one tool with support for dark-pattern detection or enhanced privacy modeling
- Document findings through annotated examples, rule prototypes, and final thesis

---

##  Repository Structure

| Folder | Contents |
|--------|----------|
| `/iac-examples/` | Infrastructure-as-Code samples (good vs. deceptive) |
| `/tool-tests/` | Outputs and logs from Checkov, ThreatSpec, etc. |
| `/custom-rules/` | Extensions (e.g., Checkov custom rules or Rego policies) |
| `/docs/` | Evaluation criteria, diagrams, and writeups |
| `/appendix-code/` | Clean versions of configs used in the final thesis |
| `/notebooks/` or `/scripts/` | Optional analysis scripts or notebooks |

---

##  Tools in Use

- [Terraform](https://www.terraform.io/)
- [Checkov](https://www.checkov.io/)
- [ThreatSpec](https://threatspec.org/)
- [OPA / Rego](https://www.openpolicyagent.org/)
- Custom rules / threat annotations

---

##  Experiments

Each tool is tested against a controlled set of IaC examples. Ethical/deceptive configurations are evaluated for detection and reporting accuracy.

---

