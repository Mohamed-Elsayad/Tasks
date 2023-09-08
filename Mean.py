import streamlit as st

def calculate_mean(grades):
    total = sum(grades)
    mean = total / len(grades)
    return mean

def main():
    st.title("Student Grade Calculator")
    st.write("Enter the grades for each subject and calculate the mean.")

    num_subjects = st.number_input("Number of Subjects", min_value=1, value=1, step=1)

    grades = []

    for subject in range(num_subjects):
        grade = st.number_input(f"Enter the grade for Subject {subject+1}", min_value=0.0, max_value=100.0, step=0.1)
        grades.append(grade)

    if st.button("Calculate Mean"):
        mean = calculate_mean(grades)
        st.success(f"The mean grade is {mean:.2f}")

if __name__ == "__main__":
    main()
