import requests
import json
import csv
import re
from tabulate import tabulate
from JSONplaceholder import JSONPlaceholderAPI


class UserService:
    def __init__(self):
        self.api = JSONPlaceholderAPI()
        self.history = []

    def getAllPosts(self):
        # if posts:
        #     print("All Posts:")
        #     for post in posts:
        #         print(f"Post ID: {post['id']}, Title: {post['title']}")
        # else:
        #     print("No posts found.")
        return self.api.get_posts()
    
    def getPostByID(self,id):
        self.api.get_post_details(id)

    def returnDetailTable(self, post_details):
        headers = ["Field", "Value"]
        table_data = []
        for key, value in post_details.items():
            table_data.append([key, value])

        res = tabulate(table_data, headers=headers, tablefmt="pretty")
        self.history.append(res)
        
        return res

    def returnDetailList(self, post_details):
        str = ""
        for key, value in post_details.items():
            str += (f"{key}: {value}")
        self.history.append(str)
        return str

    def save_to_json(self, data):
        with open('data\lab7\data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def save_to_csv(self, data):
        keys = data[0].keys()
        with open('data\lab7\data.csv', 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

    def save_to_txt(self, data):        
        with open('data\lab7\data.txt', 'w', newline='') as csv_file:
            csv_file.writelines(data)


    # def parse_user_input(self):
    #     post_id = input("Enter the ID of the post to view details: ")

    #     pattern = re.compile(r'^[1-9][0-9]*$')
    #     while not re.match(pattern, post_id):
    #         print("Invalid input. Please enter a valid positive integer ID.")
    #         post_id = input("Enter the ID of the post to view details: ")

    #     self.history.append(f"Post ID: {post_id}")
    #     return post_id

    # def start(self):
    #     posts = self.api.get_posts()
    #     self.display_posts(posts)

    #     post_id = self.parse_user_input()

    #     post_details = self.api.get_post_details(post_id)
    #     if post_details:
    #         print("\nPost Details:")
    #         display_choice = input("Choose display format (table/list): ").lower()
    #         if display_choice == 'table':
    #             self.display_post_details_table(post_details)
    #         elif display_choice == 'list':
    #             self.display_post_details_list(post_details)
    #         else:
    #             print("Invalid choice. Displaying as a list.")
    #             self.display_post_details_list(post_details)

    #         save_choice = input("Do you want to save this post? (json/csv/no): ").lower()
    #         if save_choice == 'json':
    #             self.save_to_json(post_details)
    #             print("Post details saved to data.json.")
    #         elif save_choice == 'csv':
    #             self.save_to_csv([post_details])
    #             print("Post details saved to data.csv.")
    #         elif save_choice == 'no':
    #             pass
    #         else:
    #             print("Invalid choice. Skipping saving.")
    #     else:
    #         print("Failed to fetch post details.")

    # def run(self):
    #     try:
    #         self.start()
    #     except requests.RequestException as e:
    #         print(f"Request Exception: {e}")
    #     except (KeyError, TypeError) as e:
    #         print("Invalid data received from API.")
    #     except KeyboardInterrupt:
    #         print("\nOperation interrupted by the user.")
    #     except Exception as e:
    #         print(f"An error occurred: {e}")

    # def save_to_history(self):
    #     with open('history.txt', 'a') as file:
    #         file.write("History:\n")
    #         for item in self.history:
    #             file.write(f"{item}\n")
    #         file.write("\n")

    # def run_tests(self):
    #     pass
            
    def save(self, text):
        res = input("JSON/CSV/TXT")
        if res not in ["JSON","CSV","TXT" ]:
            raise Exception
        
        if(res == "JSON"):
            self.save_to_json(text)
        elif(res == "CSV"):
            self.save_to_csv(text)
        elif(res == "TXT"):
            self.save_to_txt(text)
        else:
            raise Exception



    def start(self):

        while(True):
            try:
                res = []
                inp = input("Show all(1) or Show spec(2)\n Type \"ex\" eo exit\n")
                if inp == "ex":
                    break
                elif inp == "1":
                    post = self.getAllPosts()
                    tbl = input("Table/List: ")
                    if(tbl == "List"):
                        for elements in post:

                            res.append(self.returnDetailList(elements))
                        
                    elif(tbl == "Table"):
                        for elements in post:

                            res.append(self.returnDetailTable(elements))
    
                    else:
                        raise Exception
                elif inp == "2":
                    # post_id = int(input("Enter the ID of the post to view details: "))
                    # pattern = re.compile(r'^[1-9][0-9]*$')
                    # while not re.match(pattern, post_id):
                    #     print("Invalid input. Please enter a valid positive integer ID.")
                    #     post_id = input("Enter the ID of the post to view details: ")
                    post_id = input("Enter the ID of the post to view details: ")
                    pattern = re.compile(r'^\d{2,3}$')
                    while not re.match(pattern, post_id):
                            print("Invalid input. Please enter a valid positive integer ID (two or three digits).")
                            post_id = input("Enter the ID of the post to view details: ")


                    post = self.api.get_post_details(post_id)
                    tbl = input("Table/List:\n")
                    
                    if(tbl == "List"):
                        res.append( self.returnDetailList(post))

                    elif(tbl == "Table"):
                        res.append( self.returnDetailTable(post))
    
                    else:
                        raise Exception
                else:
                    raise Exception
                
                print(res)
                isSave = input("Save file?(Y/n)")
                if(isSave == "Y"):
                    self.save(res)



            except Exception as e:
                print("Wrong input")

        with open("data\lab7\history.txt", "w") as history:
            history.writelines(res)   
