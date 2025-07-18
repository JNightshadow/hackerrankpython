import os

readme_header = """# 📘 My Python Notes

Welcome! This repo contains my Markdown notes for various Python problems, explanations, and concepts.

## 🗂 Available Topics
"""

def get_md_files(directory="."):
    files = []
    for file in sorted(os.listdir(directory)):
        if file.endswith(".md") and file != "README.md":
            files.append(file)
    return files

def generate_links(md_files):
    return "\n".join(f"- [{file[:-3].replace('_', ' ').title()}]({file})" for file in md_files)

if __name__ == "__main__":
    md_files = get_md_files()
    with open("README.md", "w") as readme:
        readme.write(readme_header + "\n\n" + generate_links(md_files))
