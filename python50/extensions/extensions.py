extension = input("File name: " ).strip().lower().rpartition(".")[2]
if extension in ["gif", "jpg", "jpeg", "png"]:
    print(f"image/jpeg") if extension == "jpg" else print(f"image/{extension}")
elif extension == "pdf" or extension == "zip":
    print(f"application/{extension}")
elif extension == "txt":
    print(f"text/plain")
else:
    print("application/octet-stream")