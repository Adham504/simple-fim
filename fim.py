import os, hashlib, json

def hash_calc(file_path):

    with open(file_path, 'rb') as f:

        file_content = f.read()

        file_hash = hashlib.sha256(file_content)

        return file_hash.hexdigest()
    


def scan_folder(folder_path):

    scan_result = {}
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        
        if os.path.isfile(full_path):
            scan_result.update({file: hash_calc(full_path)})

    return scan_result

def create_baseline(foler_path, baseline_file="/home/adham/Documents/fim_project/baseline.json"):
    current_hash = scan_folder(foler_path)

    with open(baseline_file, "w") as f:
        json.dump(current_hash, f, indent=4)


def monitor(folder_path):

    baseline_dict = {}
    with open("/home/adham/Documents/fim_project/baseline.json", 'r') as f:
        baseline_dict.update(json.load(f))
        current_data = scan_folder(folder_path)


        for filename, saved_hash in baseline_dict.items():
            if filename not in current_data:
                print(f'file {filename} was deleted')
            elif current_data[filename] != saved_hash:
                print(f'file {filename} was modeifed')

        for file_name in current_data:
            if file_name not in baseline_dict:
                print(f'new file {file_name} was added')



if __name__ == "__main__":
    print("Welcome to the FIM Tool!")
    print("1. Create Baseline")
    print("2. Start Monitoring")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        create_baseline("/home/adham/Documents/fim_project/target")
        print("Baseline created!")
    elif choice == "2":
        monitor("/home/adham/Documents/fim_project/target")