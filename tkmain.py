class TkMain:
    def start_programm(self):
        import pandacalculate as pc
        import tkinter as tk
        window = tk.Tk()
        window.title('Datenanalyse für LF8')
        # window size
        window.geometry("800x500")
        # headline
        label_headline = tk.Label(window, text='Datenanalyse einiger Datenquellen für LF8')

        # button kreisdiagramm_nach_genre

        button_k_n_g_ps4 = tk.Button(window, text='Absatz PS4 nach Genre',
                                     command=lambda: pc.PandaCalculate.piechart_genre("PS4_GamesSales.csv"))
        button_k_n_g_xbox = tk.Button(window, text='Absatz Xbox nach Genre',
                                      command=lambda: pc.PandaCalculate.piechart_genre("XboxOne_GameSales.csv"))
        button_k_n_g_rest = tk.Button(window, text='Absatz Restliche Geräte nach Genre',
                                      command=lambda: pc.PandaCalculate.piechart_genre(
                                          "Video_Games_Sales_as_at_22_Dec_2016.csv"))

        # Programm beenden
        exit_button = tk.Button(window, text='Beenden', command=lambda: [window.quit()])

        # anordnung der Elemente
        label_headline.grid(row=0, column=1)
        button_k_n_g_ps4.grid(row=1, column=0, pady=10, padx=10)
        button_k_n_g_xbox.grid(row=1, column=1, pady=10, padx=10)
        button_k_n_g_rest.grid(row=1, column=2, pady=10, padx=10)
        exit_button.grid(row=10, column=1, pady=10)

        window.mainloop()