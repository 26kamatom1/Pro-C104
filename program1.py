import csv
with open("SOCR-HeightWeight.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
newdata=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    newdata.append(float(n_num))
import statistics as st
mean=st.mean(newdata)
print(mean)
median=st.median(newdata)
print(median)
mode=st.mode(newdata)
print(mode)