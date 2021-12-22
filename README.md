# `siunitxext` - IP unit definitions for `siunitx` Latex package

This package includes English (I-P) unit definitions for use in `siunitx`.
I work in the American HVAC industry, and it sadly might be the last industry to move to SI.

# How to use

Based on the documentation for `siunitx`, the most straightforward method
is to copy one of the `.tex` files in this repository and place it in
the Tex tree.
This is usually something like:

- `~/texmf/tex/latex/` for Linux
- `~/Library/texmf/tex/latex/` for MacOS
- `C:\Users\<name>\texmf\tex\latex` for Windows

Then you can input the contents directly by using an `\input` in the preamble.

```tex
% Load useful ’local’ units
\input{siunitx-local-units-v3}
```

Note there are two versions, `siunitx-local-units-v2.tex` and `siunitx-local-units-v3.tex`.
There were some changes to the options going from `siunitx` version 2 to 3.
For now, the versions should be backwards compatible, but you can choose the matching version to be sure things work.

Previously, I only had a `.sty` package in this repository.
I'm going to leave it here, although I don't have plans to put it in CTAN,
as the direct input method should suffice.
You could still put the `.sty` file in the correct location and then call `usepackage` if desired.

```tex
\usepackage{siunitxext}
```

Here are the units that are defined:

 Unit Macro | Tex Output
----|----
\inch, \in | in
\foot, \feet, \ft | ft
\yard, \yd | yd
\mile, \mi | mi
\gallon, \gal | gal
\quart, \qt | qt
\pint, \pt | pt
\fluidOunce, \floz | floz
\cup | cup
\pound, \lb | lb
\ounce, \oz | oz
\ton | t
\grain, \gr | gr
\poundMass, \lbm | lb\textsubscript{m}
\slug | slug
\rankine | R
\fahrenheit, \degF, \dF, \degreeF | \degree{}F
\degreeRankine, \degR, \dR, \degreeR | \degree{}R
\bar | bar
\psi | psi
\psia | psia
\psig | psig
\atmosphere, \atm | atm
\BTU | BTU
\btu | btu
\poundForce, \lbf | lb\textsubscript{f}
\poundDryAir, \lbda | lb\textsubscript{da}
\cfm, \ft3 | cfm
\lbmol | lbmol

