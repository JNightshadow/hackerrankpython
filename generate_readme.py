import os

readme_header = """# 📘 HackerRank Python preparation

Solutions to selected problems in Python Hackerrank which I struggled or didn't know how to do.. Added explanations or some notes for later reference which would help to understand the code.

I would like to refine the little notes I've made after getting more practice!

## 🗂 Available Topics
"""

def get_md_files(root="."):
    topic_links = {}
    for dirpath, _, filenames in os.walk(root):
        md_files = [f for f in filenames if f.endswith(".md") and f != "README.md"]
        if md_files:
            folder = os.path.basename(dirpath)
            # Pick the first Markdown file found in this folder
            first_md_file = sorted(md_files)[0]
            relative_path = os.path.join(dirpath, first_md_file).replace("\\", "/")
            topic_links[folder] = relative_path
    return topic_links

def generate_links(topic_links):
    return "\n".join(
        f"- [{folder}](./{path})" for folder, path in sorted(topic_links.items())
    )

if __name__ == "__main__":
    topics = get_md_files()
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_header + "\n" + generate_links(topics))
