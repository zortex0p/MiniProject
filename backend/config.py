"""
Configuration settings for Legal Document Simplifier backend
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration"""
    JSON_SORT_KEYS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # API Keys
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    
    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///legal_documents.db')
    
    # CORS
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:3000,http://localhost:8000').split(',')
    
    # Models
    LEGAL_BERT_MODEL = os.getenv('LEGAL_BERT_MODEL', 'nlpaueb/legal-bert-base-uncased')
    LLM_MODEL = os.getenv('LLM_MODEL', 'claude-3-5-sonnet-20241022')
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    DATABASE_URL = 'sqlite:///:memory:'


def get_config():
    """Get configuration based on environment"""
    env = os.getenv('FLASK_ENV', 'development')
    
    if env == 'production':
        return ProductionConfig()
    elif env == 'testing':
        return TestingConfig()
    else:
        return DevelopmentConfig()
