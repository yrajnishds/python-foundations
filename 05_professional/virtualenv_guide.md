# 🐍 Virtual Environment Guide

A virtual environment isolates project dependencies.

Why use it?
- Avoid dependency conflicts
- Keep system Python clean
- Professional development standard

Create virtual environment:

python -m venv venv

Activate (Linux/Mac):

source venv/bin/activate

Activate (Windows):

venv\Scripts\activate

Deactivate:

deactivate

Install package:

pip install package_name

Generate requirements file:

pip freeze > requirements.txt

Install from requirements:

pip install -r requirements.txt