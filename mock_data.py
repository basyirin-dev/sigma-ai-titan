# mock_data.py

# SCENARIO 1: COMPLEX CALCULUS (Integration)
# Trigger Keyword: "integrate", "area", "calculus"
MOCK_CALCULUS = r"""
### Analysis
The user has provided an image of a definite integral problem involving a trigonometric function.
**Objective:** Evaluate the integral $\int_{0}^{\pi/2} x \cos(x) \, dx$.

### First Principles
To solve an integral of the form $\int u dv$, we must utilize **Integration by Parts**:
$$ \int u \, dv = uv - \int v \, du $$

We follow the **LIATE** rule to select $u$:
1.  **L**ogarithmic
2.  **I**nverse Trigonometric
3.  **A**lgebraic ($x$) -> **Select this as u**
4.  **T**rigonometric ($\cos x$) -> **Select this as dv**
5.  **E**xponential

### Step-by-Step Solution

**Step 1: Define variables**
Let $u = x \Rightarrow du = dx$
Let $dv = \cos(x) \, dx \Rightarrow v = \sin(x)$

**Step 2: Apply the formula**
$$ \int_{0}^{\pi/2} x \cos(x) \, dx = [x \sin(x)]_{0}^{\pi/2} - \int_{0}^{\pi/2} \sin(x) \, dx $$

**Step 3: Evaluate the first part**
$$ [x \sin(x)]_{0}^{\pi/2} = (\frac{\pi}{2} \sin(\frac{\pi}{2})) - (0 \cdot \sin(0)) $$
$$ = \frac{\pi}{2}(1) - 0 = \frac{\pi}{2} $$

**Step 4: Evaluate the remaining integral**
$$ \int \sin(x) \, dx = -\cos(x) $$
$$ - [-\cos(x)]_{0}^{\pi/2} = [\cos(x)]_{0}^{\pi/2} $$
$$ = \cos(\frac{\pi}{2}) - \cos(0) $$
$$ = 0 - 1 = -1 $$

**Step 5: Combine results**
$$ \text{Total} = \frac{\pi}{2} - (-(-1)) \quad \text{(Wait, check signs)} $$
Correction:
$$ \text{Total} = [x \sin x] - [-\cos x] = [x \sin x + \cos x]_{0}^{\pi/2} $$
$$ = (\frac{\pi}{2}(1) + 0) - (0 + 1) $$
$$ = \frac{\pi}{2} - 1 $$

### Final Answer
$$ \boxed{\frac{\pi}{2} - 1} $$
"""

# SCENARIO 2: GEOMETRY (Solution of Triangles)
# Trigger Keyword: "triangle", "angle", "geometry"
MOCK_GEOMETRY = r"""
### Analysis
The image displays a triangle $ABC$ with the following knowns:
- Side $AC = 12 \text{ cm}$
- Side $BC = 15 \text{ cm}$
- Angle $\angle ABC = 40^\circ$
- **Goal:** Find the length of side $AB$ and Area of triangle.

### First Principles
Since we have two sides and a non-included angle (SSA case), we must first use the **Sine Rule** to find angle $A$, then the **Cosine Rule** or subtraction to find the last side.

### Calculation

**1. Find Angle A using Sine Rule:**
$$ \frac{\sin A}{a} = \frac{\sin B}{b} $$
$$ \frac{\sin A}{15} = \frac{\sin 40^\circ}{12} $$
$$ \sin A = \frac{15 \sin 40^\circ}{12} $$
$$ \sin A \approx \frac{15(0.6428)}{12} \approx 0.8035 $$
$$ A = \sin^{-1}(0.8035) \approx 53.47^\circ $$

*Constraint Check:* Since $a > b$, angle $A$ could be obtuse (Ambiguous Case). However, assuming acute for this context.

**2. Find Angle C:**
$$ C = 180^\circ - 40^\circ - 53.47^\circ = 86.53^\circ $$

**3. Find Side c (AB) using Sine Rule:**
$$ \frac{c}{\sin 86.53^\circ} = \frac{12}{\sin 40^\circ} $$
$$ c = \frac{12 \sin 86.53^\circ}{\sin 40^\circ} \approx \frac{12(0.998)}{0.6428} $$
$$ c \approx 18.63 \text{ cm} $$

### Final Answer
$$ \boxed{AB = 18.63 \text{ cm}} $$
"""

# SCENARIO 3: FALLBACK / ERROR
MOCK_GENERAL = r"""
### System Analysis
**Status:** Simulation Mode Active.
**Input:** Image detected.
**Context:** General Query.

I am currently in **DEV_MODE**. I cannot process this specific image dynamically yet, but I can confirm the pipeline is operational.

To test specific modules, include these keywords in your prompt:
- **"integrate"** : Triggers Calculus Module.
- **"triangle"** : Triggers Geometry Module.

### LaTeX Test
Here is a test of the rendering engine:
$$ f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n $$
"""

# --- UX: THOUGHT CHAINS ---
THOUGHT_CHAINS = {
    "calculus": [
        "Identifying integration bounds...",
        "Applying LIATE rule for Integration by Parts...",
        "Computing definite integral...",
        "Verifying singularity points...",
        "Formatting LaTeX output...",
    ],
    "geometry": [
        "Vectorizing diagram...",
        "Detecting geometric primitives (Triangle, Circle)...",
        "Applying Sine/Cosine Rules...",
        "Checking for ambiguous cases...",
        "Rendering final proof...",
    ],
    "general": [
        "Ingesting multimodal data...",
        "Tokenizing input stream...",
        "Accessing Knowledge Graph...",
        "Synthesizing response...",
    ],
}

# --- COGNITIVE PATHWAYS ---
# These simulate the internal steps of the Gemini Thinking Model.
THOUGHT_CHAINS = {
    "geometry": [
        "Scanning diagram topology...",
        "Identifying geometric primitives (Triangle, Angle, Arc)...",
        "Extracting labels (A, B, C, theta)...",
        "Checking for ambiguous cases (Sine Rule)...",
        "Formulating proof strategy...",
        "rendering_latex",
    ],
    "algebra": [
        "Parsing symbolic expressions...",
        "Identifying variables ($x$, $y$)...",
        "Checking for simultaneous constraints...",
        "Applying substitution method...",
        "Verifying roots...",
        "rendering_latex",
    ],
    "graph": [
        "Vectorizing curve data...",
        "Identifying critical points (min/max)...",
        "Calculating gradient function $dy/dx$...",
        "Determining nature of stationary points...",
        "rendering_latex",
    ],
    "pdf_test": [
        "Ingesting PDF stream...",
        "OCR Extraction (Page 1)...",
        "Segmenting Question 1...",
        "Contextualizing MRSM syllabus...",
        "rendering_latex",
    ],
    "general": [
        "Analyzing multimodal input...",
        "Tokenizing context...",
        "Accessing Knowledge Graph...",
        "Synthesizing response...",
        "rendering_latex",
    ],
    # Add this to THOUGHT_CHAINS dictionary
    "failure_test": [
        "Establishing secure handshake...",
        "Uploading payload to neural engine...",
        "WARNING: High latency detected...",
        "Attempting packet reroute...",
        "CONNECTION_TIMED_OUT",
    ],
}
