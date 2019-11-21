import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class CvsTa:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x700")
        self.root.title("Placement Details for {}".format('IEM'))

        df = pd.read_csv('./databases/placement.csv')

        a_df = df[df['BRANCH']=='ISE']


        total_app = a_df['TOTAL_APPEARED']
        total_placed = a_df['TOTAL_PLACED']

        x = a_df['COMPANY_NAME']

        df1 = a_df[['COMPANY_NAME','TOTAL_APPEARED','TOTAL_PLACED']] \
            .groupby('COMPANY_NAME').sum()
        
        figure1 = plt.Figure(figsize=(7,7), dpi=70)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self.root)

        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Companies Visited Vs. Total Students Appeared and Placed')

        self.root.mainloop()

a = CvsTa()