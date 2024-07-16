int val;
if(top==MAX-1)
 print("Stack is Full\n")
else
 {
    print("Enter the vale to be pushed:");
    scanf("%d",&val);
    stack[++top]=val;
    print("Successfully Pushed\n");
 }