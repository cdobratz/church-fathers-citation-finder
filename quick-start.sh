#!/bin/bash
mkdir -p backend

# Church Fathers MVP - Quick Start Script
# This script automates the initial setup

set -e  # Exit on any error

echo "=========================================="
echo "Church Fathers MVP - Quick Setup"
echo "=========================================="
echo ""

# Check if we're in the right directory
if [ ! -f "README.md" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

echo "📦 Setting up Backend..."
echo ""

# Backend setup
cd backend

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate venv
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt --quiet

# Copy env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cp .env.example .env
fi

echo "✅ Backend setup complete!"
echo ""

# Frontend setup
cd ../frontend

echo "📦 Setting up Frontend..."
echo ""

# Install npm dependencies
echo "Installing Node dependencies (this may take a minute)..."
npm install --silent

# Copy env file if it doesn't exist
if [ ! -f ".env.local" ]; then
    echo "Creating .env.local file..."
    cp .env.example .env.local
fi

echo "✅ Frontend setup complete!"
echo ""

cd ..

echo "=========================================="
echo "✨ Setup Complete! ✨"
echo "=========================================="
echo ""
echo "To start the application:"
echo ""
echo "1. Terminal 1 (Backend):"
echo "   cd backend"
echo "   source venv/bin/activate"
echo "   python run.py"
echo ""
echo "2. Terminal 2 (Frontend):"
echo "   cd frontend"
echo "   npm run dev"
echo ""
echo "3. Open http://localhost:3000"
echo ""
echo "Happy coding! 🚀"
echo ""
