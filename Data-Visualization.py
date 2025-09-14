import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/rice_yield_prediction.csv", delimiter=',')

sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(
    data=data, 
    x="Rice Variety", 
    y="Yield (kg/ha)", 
    hue="Rice Variety",  
    errorbar=None,  
    estimator=lambda x: x.mean(), 
    palette="viridis",
    dodge=False 
)
plt.title("Yield Comparison Across Rice Varieties", fontsize=14)
plt.xticks(rotation=45, fontsize=10)
plt.ylabel("Yield (kg/ha)", fontsize=12)
plt.xlabel("Rice Variety", fontsize=12)
plt.legend([], [], frameon=False)  
plt.tight_layout()
# Yield comparison plot
plt.savefig("images/yield_comparison.png")
plt.close()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/rice_yield_prediction.csv", delimiter=',')

numeric_columns = data.select_dtypes(include=["float64", "int64"]).columns
correlation_matrix = data[numeric_columns].corr()

plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlation Heatmap", fontsize=14)
plt.tight_layout()
# Correlation heatmap
plt.savefig("images/correlation_heatmap.png")
plt.close()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "rice_yield_predicton.csv"  # Replace with your actual file path
data = pd.read_csv(file_path, delimiter="\t")  # Adjust the delimiter if necessary

# Pie Chart: Proportion of Soil Types
soil_counts = data["Soil Type"].value_counts()  # Replace with the actual column name
plt.figure(figsize=(6,6))  # Reduced size
plt.pie(
    soil_counts, 
    labels=soil_counts.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=sns.color_palette("pastel")
)
plt.title("Proportion of Soil Types", fontsize=12)  # Reduced font size
plt.tight_layout()
plt.savefig("images/soil_type_distribution.png")
plt.close()





import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("data/rice_yield_prediction.csv", delimiter=',')

# Pie Chart: Protein Deficiency Severity Distribution
severity_counts = data["Protein Deficiency Severity"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(severity_counts, labels=severity_counts.index, autopct="%1.1f%%", startangle=140, colors=sns.color_palette("Set2"))
plt.title("Protein Deficiency Severity Distribution", fontsize=14)
plt.tight_layout()
# Yield comparison plot
plt.savefig("images/Protein_Deficiency_Severity_Distribution.png")
plt.close()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("rdata/rice_yield_prediction.csv", delimiter=',')

# Bar Chart: Yield by Region
plt.figure(figsize=(10, 6))
sns.barplot(
    data=data, 
    x="Region",  # Replace with the actual column name
    y="Yield (kg/ha)", 
    hue="Region",  # Set hue to the same categorical variable to avoid warning
    errorbar=None, 
    estimator="mean", 
    palette="coolwarm", 
    legend=False  # To remove the legend if not needed
)
plt.title("Average Yield by Region", fontsize=14)
plt.xlabel("Region", fontsize=12)
plt.ylabel("Yield (kg/ha)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/average_yield_region.png")
plt.close()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("data/rice_yield_prediction.csv", delimiter=',')

# Scatter Plot: Rainfall vs Yield
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="Rainfall (mm/month)", y="Yield (kg/ha)", hue="Protein Deficiency Severity", palette="Set2")
plt.title("Rainfall vs Yield with Protein Deficiency Severity", fontsize=14)
plt.xlabel("Rainfall (mm/month)", fontsize=12)
plt.ylabel("Yield (kg/ha)", fontsize=12)
plt.legend(title="Deficiency Severity")
plt.tight_layout()
# Rainfall vs Yield plot
plt.savefig("images/rainfall_vs_yield.png")
plt.close()



