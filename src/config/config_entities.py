import os, sys

from dataclasses import dataclass
from src.constants.training_pipeline import (
    ARTIFACT_DIR, TRAIN_FILE_NAME, TEST_FILE_NAME, RAW_FILE_NAME, 
    PREPROCESSING_OBJECT_FILE_NAME,
    MODEL_FILE_NAME)

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join(ARTIFACT_DIR, TRAIN_FILE_NAME)
    test_data_path: str = os.path.join(ARTIFACT_DIR, TEST_FILE_NAME)
    raw_data_path: str = os.path.join(ARTIFACT_DIR, RAW_FILE_NAME)
    
@dataclass
class DataTransformationConfig:
    preprocessor_object_file_path: str = os.path.join(ARTIFACT_DIR, PREPROCESSING_OBJECT_FILE_NAME)
    # transformed_train_path: str = os.path.join(ARTIFACT_DIR, "transformed", TRAIN_FILE_NAME)
    # transformed_test_path: str = os.path.join(ARTIFACT_DIR, "transformed", TEST_FILE_NAME)
    
@dataclass
class ModelTrainerConfig: 
    trained_model_file_path: str = os.path.join(ARTIFACT_DIR, MODEL_FILE_NAME)