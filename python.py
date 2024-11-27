# Define global variables
projects = {}  # Dictionary to store project details
project_details_saved = False  # Variable to track if project details have been saved
















# Function to display menu
def display_menu():
    print("1. Adding Project Details (APD)   " )
    print()
    print("2. Updating Project Details (UPD)   " )
    print()
    print("3. Deleting Project Details (DPD)   ")
    print()
    print("4. Viewing Project Details (VPD)   ")
    print()
    print("5. Saving Project Details to Text File (SPD)   ")
    print()
    print("6. Random Spotlight Selection & Award given (RSS and AWP)   ")
    print()
    print("7. Visualizing Award-Winning Projects (VAP)   ")
    print()
    print("8. Exiting the Program (EXIT)   ")
    print()


















# Function to add project details
def add_project():
    global project_details_saved
    if project_details_saved:
        print("Project details have already been saved. You cannot add new projects.")
        print()
        return
    
    # Input project details
    while True:
        project_id = input("Enter Project ID (numeric only & must be a 3-digit number): ")
        if project_id.isdigit():  # Check if input consists only of digits
            project_id = int(project_id)  # Convert to integer
            if 0 < project_id <= 999:
                break
            else:
                print("Project ID must be a 3-digit number.")
                print()
        else:
            print("Invalid input. Please enter a numeric value.")
            print()

    project_name = input("Enter Project Name: ")
    category = input("Enter Category: ")
    team_members = input("Enter Team Members (separated by comma): ").split(",")
    description = input("Enter Brief Description: ")
    country = input("Enter Country: ")

    # Store project details
    # Convert project IDs to strings when adding projects
    projects[str(project_id)] = {
        "Project Name": project_name,
        "Category": category,
        "Team Members": team_members,
        "Description": description,
        "Country": country
        }




# Function to add sample data
def add_sample_data():
    global projects
    sample_data = [
        {
            "Project ID": "001",
            "Project Name": "Social Media App",
            "Category": "Software Development",
            "Team Members": ["John Doe", "Jane Smith", "Alice Johnson"],
            "Description": "Developing a social media application for sharing photos and messages.",
            "Country": "USA"
        },
                {
            "Project ID": "002",
            "Project Name": "Social Media App",
            "Category": "Software Development",
            "Team Members": ["John Doe", "Jane Smith", "Alice Johnson"],
            "Description": "Developing a social media application for sharing photos and messages.",
            "Country": "USA"
        },
        {
            "Project ID": "003",
            "Project Name": "Data Science - www ",
            "Category": "Artificial Intelligence",
            "Team Members": ["David Brown", "Emily Wilson", "Michael Lee"],
            "Description": "Building an online platform for buying and selling various products.",
            "Country": "Canada"
        },
        {
            "Project ID": "004",
            "Project Name": "Software Development - AAA",
            "Category": "Software Development",
            "Team Members": ["John Doe", "Jane Smith", "Alice Johnson"],
            "Description": "Developing a social media application for sharing photos and messages.",
            "Country": "USA"
        },
        {
            "Project ID": "005",
            "Project Name": "E-commerce Webs",
            "Category": "Data Science",
            "Team Members": ["David Brown", "Emily Wilson", "Michael Lee"],
            "Description": "Building an online platform for buying and selling various products.",
            "Country": "Canada"
        },
        {
            "Project ID": "006",
            "Project Name": "Software Development",
            "Category": "Artificial Intelligence",
            "Team Members": ["Sophia Martinez", "Daniel Taylor", "Olivia Clark"],
            "Description": "Creating an addictive mobile game with challenging levels.",
            "Country": "UK"
        },
        {
            "Project ID": "007",
            "Project Name": "AI Chatbot",
            "Category": "Artificial Intelligence",
            "Team Members": ["Liam Anderson", "Ella White", "James Wilson"],
            "Description": "Designing an intelligent chatbot capable of answering user queries.",
            "Country": "Australia"
        },
        {
            "Project ID": "008",
            "Project Name": "Robotics Project",
            "Category": "Data Science",
            "Team Members": ["Ava Garcia", "Noah Brown", "Sophie Moore"],
            "Description": "Building a robot capable of performing various tasks autonomously.",
            "Country": "Germany"
        },
        {
            "Project ID": "009",
            "Project Name": "Data Analysis Tool",
            "Category": "Data Science",
            "Team Members": ["Mia Johnson", "William Taylor", "Ethan Martinez"],
            "Description": "Developing a tool for analyzing large datasets and generating insights.",
            "Country": "France"
        },
        {
            "Project ID": "010",
            "Project Name": "Software Development",
            "Category": "Artificial Intelligence",
            "Team Members": ["Isabella Wilson", "Mason Garcia", "Abigail Brown"],
            "Description": "Researching and implementing renewable energy solutions.",
            "Country": "Brazil"
        },
        {
            "Project ID": "011",
            "Project Name": "Healthcare App",
            "Category": "Artificial Intelligence",
            "Team Members": ["Evelyn Clark", "Logan Anderson", "Chloe Moore"],
            "Description": "Developing a mobile application for monitoring health metrics.",
            "Country": "Japan"
        }

        # Add more sample data entries here
    ]

    # Add sample data to projects dictionary
    for data in sample_data:
        projects[data["Project ID"]] = {
            "Project Name": data["Project Name"],
            "Category": data["Category"],
            "Team Members": data["Team Members"],
            "Description": data["Description"],
            "Country": data["Country"]
        }

# Call the function to add sample data
add_sample_data()






































# Function to update project details

def update_project():
    global project_details_saved
    if project_details_saved:
        print("Project details have already been saved. You cannot update project details.")
        return
    project_id = input("Enter Project ID to update: ")
    
    if project_id in projects:
        #Update project details
        projects[project_id]["Project Name"] = input("Enter Updated Project Name: ")
        projects[project_id]["Category"] = input("Enter Updated Category: ")
        projects[project_id]["Team Members"] = input("Enter Updated Team Members (separated by comma): ").split(",")
        projects[project_id]["Description"] = input("Enter Updated Brief Description: ")
        projects[project_id]["Country"] = input("Enter Updated Country: ")
    else:
        print("Project ID not found.")































# Function to delete project details
def delete_project():
    global project_details_saved
    if project_details_saved:
        print("Project details have already been saved. You cannot delete project details.")
        return
    project_id = input("Enter Project ID to delete: ")
    if project_id in projects:
        del projects[project_id]
        print("Project details deleted successfully.")
    else:
        print("Project ID not found.")

























# Function to view project details
def view_projects():
    global projects, project_details_saved
    
    if not projects:  # Check if there are no projects saved
        print("No projects have been saved yet")
        print()
        return
    
    if project_details_saved:  # Check if project details have not been saved
        print("Project details have already been saved. You cannot view project details.")
        print()
        return
    
    # Display project details sorted by Project ID
    for project_id in sorted(projects.keys()):
        print("Project ID:", project_id)  # No need for int() conversion if project_id should be a string
        for key, value in projects[project_id].items():
            print(key + ":", value)
        print()

























# Function to save project details to text file
def save_to_text_file():
    global project_details_saved
    try:
        if project_details_saved:
            print("Project details have already been saved.")
            print()
            return
    except IOError as err:
        print("Error saving project details:", err)


    
    # Write project details to a text file
    with open("project_details.txt", "w") as file:
        for project_id, details in projects.items():
            file.write(f"Project ID: {project_id}\n")
            for key, value in details.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")


            
    # Set the flag to indicate that project details have been saved
    project_details_saved = True
    print("Project details saved to text file.")
    print()


























# Function to simulate random spotlight selection
def random_spotlight_selection():
    # Initialize a dictionary to store randomly selected projects for each category
    selected_projects = {}
    categories = set([project['Category'] for project in projects.values()])
    
    # Iterate through each category
    for category in categories:
        # Get projects belonging to the current category
        category_projects = [project_id for project_id, project in projects.items() if project["Category"] == category]
        
        # Check if there are projects in the current category
        print(f"Category: {category}")
        for project_id in category_projects:
            project_details = projects[project_id]
            print()
            print()
            print("Selected Project Details:")
            for key, value in project_details.items():
                print(key + ":", value)
            print("Project id is : " + project_id)
            print()
            give_judge_pointss(project_id, project_details)  # call * marks funtion
            #give_judge_points(project_id, project_details)    # call numeric funtion
    yes_or_no = input("If you wish final marks, NOW it's ready. Do you want to continue (yes/no): ")
    if yes_or_no == 'yes':
        visualize_projects()
    else:
        print()



# Give judge  using ************
def give_judge_pointss(project_id, project_details):
    points = []
    for i in range(4):
        while True:
            judge_points = input(f"Judge {i+1} points (out of 5) for project {project_details['Project Name']}: ")
            if judge_points in ['*', '**', '***', '****', '*****']:
                break
            else:
                print("Invalid input! Please enter '*' to '*****'.")
        points.append(len(judge_points))
    
    # Calculate total points for the current project
    total_points = sum(points)
    
    # Update project details with total points
    projects[project_id]["Total Points"] = total_points


# Give judge points in numerical
def give_judge_points(project_id, project_details):
    points = []
    for i in range(4):
        while True:
            try:
                judge_points = int(input(f"Judge {i+1} points (out of 5) for project {project_details['Project Name']}: "))
                if 1 <= judge_points <= 5:
                    break
                else:
                    print("Invalid input! Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        points.append(judge_points)
        print()



        



































# Function to visualize award-winning projects
def visualize_projects():
    sorted_projects = sorted(projects.items(), key=lambda x: x[1].get("Total Points", 0), reverse=True)
    
    # Display details of 1st, 2nd, and 3rd place projects
    for i in range(3):
        # Determine the number of stars based on total points
        stars = "*" * sorted_projects[i][1].get("Total Points", 0)
        for _ in range(len(stars)):
            print("*")
        print(f"{i+1}st Place:")
        print("Project Name:", sorted_projects[i][1]["Project Name"])
        print("Country:", sorted_projects[i][1]["Country"])
        print("Total Points:", sorted_projects[i][1].get("Total Points", 0))
        print("Project ID:", sorted_projects[i][0])  # Access project ID from the sorted projects
    print("Exiting the program...")
    exit()












# Welcome page for your application
def display_welcome():
    welcome_text = """


$$$$$$$$\\                  $$\\             $$$$$$$$\\                                     
\\__$$  __|                 $$ |            $$  _____|                                    
   $$ | $$$$$$\\   $$$$$$$\\ $$$$$$$\\        $$ |      $$\\   $$\\  $$$$$$\\   $$$$$$\\        
   $$ |$$  __$$\\ $$  _____|$$  __$$\\       $$$$$\\    \\$$\\ $$  |$$  __$$\\ $$  __$$\\       
   $$ |$$$$$$$$ |$$ /      $$ |  $$ |      $$  __|    \\$$$$  / $$ /  $$ |$$ /  $$ |      
   $$ |$$   ____|$$ |      $$ |  $$ |      $$ |       $$  $$<  $$ |  $$ |$$ |  $$ |      
   $$ |\\$$$$$$$\\ \\$$$$$$$\\ $$ |  $$ |      $$$$$$$$\\ $$  /\\$$\\ $$$$$$$  |\\$$$$$$  |      
   \\__| \\_______| \\_______|\\__|  \\__|      \\________|\\__/  \\__|$$  ____/  \\______/       
                                                               $$ |                      
                                                               $$ |                      
                                                               \\__|                      
    Welcome to MY Application!
    This is your TechExpo - Event Mangement Systerm.
    """
    print(welcome_text)
    import time
    time.sleep(4)



















# Main program loop
display_welcome()
try:
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_project()
        elif choice == "2":
            update_project()
        elif choice == "3":
            delete_project()
        elif choice == "4":
            view_projects()
        elif choice == "5":
            save_to_text_file()
        elif choice == "6":
            random_spotlight_selection()
        elif choice == "7":
            visualize_projects()
        elif choice == "8":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
except KeyboardInterrupt:
    print("\nKeyboardInterrupt detected. Exiting the program...")

