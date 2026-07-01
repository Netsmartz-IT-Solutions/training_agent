import os
import zipfile
import json
import re

agent_dir = os.path.dirname(os.path.abspath(__file__))
app_pkg_dir = os.path.join(agent_dir, "appPackage")
output_zip = os.path.join(agent_dir, "agent_package.zip")

print("📦 Compiling agent package...")

with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(app_pkg_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, app_pkg_dir)
            
            if file == "declarativeAgent.json":
                with open(file_path, "r", encoding="utf-8") as f:
                    da_json = json.load(f)
                
                if "instructions" in da_json and isinstance(da_json["instructions"], str):
                    match = re.search(r"\$\[file\('([^']+)'\)\]", da_json["instructions"])
                    if match:
                        filename = match.group(1)
                        target_file_path = os.path.join(root, filename)
                        if os.path.exists(target_file_path):
                            with open(target_file_path, "r", encoding="utf-8") as tf:
                                da_json["instructions"] = tf.read()
                                
                zipf.writestr(arcname, json.dumps(da_json, indent=2))
                
            elif file == "instruction.txt":
                pass 
            else:
                zipf.write(file_path, arcname)

print(f"✅ Successfully compiled into: {output_zip}")
print("You can now upload this .zip file to your Teams Admin Center or Copilot Studio.")
