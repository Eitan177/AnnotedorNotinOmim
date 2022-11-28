import streamlit as st
import pandas as pd
import numpy as np
import re



texttomatch=st.text_input('text to match',value='')

kk=pd.read_table('mimannot.txt',sep='\t')

if texttomatch != '':

        foundrow=np.where((kk['OmimPresent'].str.contains(texttomatch,case=False,regex=True)) | (kk['OmimAbsent'].str.contains(texttomatch,case=False,regex=True)) | \
                (kk['Phenotype_x'].str.contains(texttomatch,case=False,regex=True)))[0]
        kk=kk.iloc[foundrow]
        st.write('found',len(kk),'rows')
        st.write('the input text that was searched is:')
        st.write(texttomatch)
        st.write(kk)
else:
      st.write(kk)
