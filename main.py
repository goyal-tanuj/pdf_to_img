from pdf2image import convert_from_path

old_pdf = convert_from_path("pdfimage/nature.pdf",  # forward slashes in the PDF path
                            poppler_path="C:/Users/tanuj/Desktop/pdfimage/Release-24.08.0-0/poppler-24.08.0/Library/bin")  # forward slashes for poppler path

for i in range(len(old_pdf)):
    old_pdf[i].save("new" + str(i) + ".jpg", "JPEG")