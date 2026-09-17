# Three-Phase Phasor Animation

A small Python visualization of a balanced three-phase system.

The project shows three equal-magnitude voltage phasors rotating at the same angular velocity with a 120° phase shift between phases A, B, and C. Corresponding current phasors can be displayed with a configurable load-dependent phase shift.

## Stack

- Python 3.10+
- NumPy
- Matplotlib

## Run

Install dependencies:

```bash
pip install numpy matplotlib
```

Start the animation:

```bash
python main.py
```

## Current scope

- Three rotating voltage phasors
- 120° phase displacement between phases
- Current phasors for phases A, B, and C
- Configurable resistive, inductive, or capacitive load
- Load-dependent voltage/current phase shift
- Unit voltage amplitude and configurable current amplitude
- Real/imaginary axes
- Reference circle
- Current rotation angle

To change the load type, edit `LOAD_TYPE` in `main.py`:

```python
LOAD_TYPE = "inductive"
```

Available values:

- `resistive` — current in phase with voltage
- `inductive` — current lags voltage by 90°
- `capacitive` — current leads voltage by 90°

This is intentionally a small engineering visualization project focused on connecting electrical engineering concepts with Python.
