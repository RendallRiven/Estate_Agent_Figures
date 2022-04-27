def open_file():
    browse_text.set('Loading....')
    file = askopenfile(parent=root, mode='rb', title='Choose file', filetype=[('xlsx file', '*.xlsx')])
    if file:
       df =  pd.read_excel(file)

       text_box = tk.Text(root, height=10, width=100, padx=15, pady=15)
       text_box.insert(1.0, df)
       text_box.grid(columnspan=5, row=4)
       browse_text.set('Browse')

browse_text = tk.StringVar()
browse_button = tk.Button(root, textvariable=browse_text, command=lambda:open_file())
browse_text.set("Browse")
browse_button.grid(column=2, row=3)