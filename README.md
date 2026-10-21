# mechanics-ai999x — offline, verified classical mechanics solver with step-by-step answers

[![tests](https://github.com/AI999X/mechanics-ai999x/actions/workflows/ci.yml/badge.svg)](https://github.com/AI999X/mechanics-ai999x/actions/workflows/ci.yml) [![PyPI](https://img.shields.io/pypi/v/mechanics-ai999x)](https://pypi.org/project/mechanics-ai999x/) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow)](https://huggingface.co/AI999X/mechanics-ai999x)

**[Install](https://pypi.org/project/mechanics-ai999x/)** · **[Capability guide](https://huggingface.co/AI999X/mechanics-ai999x/tree/main/docs)** · **[Evaluation](https://huggingface.co/AI999X/mechanics-ai999x/tree/main/evaluation)** · **[AI999X on Hugging Face](https://huggingface.co/AI999X)** · **[Website](https://ai999x.com)** · **[Support: Buy Me a Coffee](https://buymeacoffee.com/ibnuljaiffarabi)**

License: Apache-2.0 · Author: Ibnul Jaif Farabi (creator and engineer) · Organization: AI999X · Version 1.0.1

mechanics-ai999x is an offline, deterministic Python solver that answers classical mechanics questions with verified results from 25 certified capabilities, gives 234 documented answers identically on Windows and Linux, and refuses rather than guesses when an answer cannot be verified.

**mechanics-ai999x** is a compact, deterministic classical mechanics engine for Python. It reads a question in plain English (or a typed call), picks a certified classical mechanics capability, computes the answer exactly, checks it, and returns the result with its steps, units, LaTeX and assumptions — or an honest refusal that says what is missing. It runs fully offline on any CPU, needs no GPU, no API key and no internet, and is built to give **zero wrong answers**: when it is not sure, it refuses instead of guessing.

[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-support%20development-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/ibnuljaiffarabi) ![License](https://img.shields.io/badge/license-Apache--2.0-blue) ![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue) ![Offline](https://img.shields.io/badge/runs-offline%20on%20CPU-green)

## Highlights

- **Verified, not generated.** Every answer is computed by a certified classical mechanics capability and checked (substituted back, dimension-checked or compared with an independent computation) before it is returned.
- **Zero wrong answers by design.** Seven explicit outcomes — SOLVED, NEEDS_INPUT, AMBIGUOUS, INVALID_INPUT, OUT_OF_SCOPE, UNRECOGNIZED_FORMAT, INTERNAL_ERROR — never a silent guess. Every one of its 234 documented answers is reproduced exactly on every tested platform.
- **Plain-English questions and a guaranteed typed interface.** `ask()` reads documented question forms; `solve(capability_id, **inputs)` always solves a supported task with valid inputs.
- **Explains itself.** Steps, formulas in LaTeX, units, assumptions and the model used, ready for notebooks, tutoring apps and homework checkers.
- **Small and portable.** Pure Python (sympy, mpmath); identical answers on Windows and Linux (Python 3.10, 3.11, 3.12, 3.13, 3.14).
- **Coverage:** damped, driven and coupled oscillations, physical and double pendulums, orbits (vis-viva, escape speed, Kepler's third law), moments of inertia, rolling, Atwood machines with a massive pulley, torque-free precession, rotating frames (Foucault pendulum, bead on a hoop), elastic collisions and rockets.

## Model overview

| Property | Value |
|---|---|
| Package | `mechanics-ai999x` 1.0.1 (import `mechanics_ai999x`) |
| Type | Deterministic neuro-symbolic classical mechanics engine (rule-based reading + certified symbolic capabilities) |
| Capabilities | 25 certified relations |
| Knowledge pack | version 0.1.0 |
| Golden answers | 234 documented answers, identical on every tested platform |
| Platforms tested | Windows (Python 3.13), Linux x86-64 (Python 3.10, 3.11, 3.12, 3.13, 3.14) |
| Runtime | CPU only, offline; no GPU, no network, no API key |
| License | Apache-2.0 |
| Creator / engineer | Ibnul Jaif Farabi |
| Organization | AI999X |

## Quickstart

```bash
pip install mechanics-ai999x
```

```python
import mechanics_ai999x as mechanics

mechanics.ask("A 2 kg mass on a spring with a spring constant of 50 N/m has a damping coefficient of 4 kg/s. What is the damped angular frequency?").show()
# -> SOLVED — 4.89898 rad/s  (damped_angular_frequency)
mechanics.ask("What is the escape speed from a planet of mass 5.972e24 kg and radius 6.371e6 m?").show()
# -> SOLVED — 11186 m/s  (escape_speed)
mechanics.ask("A rocket with an exhaust velocity of 3000 m/s has an initial mass of 1000 kg and a final mass of 400 kg after the burn. What is its change in velocity?").show()
# -> SOLVED — 2748.87 m/s  (rocket_delta_v)
mechanics.solve("rocket_delta_v", ve="3000 m/s", m0="1000 kg", mf="400 kg").show()
# -> SOLVED — 2748.87 m/s  (rocket_delta_v)
mechanics.ask("What is the escape speed from a planet of mass 5.972e24 kg?").show()
# -> NEEDS_INPUT — Escape speed applies, but it needs: distance from its center (m). Add it to the question with its unit, or use
mechanics.ask("Who created you?").message
# -> mechanics-ai999x was created and engineered by Ibnul Jaif Farabi at AI999X.
```

Command line: `mechanics-ai999x "<question>"`, `mechanics-ai999x --capabilities`. The outputs above were produced by running this exact code on mechanics-ai999x 1.0.1.

## How every answer is verified

1. **Reading** — the question is turned into typed quantities (value, unit, kind, role) and one asked quantity; every stated number must be used or the question is refused.
2. **Planning** — only certified capabilities may answer; a capability applies only under the conditions the wording states (for example a pendulum, a liquid at rest, boiling).
3. **Computing** — exact symbolic or high-precision numeric evaluation.
4. **Checking** — dimensions, substitution back into the defining equation, and agreement between independent readings; any disagreement becomes a refusal, never a number.

Capabilities are certified before they ship: each must reproduce hand-worked reference cases, reject a deliberately wrong variant (a control), and leave every benchmark answer unchanged.

## Capabilities

25 certified relations. A few of them:

- **Relations:** Acceleration of a body rolling without slipping down an incline; Acceleration of an Atwood machine with a massive pulley; Amplitude-resonance frequency of a driven damped oscillator; Angular frequency of a damped oscillator; Body-frame precession rate of a torque-free symmetric body; Damping ratio; Escape speed; Final velocity of the first body in a one-dimensional elastic collision; Final velocity of the second body in a one-dimensional elastic collision; Higher normal mode of a double pendulum; Higher normal-mode frequency of two coupled oscillators; Lower normal mode of a double pendulum; Moment of inertia of a solid disk about its axis; Moment of inertia of a solid sphere; Moment of inertia of a thin rod about its center; Moment of inertia of a thin rod about one end; Moment of inertia of a thin spherical shell; Off-axis equilibrium of a bead on a rotating hoop; Orbital period from the semi-major axis (Kepler's third law); Orbital speed on an elliptical orbit (vis-viva); Period of a physical pendulum; Precession period of a Foucault pendulum; Quality factor of a damped oscillator; Steady-state amplitude of a driven damped oscillator …

`mechanics_ai999x.templates()` lists every question form `ask()` reads; the capability guide (PDF, every example executed) is included in this repository.

## Out of scope

- Open-ended explanation, essay writing or tutoring dialogue: it is a solver, not a chatbot.
- Questions outside its certified classical mechanics capabilities, and any question whose stated numbers it cannot all use — it refuses with the reason instead.
- High-stakes engineering, medical or legal decisions without independent review.

## Limitations

- It answers what its certified capabilities cover (damped, driven and coupled oscillations, physical and double pendulums, orbits (vis-viva, escape speed, Kepler's third law), moments of inertia, rolling, Atwood machines with a massive pulley, torque-free precession, rotating frames (Foucault pendulum, bead on a hoop), elastic collisions and rockets); anything else is refused with a reason.
- `ask()` reads documented question forms and common phrasings; unusual wording may be refused — use `solve()` for guaranteed results.
- Results are as correct as the certified relations and their stated conditions; a certified relation is a checked model, not a claim about every physical situation.

## Citation

```bibtex
@software{mechanics_ai999x_1_0_1,
  title  = {mechanics-ai999x: an offline, verified classical mechanics solver},
  author = {Farabi, Ibnul Jaif}, organization = {AI999X},
  year   = {2026}, version = {1.0.1},
  url    = {https://huggingface.co/AI999X/mechanics-ai999x}
}
```

## Contact

Questions, bug reports and requests: open a discussion on https://huggingface.co/AI999X/mechanics-ai999x/discussions or visit https://ai999x.com.

## Support the project

mechanics-ai999x is free and open source. If it helps you, you can support further development on [Buy Me a Coffee](https://buymeacoffee.com/ibnuljaiffarabi).

Created and engineered by **Ibnul Jaif Farabi** · **[AI999X](https://huggingface.co/AI999X)** · [ai999x.com](https://ai999x.com)

## Source and releases

This repository holds the installable source of each release, exactly as published on [PyPI](https://pypi.org/project/mechanics-ai999x/) (`pip install .` builds it). Releases are tagged `v<version>`; the wheel is attached to each [GitHub release](https://github.com/AI999X/mechanics-ai999x/releases). The optional ONNX models (formula graphs and, where measured, a decision model) are on [Hugging Face](https://huggingface.co/AI999X/mechanics-ai999x/tree/main/onnx).
