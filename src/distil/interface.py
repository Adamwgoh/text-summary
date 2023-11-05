import gradio as gr

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain import OpenAI, PromptTemplate

# def upload_file(files):
#     file_paths = [file.name for file in files]
#     return file_paths


def loaddocs(files):
    file_paths = [file.name for file in files]
    docs = []
    for file in file_paths:
        loader = PyPDFLoader(file)
        doc = loader.load_and_split()
        chain = load_summarize_chain(llm, chain_type="map_reduce")
        summary = chain.run(doc)
        docs.append(summary)

    return docs

def setup_interface():

    input_pdf = gr.inputs.File(type="file", label="Upload PDF")
    input_text = gr.inputs.Textbox(lines=5, label="Enter Text")
    input_type = gr.inputs.Radio(choices=["Upload PDF", "Enter Text"], label="Input Type")
    output_summary = gr.outputs.Textbox(label="Output Summary")
    # Change to Gradio blcoks later
    demo = gr.Interface(
        fn=loaddocs, 
        inputs=[input_type, input_pdf, input_text], 
        outputs=[output_summary], 
        title="Summarizer", 
        description="Summarize your documents with a click of a button.")
    return demo

if __name__ == "__main__":
    demo = setup_interface()
    demo.launch()