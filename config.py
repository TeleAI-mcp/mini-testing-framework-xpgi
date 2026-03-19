"""Configuration module for the testing framework."""


class Config:
    """Base configuration class."""
    
    def __init__(self):
        self.test_dir = "tests"
        self.verbose = False
