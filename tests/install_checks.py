"""Mechanics checks run by tools/clean_install.py inside a fresh environment."""
from math import log, sqrt

SAMPLE = ("A rocket with an exhaust velocity of 3000 m/s has an initial mass of 1000 kg and a final mass of 400 kg after the burn. "
          "What is its change in velocity?", 3000 * log(2.5))
LATENCY = ["A 2 kg mass on a spring with a spring constant of 50 N/m has a damping coefficient of 4 kg/s. What is the damped angular frequency?",
           "What is the escape speed from a planet of mass 5.972e24 kg and radius 6.371e6 m?",
           "A uniform rod of mass 3 kg and length 2 m rotates about one end. What is its moment of inertia?"]


def checks(P) -> dict:
    return {
        "twenty_five_certified_relations": len(P.formulas()) == 25,
        "damped_frequency": abs(P.ask(LATENCY[0]).value - sqrt(24)) < 1e-9,
        "inverse_solve": abs(P.ask("A damped oscillator has mass 1 kg, spring constant 10 N/m and a damped angular frequency of "
                                   "3 rad/s. What is the damping coefficient?").value - 2.0) < 1e-6,
        "unit_conversion": abs(P.ask("A uniform rod of mass 3 kg and length 200 cm rotates about one end. What is its moment of "
                                     "inertia?").value - 4.0) < 1e-9,
        "refuses_missing": not P.ask("What is the escape speed from a planet of mass 5.972e24 kg?").solved,
        "refuses_unknown": not P.ask("A body has a mass of 2 kg. What is its moment of inertia?").solved,
        "signed_collision": abs(P.ask("Two carts collide elastically: the first mass is 1 kg and the velocity of the first is 4 m/s; "
                                      "the second mass is 3 kg and the velocity of the second is -2 m/s. Find the final velocity "
                                      "of the first.").value - (-5.0)) < 1e-9,
    }
