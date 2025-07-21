import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Create DataFrame
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8],
    'Marks': [100, 200, 300, 400, 500, 600, 700, 800]
}
df = pd.DataFrame(data)

# Step 2: Calculate Percentage
df['Percentage'] = df['Marks'] / 8

# Step 3: Assign Grade based on Percentage
def assign_grade(p):
    if p >= 800:
        return 'A+'
    elif p >= 700:
        return 'A'   
    elif p >= 600:
        return 'B'     
    elif p >= 500:
        return 'C'    
    elif p >= 400:
        return 'D'    
    elif p >= 300:
        return 'E'    
    elif p >= 200:
        return 'F' 
    else:
        return 'Fail'

df['Grade'] = df['Percentage'].apply(assign_grade)

# Step 4: Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x='Hours', y='Marks', data=df, palette='Blues_d')
plt.title('Hours of Reading vs Marks')  
plt.xlabel('Hours')
plt.ylabel('Marks')
plt.tight_layout()
plt.show()