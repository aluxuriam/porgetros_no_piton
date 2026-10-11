start = True
import datetime
hoje = (datetime.date.today())
print ("Wellcome to your To Do List")
while start:
    try:
        with open("list.txt", "r") as file:
            tasks = file.readlines()
    except FileNotFoundError:
        tasks = []
    print ("\nchose what you want to do")
    choice = int(input(" [1] see your list\n [2] add a item in your list\n [3] remove a item from your list\n [4] mark as done\n [5] exit list \n ").strip())
    if choice == 1:
        if not tasks:
            print("Your list is empty.\n")
        else:
            try:
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task.strip()}")
            except FileNotFoundError:
                tasks = []
    elif choice == 2:
        with open("list.txt", "a") as file:
            taskadd = input("what task do you want to add? ").strip()
            file.write(taskadd + "     add "+hoje.strftime('%d/%m/%Y')+"\n")
            print ("task added!")
    elif choice == 3:
        if not tasks:
            print ("you don't have a tasks added")
        else:
            num = int(input("write the number of the task to delete: "))
            if 1 <= num <= len(tasks):
                del tasks[num-1]
                with open("list.txt", "w") as file:
                    file.writelines(tasks)
                print ("done, your task has been deleted\n")
    elif choice == 4:
        done = int(input("choose the number you want to mark as done: "))
        if 1 <= done <= len(tasks):
            tasks[done-1] = tasks[done-1].strip() + f"    done " + hoje.strftime('%d/%m/%Y\n')
            with open("list.txt", "w") as file:
                file.writelines(tasks)
            print ("your task has been marked done")
    elif choice == 5:
        print("goodbye!")
        break