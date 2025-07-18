import os

readme_header = """# 📘 My Python Notes

Welcome! This repo contains my Markdown notes for various Python problems, explanations, and concepts.

## 🗂 Available Topics
"""

def get_md_files(root="."):
    md_files = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".md") and filename != "README.md":
                relative_path = os.path.join(dirpath, filename).replace("\\", "/")
                md_files.append(relative_path)
    return sorted(md_files)

def generate_links(md_files):
    return "\n".join(
        f"- [{os.path.splitext(os.path.basename(path))[0].replace('_', ' ').title()}]({path})"
        for path in md_files
    )

if __name__ == "__main__":
    md_files = get_md_files()
    with open("README.md", "w", encoding="utf-8") as readme:
        readme.write(readme_header + "\n\n" + generate_links(md_files))
