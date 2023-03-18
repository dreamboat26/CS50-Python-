def main():
    filename = input("Enter a filename: ")
    print(get_media_type(filename))

def get_media_type(filename):
    suffix = filename.strip().split(".")[-1].lower()
    if suffix == "gif":
        return "image/gif"
    elif suffix in ["jpg", "jpeg"]:
        return "image/jpeg"
    elif suffix == "png":
        return "image/png"
    elif suffix == "pdf":
        return "application/pdf"
    elif suffix == "txt":
        return "text/plain"
    elif suffix == "zip":
        return "application/zip"
    else:
        return "application/octet-stream"

if __name__ == "__main__":
    main()