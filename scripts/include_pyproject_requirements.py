"""Include requirements.txt in pyproject.toml project.dependencies array."""
import toml

PROJECT_METADATA_FILE_NAME = "pyproject.toml"
REQUIREMENTS_FILE_NAME = "requirements.txt"


with open(REQUIREMENTS_FILE_NAME, "r", encoding="utf8") as f:
    requirements = [
        line.strip() for line in f if line.strip() and not line.lstrip().startswith("#")
    ]
print(
    f"From {REQUIREMENTS_FILE_NAME} read requirements:"
    f"\n{requirements[:10]}...\n{len(requirements)} total"
)

with open(PROJECT_METADATA_FILE_NAME, "r", encoding="utf8") as f:
    pyproject_data = toml.load(f)

print(
    f"Updating project {pyproject_data['project']['name']} project.dependencies array"
    f" in {PROJECT_METADATA_FILE_NAME}"
)

pyproject_data["project"]["dependencies"] = requirements

with open(PROJECT_METADATA_FILE_NAME, "w", encoding="utf8") as f:
    toml.dump(pyproject_data, f)
