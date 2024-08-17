import PyPDF2
import pyttsx3

with open("pdf-to-audio.pdf", "rb") as path:
    pdfReader = PyPDF2.PdfReader(path)
    audio = pyttsx3.init()

    for pageNum in range(len(pdfReader.pages)):
        page = pdfReader.pages[pageNum]
        text = page.extract_text()

        if text:
            print(f"\n Reading page { pageNum + 1 } ...\n")
            print(text)

            audio.say(text)
            audio.runAndWait()

    audio.stop()
