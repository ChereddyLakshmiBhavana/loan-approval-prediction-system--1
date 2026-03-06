# Project Structure Documentation

## Directory Organization

```
deep-learning-loan-prediction-system/
├── data/
│   ├── raw/                    # Original, immutable raw data
│   └── processed/              # Cleaned and processed data ready for ML
├── notebooks/                  # Jupyter notebooks for EDA and experiments
├── src/
│   ├── __init__.py
│   ├── api/                    # REST API server
│   │   ├── __init__.py
│   │   └── app.py              # Main Flask application
│   ├── data/                   # Data loading and preprocessing
│   │   ├── __init__.py
│   │   ├── loader.py           # Data loading utilities
│   │   └── preprocessing.py    # Data cleaning and transformation
│   ├── models/                 # Model architectures and training
│   │   ├── __init__.py
│   │   ├── model.py            # Model architectures
│   │   └── train.py            # Training scripts
│   └── utils/                  # Helper functions
│       ├── __init__.py
│       ├── logger.py           # Logging setup
│       └── helpers.py          # Utility functions
├── tests/                      # Unit and integration tests
│   ├── test_data.py
│   └── test_models.py
├── config/
│   └── config.py               # Configuration settings
├── docs/                       # Project documentation
│   ├── PROJECT_STRUCTURE.md    # This file
│   ├── API.md                  # API documentation
│   ├── DATA_DICTIONARY.md      # Data field descriptions
│   └── RESULTS.md              # Results and evaluation
├── models/                     # Trained model files
├── logs/                       # Application logs
├── frontend/                   # Web interface
├── requirements.txt            # Python dependencies
├── setup.py                    # Package installation script
├── .gitignore                  # Git ignore rules
└── README.md                   # Project overview
```

## Key Files

### Configuration
- **config/config.py**: Central configuration for paths, model parameters, hyperparameters

### Data
- **src/data/loader.py**: DataLoader class for file I/O
- **src/data/preprocessing.py**: DataPreprocessor class for cleaning and transformation

### Models
- **src/models/model.py**: LoanApprovalModel (Neural Network), GradientBoostingModel
- **src/models/train.py**: Model training pipeline and scripts

### API
- **src/api/app.py**: Flask REST API with endpoints for predictions

### Utilities
- **src/utils/logger.py**: Logging configuration
- **src/utils/helpers.py**: Helper functions for evaluation and formatting

### Testing
- **tests/test_data.py**: Tests for data loading and preprocessing
- **tests/test_models.py**: Tests for model training and prediction

## Data Flow

1. **Raw Data** → `data/raw/` (immutable original files)
2. **Loading** → DataLoader reads from raw directory
3. **Preprocessing** → DataPreprocessor cleans and transforms
4. **Processed Data** → `data/processed/` (ready for modeling)
5. **Model Training** → src/models/train.py trains the model
6. **Model Artifacts** → `models/` (trained model files saved)
7. **API Server** → src/api/app.py loads model and serves predictions
8. **Predictions** → Output through /predict endpoint

## Development Workflow

1. **EDA**: Use Jupyter notebooks in `notebooks/` for exploration
2. **Preprocessing**: Develop and test preprocessing logic in `src/data/`
3. **Modeling**: Create and train models in `src/models/`
4. **Testing**: Write unit tests in `tests/`
5. **API**: Build API endpoints in `src/api/`
6. **Deployment**: Package with setup.py and deploy

## Configuration Management

All configuration is centralized in `config/config.py`:
- File paths
- Model hyperparameters
- Training settings
- Feature names
- Performance thresholds

## Logging

Application logs are saved to `logs/` directory with:
- File logging for persistence
- Console logging for debugging
- Configurable log levels in config.py

## Model Persistence

Models are saved in `models/` directory:
- Neural Network: `.h5` format (TensorFlow/Keras)
- Gradient Boosting: `.pkl` format (scikit-learn)

## Testing

Run tests with:
```bash
pytest tests/
pytest tests/test_data.py -v
pytest tests/test_models.py -v
```

## Best Practices

1. Keep data immutable in `data/raw/`
2. Save all transformations results in `data/processed/`
3. Use configuration file for all settings
4. Write tests for all functionality
5. Document all notebook experiments
6. Version control models and results
7. Use logging instead of print statements
8. Follow PEP 8 code style guidelines
