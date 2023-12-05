from tkinter import *
from translate import Translator
from tkinter import messagebox


class LanguageTranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Language Translator")
        master.geometry("700x360+100+200")
        master.config(bg="black")

        # Initialize variables with self
        self.lang1 = StringVar() 
        self.lang2 = StringVar()
        self.var1 = StringVar()
        self.var2 = StringVar()

        self.lang1.set("Choose")
        self.lang2.set("Choose")

        self.create_widgets()

    def create_widgets(self):
        Label(self.master, text="TRANSLATOR", font="comicsans 20 bold", fg="white", bg="gray20").pack(side=TOP, fill=X)

        f1 = Frame(self.master, bg="gray10", padx=45, pady=15, relief=RAISED)
        f1.pack(side=TOP, pady=10)

        Label(f1, text="Select input Language", fg="white", font="arial 14 bold", bg="gray22", pady=5).grid(row=1,
                                                                                                            column=0,
                                                                                                            pady=5)
        Label(f1, text="Select output Language", fg="white", font="arial 14 bold", bg="gray22", pady=5).grid(row=1,
                                                                                                             column=2,
                                                                                                             pady=5)

        choices = ["English", "German", "French", "Hindi"]
        menu1 = OptionMenu(f1, self.lang1, *choices)
        menu1.grid(row=2, column=0, padx=5, pady=5, ipadx=4, ipady=4)

        menu2 = OptionMenu(f1, self.lang2, *choices)
        menu2.grid(row=2, column=2, padx=5, pady=5, ipadx=4, ipady=4)

        Label(f1, text="Enter Text", font="arial 14 bold", fg="white", bg="gray").grid(row=3, column=0, padx=8, pady=8,
                                                                                       ipadx=10, ipady=10)
        Label(f1, text="Output Text", font="arial 14 bold", fg="white", bg="gray").grid(row=3, column=2, padx=8, pady=8,
                                                                                        ipadx=10, ipady=10)

        Entry(f1, textvariable=self.var1, font="comicsans 15 bold").grid(row=4, column=0, ipadx=12, ipady=12, padx=4,
                                                                         pady=4)
        Entry(f1, textvariable=self.var2, font="comicsans 15 bold").grid(row=4, column=2, ipadx=12, ipady=12, padx=4,
                                                                         pady=4)

        Button(f1, text="Submit", fg="white", bg="gray22", command=self.convert).grid(row=5, column=1, padx=5, pady=5,
                                                                                      ipadx=10, ipady=10)

    def convert(self):
        try:
            v1 = self.lang1.get()
            v2 = self.lang2.get()
            v3 = self.var1.get()
            T = Translator(from_lang=v1, to_lang=v2)
            output = T.translate(v3)
            self.var2.set(output)
            messagebox.showinfo("Translation Success", "Text translated successfully!")
        except Exception as e:
            self.var2.set("")
            messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    root = Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()
