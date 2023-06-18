print("\n\n CONTACT BOOK BY USING DICTIONARY \n")

# Creating an empty dictionary as contact to save the names of contact numbers
contact={}

# creating a display_function to display the contact names and numbers 
def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
        
# taking the while loop until the condition gets false
while True:
    
    # we are takking choice of user i.e, user can Add new contact,Search contact,Display contact,Edit contact,Delete contact,Exit
    choice=int(input("\n 1.Add new contact \n 2.Search contact \n 3.Display contact \n 4.Edit contact \n 5.Delete contact \n 6.Exit \n\n Enter your choice:"))
    
    # if the users choice is 1 then user can add the new contact
    if choice==1:
        
        # Entering the contact name
        name=input("\n Enter the contact name:")
        
        # Entering the mobile number
        phone=input("\n Enter the mobile number:")
        
        # saving the name and phone in contact dictionary
        contact[name]=phone
        
    # if the users choice is 2 then user can search the contact they want to
    elif choice==2:
        
        # entering the contact name which they want to search
        search_name=input("\n Enter the contact name:")
        
        # searching if the name is in contact or not
        if search_name in contact:
            
            # if the name is in contact the print search_name,'s contact number is,contact[search_name]
            print(search_name,"'s contact number is ",contact[search_name])
            
        # if the name is not in contact
        else:
            
            # displaying the name is not found in contact book
            print("\n Name is not found in contact book")
            
    # if the users choice is 3 then they can display the contacts
    elif choice==3:
        
        # checking if there are any contacts or not
        if not contact:
            
            # if there are no contacts then display "Empty contact book"
            print("\n Empty contact book")
            
        # if there are contacts then display the contacts
        else:
            
            # using the function to display the contacts
            display_contact()
            
    # if the users choice is 4 then they can edit the contacts numbers
    elif choice==4:
        
        # entering the contact name which they want to edit the number
        edit_contact=input("\n Enter the contact name to be edited:")
        
        # checking if the contact number which we want to edit is in contact or not
        if edit_contact in contact:
            
            # if the contact number which we want to edit is in contact the ask user to Enter new mobile number
            phone=input("\n Enter mobile number:")
            
            # saving the edited contact number in contacts
            contact[edit_contact]=phone
            
            # displaying Contact updated after saving the new number
            print("\n Contact updated")
            
            # using the function to display the contacts after the changes
            display_contact()
        
        # if the contact number which we want to edit is not in contact 
        else:
            
            # displaying the "Name is not found in contact book"
            print("\n Name is not found in contact book")
            
    # if the users choice is 5 then they can delete the contact
    elif choice==5:
        
        # asking the user to enter the contact which they want to delete
        del_contact=input("\n Enter the contact to be deleted")
        
        # checking if the entered contact is in contact or not
        if del_contact in contact:
            
            # confirming whether the user really want to delete the contact or not 
            confirm=input("\n Do you want to delete this contact yes/no:")
            
            # if the entered confirm=yes,or Yes then we can delete the contact
            if confirm=='yes' or confirm=='Yes':
                
                # deleting the entered contact by using pop()
                contact.pop(del_contact)
                
                # displaying the contact after deleting the contact
                display_contact()
                
            # if the entered contct is not in contact
            else:
                
                # Displaying "Name is not found in contact book"
                print("\n Name is not found in contact book")
                
    # if the users choice is 6 or more than 6 then they can exit from the contact book
    else:
        
        # breaking the while loop and exiting from the loop
        break
