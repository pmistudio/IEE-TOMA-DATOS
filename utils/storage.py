
import os, json, datetime, pathlib, yaml

def ensure_project_dir(project_id: str) -> str:
    root = os.path.join(os.getcwd(), "proyectos", project_id)
    os.makedirs(root, exist_ok=True)
    os.makedirs(os.path.join(root, "fotos"), exist_ok=True)
    return root

def save_json(project_id: str, data: dict, name: str="datos.json"):
    path = os.path.join(ensure_project_dir(project_id), name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path

def save_md(project_id: str, markdown: str, name: str="resumen.md"):
    path = os.path.join(ensure_project_dir(project_id), name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(markdown)
    return path

def load_catalog_yaml(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def save_uploaded_file(project_id: str, file, prefix: str="foto"):
    root = ensure_project_dir(project_id)
    fotos = os.path.join(root, "fotos")
    suffix = pathlib.Path(file.name).suffix or ".jpg"
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"{prefix}_{ts}{suffix}"
    out = os.path.join(fotos, fname)
    with open(out, "wb") as f:
        f.write(file.getbuffer())
    return out
