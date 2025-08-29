import os

def save_pdf(uploaded_file, data_folder="data"):
    os.makedirs(data_folder, exist_ok=True)
    file_path = os.path.join(data_folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path
