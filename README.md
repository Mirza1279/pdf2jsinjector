Use this tool to Inject a JavaScript file into a PDF file.

To do this you will need an existing PDF file, and a ".js" file or code which contains the commands you would like to run when the document is opened. I use this to create PDFs with some active code in there that I can email to customers, or download through their proxies, to check for the JavaScript being removed or blocked. When you open the produced PDF with the JavaScript injected in Adobe you should see your code execute.

These are different from browser based JavaScript so reading that to achieve anything advanced is recommended.

Example JavaScript
Who doesn't love a simple alert message? I know I do. The following code is all you will need for your hello world alert message:

app.alert("Hello world!");

A little different from just "alert". Your alert method now lives attached to the "app" object. Nothing too crazy.

How to use
Follow the steps below to create your PDF:

Execute the requirements.txt file.
pip install -r requirements.txt

Execute the script
python3 pdf2jsinjector.py

Then it will open a GUI prompt that asks you to point it at a PDF and file.
Select the PDF file you would like to inject in to.

This will create a new file in the same directory as the PDF with "js_injected_" prepended in the name.
To automate the process via the command line the following shows the new 

Enjoy!!! 3:)
