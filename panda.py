import pandas as pd
student_data= {
    "StudentID": [100,101,102,103,104],
    "Name": ["Soyam","Sameer","numbchucks","Garjamaan","safe-al"],
    "Age": [20,19,2,202,21],
    "Grade": ["A","A","C","S","D"]
}

student_df = pd.DataFrame(student_data)
print(student_data)
