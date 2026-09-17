# Three-Phase Phasor Animation

A small Python visualization of a balanced three-phase system.

The project shows three equal-magnitude voltage phasors rotating at the same angular velocity with a 120° phase shift between phases A, B, and C. Corresponding current phasors are shown with a load-dependent phase shift.

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
- Resistive, inductive, and capacitive load modes
- Configurable voltage, current, and frequency
- Three-phase active, reactive, and apparent power calculation
- Power factor calculation
- Real/imaginary axes
- Reference circle
- Current rotation angle

### Electrical parameters

The main electrical parameters are configured directly in `main.py`:

```python
VOLTAGE = 400.0
CURRENT = 10.0
FREQUENCY = 50.0
LOAD_TYPE = "inductive"
```

`VOLTAGE` is the RMS line-to-line voltage and `CURRENT` is the RMS line current.

Available load types:

- `resistive` — current in phase with voltage
- `inductive` — current lags voltage by 90°
- `capacitive` — current leads voltage by 90°

For the selected load, the application calculates:

- Active power `P`
- Reactive power `Q`
- Apparent power `S`
- Power factor `cosφ`

The values are displayed together with the animation.

This is intentionally a small engineering visualization project focused on connecting electrical engineering concepts with Python.
