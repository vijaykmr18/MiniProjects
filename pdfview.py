import pyttsx3
import PyPDF2
import time

# Open the PDF file
book = open('demo.pdf', 'rb')

# Use PdfReader
pdf_reader = PyPDF2.PdfReader(book)

# Initialize pyttsx3
play = pyttsx3.init()
print('Playing Audio Book')

# Loop through pages
for num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[num]
    data = page.extract_text()

    if data:
        play.say(data)
        play.runAndWait()

    # Provide a way for the user to stop the audiobook (e.g., after each page)
    stop = input("Press 'q' to stop or hit Enter to continue to next page: ")
    if stop.lower() == 'q':
        print("Stopping audiobook.")
        break

book.close()
