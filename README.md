# Coulomb-Petential-Well
1. Physical Intuition:
  Negative Energy (V<0): This represents a Bound State. The electron is "trapped" inside the nucleus's attraction field and needs energy to escape.

    Ionization Limit (V=0): This is the Free State. When the electron reaches this level, it is no longer bound to the atom.

    The "Well" Shape: As the electron gets closer to the nucleus (x→0), the potential drops sharply toward −∞, showing the intensity of the electrostatic pull at the center.
   
   2. Mathematical Modeling

    Equation: $$V(x)=\frac{-Zq^2}{4\pi\varepsilon|x|}$$
    Where:
    $V(x)$ :Electrostatic potential energy .
    $Z$:Atomic number (number of protons)
    $q$: Elementary charge ($\approx1.602\times 10^{-19} c$).
    $\varepsilon$ : Vacuum permitivity ($\approx 8.854\times 10^{-12} F/m$).
    $|x|$:Distance from the nucleus.​

    Symmetry: Using the absolute value ∣x∣ ensures that the potential is identical on both sides of the nucleus.

    Singularity: The code handles the mathematical singularity at x=0 by splitting the domain to prevent division by zero.
