#import dataiku
#from dataiku import pandasutils as pdu
#import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

def plot_wafermaps(dataframe, num_columns, defect_types, img_folder):
    for defect in defect_types:
        fig, ax = plt.subplots(nrows = 1, ncols = num_columns, figsize=(20, 20))
        ax = ax.ravel(order='C')
        df_defect = dataframe.loc[dataframe['defect_type'] == defect].reset_index()
        for i in range(num_columns):
            PATH = df_defect['path'][i]
            with img_folder.get_download_stream(PATH) as f:
                data = f.read()
            img = Image.open(BytesIO(data))
            img = img.resize((128,128))
            ax[i].imshow(img)
            ax[i].set_title(defect, fontsize=20)
#             ax[i].set_xlabel(PATH.split('/')[-1], fontsize=15)
            ax[i].set_xticks([])
            ax[i].set_yticks([])
            for x, a in enumerate(ax):
                a.spines["top"].set_visible(False)
                a.spines["right"].set_visible(False)
                a.spines["left"].set_visible(False)
                a.spines["bottom"].set_visible(False)
#         plt.tight_layout()
        plt.show()
