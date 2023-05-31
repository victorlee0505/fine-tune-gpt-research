import pandas as pd
import json

# Load your dataset
df = pd.read_csv('sunshine_difference.csv')

# Function to generate prompt and completion pair
def generate_prompt_completion1(row):
    # Prompt
    prompt = generate_prompt1(row)

    # Completion
    completion = generate_completion1(row)

    return {"prompt": prompt, "completion": completion}

def generate_prompt_completion2(row):
    # Prompt
    prompt = f"Generate a summary for the following Sunshine List data:\n\
    Sector: {row['Sector']}\n\
    Last Name: {row['Last Name']}\n\
    First Name: {row['First Name']}\n\
    Salary in 2022: {row['Salary_2022']}\n\
    Benefits in 2022: {row['Benefits_2022']}\n\
    Employer: {row['Employer']}\n\
    Job Title in 2022: {row['Job Title_2022']}\n\
    Salary in 2020: {row['Salary_2020']}\n\
    Benefits in 2020: {row['Benefits_2020']}\n\
    Job Title in 2020: {row['Job Title_2020']}\n\
    Salary Difference between 2022 and 2020: {row['Salary Difference']}\n\
    Job Change: {row['Job Change']}"

    # Completion
    completion = f"{row['First Name']} {row['Last Name']}, working in the {row['Sector']} sector at {row['Employer']}, held the position of {row['Job Title_2022']} in 2022. Their salary was {row['Salary_2022']}, with additional benefits valued at {row['Benefits_2022']}. This marked an increase in salary from {row['Salary_2020']} in 2020, when they held the position of {row['Job Title_2020']}. The difference in salary was approximately {row['Salary Difference']}."
    
    if row['Job Change'] == 'Yes':
        completion += f" The change in job title from {row['Job Title_2020']} in 2020 to {row['Job Title_2022']} in 2022 could be a contributing factor to the salary difference."
    else:
        completion += " There was no change in job title during this period."

    return {"prompt": prompt, "completion": completion}


# Employee data
def generate_prompt1(row):
    prompt = f"Tell me about {row['First Name']} {row['Last Name']}'s employment details",
    return prompt

def generate_completion1(row):
    completion = f"{row['First Name']} {row['Last Name']}, working in the {row['Sector']} sector at {row['Employer']}, held the position of {row['Job Title_2022']} in 2022. Their salary was {row['Salary_2022']}, with additional benefits valued at {row['Benefits_2022']}. This marked an increase in salary from {row['Salary_2020']} in 2020, when they held the position of {row['Job Title_2020']}. The difference in salary was approximately {row['Salary Difference']}."
    
    if row['Job Change'] == 'Yes':
        completion += f" The change in job title from {row['Job Title_2020']} in 2020 to {row['Job Title_2022']} in 2022 could be a contributing factor to the salary difference."
    else:
        completion += " There was no change in job title during this period."
    return completion

def generate_prompt2(row):
    prompt = f"Tell me about :\n\
    Sector: {row['Sector']}\n\
    Last Name: {row['Last Name']}\n\
    First Name: {row['First Name']}\n\
    Salary in 2022: {row['Salary_2022']}\n\
    Benefits in 2022: {row['Benefits_2022']}\n\
    Employer: {row['Employer']}\n\
    Job Title in 2022: {row['Job Title_2022']}\n\
    Salary in 2020: {row['Salary_2020']}\n\
    Benefits in 2020: {row['Benefits_2020']}\n\
    Job Title in 2020: {row['Job Title_2020']}\n\
    Salary Difference between 2022 and 2020: {row['Salary Difference']}\n\
    Job Change: {row['Job Change']}"
    return prompt

# Apply the function to each row
prompt_completion_pairs = df.apply(generate_prompt_completion1, axis=1).tolist()

# Write the JSONL file
with open('sunshine_prompt_completion.json', 'w') as f:
    json.dump(prompt_completion_pairs, f)
