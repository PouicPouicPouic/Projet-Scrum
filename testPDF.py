import pdftotext

print("coucou")

# Load your PDF
with open("Das_Martins.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# How many pages?
print(len(pdf))

# Iterate over all the pages
for page in pdf:
    print(page)

# Read some individual pages
print(pdf[0])
print(pdf[1])

# Read all the text into one string
print("\n\n".join(pdf))
