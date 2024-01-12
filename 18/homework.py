from docx import Document

def create_word_file(text):
    doc = Document()
    doc.add_paragraph(text)

    file_name = input("Enter the name for Word file: ")
    file_name = f"{file_name}.docx"

    doc.save(file_name)

if __name__ == "__main__":
    user_input = input("Enter the text for the Word file: ")
    create_word_file(user_input)
