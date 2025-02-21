import streamlit as st
import pandas as pd
import os #for reading files
from io import BytesIO  # convert files into binary and keep them temporarily in memory for converting files

#setup page
st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("Data Sweeper ")
st.write("Transform your files between CSV and excel with dta cleaninng and Visualization")

uploadedFiles = st.file_uploader("upload your files (CSV or excel)", type=["xlsx",'csv'], accept_multiple_files=True)


#ye kam thora smjh nhi aya niche wala

if uploadedFiles:
    for file in uploadedFiles:
        fileExtension = os.path.splitext(file.name)[-1].lower()

        if fileExtension == '.csv':
            data_frame = pd.read_csv(file)
        elif fileExtension == '.xlsx':
            data_frame = pd.read_excel(file)
        else:
            st.error(f"unsupported file type: {fileExtension}")
            continue


        #display file Info
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Type:** {fileExtension}")
        st.write(f"**File Size:** {file.size/1024}")

        # preview data
        st.write("preview the head of the Data Frame")
        st.dataframe(data_frame.head())  #data_frame.head returns first 5 rows of data

        st.subheader("Data cleaning Options")
        if st.checkbox(f"Cleaning Data for {file.name}"):
            col1,col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    data_frame.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed!")

            with col2:
                    if st.button(f"Fill Missing Values for {file.name}"): # on;y work for numeric coloumn
                        numeric_cols = data_frame.select_dtypes(include=['number']).columns
                        data_frame[numeric_cols] = data_frame[numeric_cols].fillna(data_frame[numeric_cols].mean())
                        st.write('Missing Values Filled!')


        #choose individual columns

        st.subheader("Select Columns to convert")
        columns = st.multiselect(f"Choose Column for {file.name}",data_frame.columns,default=data_frame.columns)
        data_frame =  data_frame[columns]


        #Create some visualization
        st.subheader("Data Visualization")

        if st.checkbox(f"Show Visualization for {file.name}"):
            st.bar_chart(data_frame.select_dtypes(include="number").iloc[:,:2])


        #file conversion CSV --> xlxs
        st.subheader("Conversion Options")

        conversionType = st.radio(f"Convert {file.name} to:",["Excel","CSV"],key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversionType == "Excel":
                data_frame.to_excel(buffer,index=False)
                fileName = file.name.replace(fileExtension,".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            elif conversionType == "CSV":
                data_frame.to_csv(buffer,index=False)
                fileName = file.name.replace(fileExtension,".csv")
                mime_type = "text/csv"

            buffer.seek(0)

            #download Button
            st.download_button(f"Download {file.name} as {conversionType}",
            data=buffer,
            file_name=fileName,
            mime=mime_type
            )


st.success("All files done")