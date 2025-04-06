import pandas as pd

def main():
    print("📦 Creating a DataFrame from a dictionary:")
    data = {
        "name": ["Alice", "Bob", "Charlie", "Diana"],
        "age": [25, 30, 35, 28],
        "city": ["New York", "Paris", "London", "New York"],
        "salary": [70000, 80000, 120000, 75000]
    }
    df = pd.DataFrame(data)
    print(df)

    print("\n🔍 Selecting a column (Series):")
    print(df["name"])

    print("\n🔍 Filtering rows (people older than 28):")
    filtered_df = df[df["age"] > 28]
    print(filtered_df)

    print("\n➕ Adding a new column (taxed salary):")
    df["taxed_salary"] = df["salary"] * 0.8  # assume 20% tax
    print(df)

    print("\n📊 Grouping by city and calculating average salary:")
    city_group = df.groupby("city")["salary"].mean()
    print(city_group)

    print("\n🪜 Sorting by age (descending):")
    sorted_df = df.sort_values(by="age", ascending=False)
    print(sorted_df)

    print("\n📈 Describe the dataset (summary statistics):")
    print(df.describe())

    print("\n📂 Exporting to CSV (file will be created):")
    df.to_csv("sample_output.csv", index=False)
    print("Data exported to 'sample_output.csv'")

    print("\n📥 Reading data from CSV:")
    read_df = pd.read_csv("sample_output.csv")
    print(read_df)

if __name__ == "__main__":
    main()
