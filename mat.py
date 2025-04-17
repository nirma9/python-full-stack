print("------------------welcome to To-Do-List Appliacations-------------------")
def task():
               tasks = []
               total_task = int(input("enter a number of task you want.:"))
               for i in range(total_task):
                       task_name = input(f"enter new task {i+1}= ")
                       tasks.append(task_name)
               print(f"Todays Task \n{tasks}")
               # print("\n todays task ")
               while True:
                     try:  
                       operation = int(input("which operation you want to choose\n 1-add\n2-update \n 3-delete \n 4-view \n 5-Exit.."))
                       if operation ==1:
                               add = input("enter task you want  to add")
                               tasks.append(add)
                               print(f"task{add } has added successfully..")
                       elif operation == 2:
                               up = input("enter the tasks you want  to upodate")
                               if up in tasks:
                                       ip = input("enter you task..")
                                       ind = tasks.index(up)
                                       tasks[ind] = ip
                                       print("updated task successfully")
                               else:
                                        print("task not found.:")
                      
                       elif operation == 3:
                               del_task = input("enter the task you want to delete..")
                               if del_task in tasks:
                                       tasks.remove(del_task)
                                       print(f"task {del_task} is added successfully")
                               else:
                                       print("not task found")
                       elif operation == 4:
                               print("Todays tasks:",tasks)
                       elif operation == 5:
                               print("exiting ,good byee")
                       else:
                               print("invalid ")
                     except ValueError:
                             print("Error: the value error ")

                                      
                              
print(task())
                                        
               

               