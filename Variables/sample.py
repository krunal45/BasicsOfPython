import csv

def csv_to_dict(filename):
    """
    Reads a CSV file and stores its contents in a dictionary.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        dict: A dictionary where keys are the header row and values are lists of corresponding data, or None if an error occurs.
    """
    data_dict = {}
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile: #added encoding for better compatibility
            reader = csv.reader(filename)
            header = next(reader)  # Read the header row

            # Initialize lists for each column in the dictionary
            for col in header:
                data_dict[col] = []

            # Iterate through the rows and populate the dictionary
            for row in reader:
                for i, value in enumerate(row):
                    data_dict[header[i]].append(value)

        return data_dict

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e: #Catch any other potential errors.
        print(f"An error occurred: {e}")
        return None

# Example usage:
filename = 'Average Response Time Comparison.csv'  # Replace with your CSV file name
result_dict = csv_to_dict(filename)

if result_dict:
    # Print the dictionary (optional)
    for key, value in result_dict.items():
        print(f"{key}: {value}")

    # You can now access the data using the dictionary
    # For example, to get the values from the 'column_name' column:
    # column_values = result_dict.get('column_name')
    # if column_values:
    #     print(column_values)