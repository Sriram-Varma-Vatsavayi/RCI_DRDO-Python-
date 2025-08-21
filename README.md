# RCI DRDO Python Project

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DRDO](https://img.shields.io/badge/Organization-DRDO-green.svg)](https://www.drdo.gov.in/)
[![RCI](https://img.shields.io/badge/Lab-Research%20Centre%20Imarat-orange.svg)](https://www.drdo.gov.in/drdo/labs-and-establishments/research-centre-imarat-rci)

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API/Configuration](#apiconfiguration)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact/Support](#contactsupport)

## Project Description

This Python project is developed in association with Research Centre Imarat (RCI), a premier laboratory under Dr APJ Abdul Kalam Missile Complex, Defence Research and Development Organisation (DRDO). RCI specializes in R&D for avionics systems, control engineering, inertial navigation, imaging infrared seekers, RF seekers & systems, onboard computers, and mission software for defense and aerospace applications.

This repository contains Python implementations and tools that support research and development activities in areas such as:
- Control Engineering algorithms
- Navigation and guidance systems
- Signal processing for defense applications
- Simulation and modeling tools
- Data analysis for aerospace systems

## Features

- **Advanced Control Systems**: Implementation of control engineering algorithms for missile and aerospace applications
- **Navigation Algorithms**: Python implementations of inertial navigation and guidance systems
- **Signal Processing**: Tools for processing RF and infrared signals
- **Simulation Framework**: Modeling and simulation capabilities for defense systems
- **Data Analysis**: Statistical analysis and visualization tools for research data
- **Modular Design**: Well-structured, reusable code modules for different applications
- **Documentation**: Comprehensive documentation for all major components
- **Testing Suite**: Unit tests and integration tests for reliability

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sriram-Varma-Vatsavayi/RCI_DRDO-Python-.git
   cd RCI_DRDO-Python-
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python -m pytest tests/
   ```

## Usage

### Basic Usage Examples

#### Control Systems
```python
from rci_drdo.control import PIDController, StateSpaceModel

# Create a PID controller
pid = PIDController(kp=1.0, ki=0.1, kd=0.01)

# Process control signal
output = pid.compute(setpoint=100, measured_value=95, dt=0.01)
print(f"Control output: {output}")
```

#### Navigation Systems
```python
from rci_drdo.navigation import INSNavigator, GPSProcessor

# Initialize inertial navigation system
ins = INSNavigator(initial_position=[0, 0, 0], initial_velocity=[0, 0, 0])

# Update with sensor data
ins.update(acceleration=[0.1, 0.05, -9.81], angular_velocity=[0, 0, 0.1], dt=0.01)
position = ins.get_position()
print(f"Current position: {position}")
```

#### Signal Processing
```python
from rci_drdo.signal_processing import RFProcessor, IRProcessor

# Process RF signals
rf_processor = RFProcessor(sampling_rate=1000, frequency_range=(100, 500))
filtered_signal = rf_processor.bandpass_filter(raw_signal)
```

### Command Line Interface

The project includes command-line tools for common operations:

```bash
# Run simulation
python -m rci_drdo.simulate --config config/simulation.yaml

# Process data files
python -m rci_drdo.process --input data/input.csv --output results/

# Generate reports
python -m rci_drdo.report --type performance --data results/
```

## API/Configuration

### Configuration Files

The project uses YAML configuration files for different modules:

**config/control.yaml**
```yaml
control_systems:
  pid:
    kp: 1.0
    ki: 0.1
    kd: 0.01
    max_output: 100
    min_output: -100
  
  state_space:
    A: [[1, 1], [0, 1]]
    B: [[0], [1]]
    C: [[1, 0]]
    D: [[0]]
```

**config/navigation.yaml**
```yaml
navigation:
  ins:
    initial_position: [0, 0, 0]
    initial_velocity: [0, 0, 0]
    gravity: [0, 0, -9.81]
  
  gps:
    update_rate: 1.0
    accuracy: 3.0
```

### API Reference

#### Core Classes

- `PIDController`: Proportional-Integral-Derivative controller implementation
- `StateSpaceModel`: State-space representation for linear systems
- `INSNavigator`: Inertial Navigation System implementation
- `RFProcessor`: Radio Frequency signal processing utilities
- `IRProcessor`: Infrared signal processing tools

#### Key Methods

- `simulate()`: Run system simulations
- `analyze()`: Perform data analysis
- `visualize()`: Generate plots and visualizations
- `export_results()`: Export results in various formats

## Dependencies

### Core Dependencies

- **numpy** (>=1.19.0): Numerical computing
- **scipy** (>=1.6.0): Scientific computing
- **matplotlib** (>=3.3.0): Plotting and visualization
- **pandas** (>=1.2.0): Data manipulation and analysis
- **scikit-learn** (>=0.24.0): Machine learning tools
- **opencv-python** (>=4.5.0): Computer vision (for image processing)
- **h5py** (>=3.1.0): HDF5 data format support

### Optional Dependencies

- **jupyter** (>=1.0.0): Interactive development
- **plotly** (>=5.0.0): Interactive visualizations
- **pytest** (>=6.2.0): Testing framework
- **sphinx** (>=4.0.0): Documentation generation

### Installation Command

```bash
pip install numpy scipy matplotlib pandas scikit-learn opencv-python h5py
```

For development dependencies:
```bash
pip install -e .[dev]
```

## Contributing

We welcome contributions from researchers, engineers, and developers interested in defense and aerospace applications. Please follow these guidelines:

### Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Install development dependencies**
   ```bash
   pip install -e .[dev]
   ```

### Code Standards

- Follow PEP 8 Python style guidelines
- Include docstrings for all functions and classes
- Add unit tests for new functionality
- Ensure code coverage is maintained above 80%
- Use type hints where appropriate

### Testing

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=rci_drdo --cov-report=html

# Run specific test file
python -m pytest tests/test_control.py
```

### Documentation

- Update documentation for any API changes
- Include examples in docstrings
- Update README.md if needed

### Submission Process

1. **Commit your changes** with clear, descriptive messages
2. **Push to your fork**
3. **Create a Pull Request** with:
   - Clear description of changes
   - Reference to any related issues
   - Test results and coverage reports

### Code Review Process

All contributions will be reviewed by the core team. Please ensure:
- Code follows project standards
- Tests pass and coverage is maintained
- Documentation is updated
- No security vulnerabilities are introduced

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-Party Licenses

This project uses several open-source libraries. Please refer to their respective licenses:
- NumPy: BSD License
- SciPy: BSD License
- Matplotlib: PSF License
- Pandas: BSD License

## Contact/Support

### Primary Contact

**Sriram Varma Vatsavayi**
- GitHub: [@Sriram-Varma-Vatsavayi](https://github.com/Sriram-Varma-Vatsavayi)
- Project Repository: [RCI_DRDO-Python-](https://github.com/Sriram-Varma-Vatsavayi/RCI_DRDO-Python-)

### Institutional Contact

**Research Centre Imarat (RCI)**
- Address: Vigyanakancha, Hyderabad-500069, India
- Phone: 040-24306000
- Fax: 040-24306002
- Email: director[dot]rci[at]gov[dot]in
- Website: [https://www.drdo.gov.in/drdo/labs-and-establishments/research-centre-imarat-rci](https://www.drdo.gov.in/drdo/labs-and-establishments/research-centre-imarat-rci)

### Getting Help

1. **Issues and Bug Reports**: Please use GitHub Issues for bug reports and feature requests
2. **Documentation**: Check the [docs/](docs/) directory for detailed documentation
3. **Examples**: See [examples/](examples/) directory for usage examples
4. **FAQ**: Common questions are answered in [FAQ.md](FAQ.md)

### Contributing Questions

For questions about contributing, please:
1. Check existing issues and pull requests
2. Review the contributing guidelines above
3. Contact the maintainers if you need clarification

---

**Note**: This project is associated with defense research and development. Please ensure compliance with applicable regulations and security guidelines when contributing or using this code.

**Disclaimer**: This is an educational and research project. The code and algorithms provided are for learning and research purposes. Users are responsible for ensuring compliance with all applicable laws and regulations in their jurisdiction.
