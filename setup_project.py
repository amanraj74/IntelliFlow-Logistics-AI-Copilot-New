import os
import json

def create_project_structure():
    """Create complete project structure for hackathon"""
    
    project_name = "IntelliFlow-Logistics-AI-Copilot"
    
    # Define project structure
    structure = {
        project_name: {
            "backend": {
                "pathway": {},
                "api": {
                    "routers": {}
                },
                "agents": {},
                "models": {},
                "utils": {}
            },
            "frontend": {
                "components": {},
                "pages": {},
                "static": {
                    "css": {},
                    "js": {},
                    "images": {}
                }
            },
            "data": {
                "streams": {},
                "processed": {},
                "raw": {},
                "sample": {}
            },
            "config": {},
            "docker": {},
            "tests": {
                "unit": {},
                "integration": {}
            },
            "docs": {},
            "logs": {},
            "notebooks": {},
            "scripts": {}
        }
    }
    
    # Create directories recursively
    def create_dirs(path, structure):
        for folder, subfolders in structure.items():
            current_path = os.path.join(path, folder)
            os.makedirs(current_path, exist_ok=True)
            print(f"✅ Created: {current_path}")
            
            if subfolders:
                create_dirs(current_path, subfolders)
    
    # Create the structure
    create_dirs(".", structure)
    
    # Create essential files
    create_essential_files(project_name)
    
    print(f"\n🎉 Project '{project_name}' created successfully!")
    print(f"📁 Total directories created: {count_dirs(structure)}")

def create_essential_files(project_name):
    """Create essential project files"""
    
    files_content = {
        f"{project_name}/README.md": readme_content(),
        f"{project_name}/requirements.txt": requirements_content(),
        f"{project_name}/Dockerfile": dockerfile_content(),
        f"{project_name}/docker-compose.yml": docker_compose_content(),
        f"{project_name}/.gitignore": gitignore_content(),
        f"{project_name}/backend/__init__.py": "",
        f"{project_name}/backend/api/__init__.py": "",
        f"{project_name}/backend/api/main.py": fastapi_main_content(),
        f"{project_name}/backend/pathway/__init__.py": "",
        f"{project_name}/backend/pathway/pipeline.py": pathway_pipeline_content(),
        f"{project_name}/frontend/dashboard.py": streamlit_dashboard_content(),
        f"{project_name}/config/settings.py": settings_content(),
    }
    
    for file_path, content in files_content.items():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"📄 Created file: {file_path}")

def count_dirs(structure, count=0):
    """Count total directories"""
    for folder, subfolders in structure.items():
        count += 1
        if subfolders:
            count = count_dirs(subfolders, count)
    return count

# File content templates
def readme_content():
    return '''# IntelliFlow Logistics AI Copilot 🚛✨

## Pathway X IIT Ropar Gen AI Hackathon 2025

### 🚀 Quick Start

To get started, follow the instructions in this README.

'''
