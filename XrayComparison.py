import os
from tkinter import *   
from tkinter import messagebox
from PIL import Image,ImageTk, ImageChops
from prettytable import PrettyTable
ws = Tk()
ws.title("Xray comparision")
ws.geometry('900x600')
ws['bg'] = '#8B7B8B'
            
Label(ws, text = "\nWELCOME!!!!  Enter patient details.... \n\n",font=("algerian", 22),bg='#8B7B8B').pack()

Label(ws, text = "Enter patient name: ", font=("arial bold", 12),bg='#D8BFD8').pack()

p_nop = Entry(ws)
p_nop.pack(pady=10)

Label(ws, text = "Patient's aadhar no: ", font=("arial bold", 12),bg='#D8BFD8').pack()

p_aadhar = Entry(ws)
p_aadhar.pack(pady=10)

Label(ws, text = "Enter patient age: ", font=("arial bold", 12),bg='#D8BFD8').pack()

p_age = Entry(ws)
p_age.pack(pady=10)

Label(ws, text="Enter your image name: ", font=("arial bold", 12),bg='#D8BFD8').pack()

p_name = Entry(ws)
p_name.pack(pady=10)

def printValue():
    
    nop = p_nop.get()
    aadhar = p_aadhar.get()
    age = p_age.get()
    name = p_name.get()
    
    Label(ws, text=f" name of the patient is: {nop}", pady=10, bg='#8B7B8B').pack()
    Label(ws, text=f" Patient's aadhar no: {aadhar}", pady=10, bg='#8B7B8B').pack()
    Label(ws, text=f" Patient age = {age}", pady=10, bg='#8B7B8B').pack()
    Label(ws, text=f"{name}, given xray is compared with default xray. ", pady=10, bg='#8B7B8B').pack()

    i1 = Image.open('xray1.JPG')
    i2 = Image.open(name+'.JPG')

    assert i1.mode == i2.mode, "Different kinds of images."
    diff = ImageChops.difference(i1, i2)
    if diff.getbbox():
      i2.show()
       
      pairs = zip(i1.getdata(), i2.getdata())
       
    if len(i1.getbands()) == 1:
    # for gray-scale jpegs
      dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
      dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
 
    ncomponents = i1.size[0] * i1.size[1] * 3
    x = (dif / 255.0 * 100) / ncomponents
    t= "Defect(%) is: "+str(x)
    
    Label(ws, text=f'{x}', pady=20, bg='#8B7B8B').pack()
    file1 = open("myfile.txt","a")
    L = [aadhar,"----",nop,"----",age,"----",name,"----",t] 
    file1.writelines(L)
    file1.write("\n")
    file1.close()
    if(x>0 and x<1):
       y = " Low Risk!!! but Take precautions....!"
       Label(ws, text=f'{y}', pady=20, bg='#8B7B8B').pack()

    if(x>=1 and x<=3):
       y = " Medium Risk"
       Label(ws, text=f'{y}', pady=20, bg='#8B7B8B').pack()

    if(x>3 and x<=5):
       y="high risk"
       Label(ws, text=f'{y}', pady=20, bg='#8B7B8B').pack()

    if(x>5):
       y="Danger!! Admit in hospital waste fellow...!"
       Label(ws, text=f'{y}', pady=20, bg='#8B7B8B').pack()

    while(True):
     print("\n1. Display All Record")
     print("2. Search patient record by aadhar no:")
     print("3. Delete patient record by aadhar no:")
     print("4. Exit")

     n = int(input("\nEnter your choice: "))

     if(n==4):
        break

        
     elif(n==1):  
      print("\n******  List of present Records!!  ******\n")
      print("Aadhar no  ----- Patient Name ----- Age ----- Image name ---- Defect(%)\n")
      f = open("myfile.txt","r")
      ans = PrettyTable(["Aadhar no" , "Patient name" ,"Age" , "Image name" , "% value" ])
      while(True):
        d = f.readline()
        l = len(d)
        if(l==0):
             break
        #print(d.strip())
        d.strip()
        g = d.split('----')
        ans.add_row([g[0] ,g[1] ,g[2], g[3] , g[4] ])
    
      print(ans)        
      f.close()

     elif(n==2):
        search = input("Enter patient's aadhar no: ")
        f = open("myfile.txt","r")
        flag = 0
        while (True):
            t = f.readline()
            l=len(t)
            if (l==0):     
                break
            
            g = t.split('----')
            if(g[0] == search):
                print("\n **** Record Found!! ****\n")
                ans = PrettyTable(["Aadhar no" , "Patient name" ,"Age" , "Image name" , "% value" ])
                ans.add_row([g[0] ,g[1] ,g[2], g[3] , g[4] ])
                print(ans)
                #print("Aadhar no is ", g[0])
                #print("Patient name is ", g[1])
                #print("Age is ", g[2])
                #print("Image name is ", g[3])
                #print("-", g[4])
                flag=1
                break
            
        if(flag == 0):
            print("Record not found!!")
        f.close()

     elif(n==3):
        search = input("Enter patient's aadhar no: ")
        f = open("myfile.txt","r") 
        tt = open("temp.txt","w")
        h=0
        flag=0

        while(True):
            t =f.readline()
            l = len(t)
            if(l==0):
                break
            g = t.split('----')
            if(g[0]!=search):
                tt.write(t)
            if(g[0]==search):
                h=1
        f.close()
        tt.close()
    
        if(h==1):
            print("\n **** Record Deleted Successfully!! **** ")
            os.remove("myfile.txt")
            os.rename("temp.txt","myfile.txt")
                
        elif(h==0):
            print("Record Not found!! deletion unsuccessful")   
              
Button(
    ws,
    text="Submit", 
    padx=10, 
    pady=10,
    command=printValue
    ).pack()

def addRecord():
     ws.mainloop()

