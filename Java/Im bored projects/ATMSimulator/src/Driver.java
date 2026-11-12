import java.util.Scanner;
import static java.lang.System.out;
import static java.lang.System.err;

public class Driver {
	public static boolean isRunning = true;
	public static void displayMenu() {
		out.println("");
		out.println("===== JAVA ATM =====\r\n"
				+ "1. View Balance\r\n"
				+ "2. Deposit Money\r\n"
				+ "3. Withdraw Money\r\n"
				+ "4. Account Information\r\n"
				+ "5. Exit");
	}
	
	//check if user input is valid
	public static boolean isValid(int thing, int numinputs) {
		int[] validInputs = new int[numinputs];
		//populate list with valid inputs
		for (int i = 0; i < validInputs.length; i++) {
			validInputs[i] = i+1;
		}
		
		// check list against user input
		for (int i = 0; i < validInputs.length; i++) {
			if(thing == validInputs[i])
				return true;
				
		}
		return false;
	}
	
	//check if amount is valid
	public static boolean isValidAmount(double amount) {
		if (amount > 0)
			return true;
		return false;
	}
	
	//check how many accounts we have
	public static boolean twoAccounts(BankAccount[] a) {
		if(a[1] != null) {
			return true;
		}
		return false;
	}
	
	// check the account balance
	public static void checkAcctBal(BankAccount[] a, Scanner s) {
		int choice;
		if (twoAccounts(a)){
			do {
				out.println("Which account balance would you like to see?");
				out.println("Enter 1 for checkings and 2 for savings");
				s.nextLine();
				choice = s.nextInt();
				if(!isValid(choice,2)) {
					err.println("Error: Invalid input");
				}
				
			}while(!isValid(choice,2));
			switch(choice) {
			case 1:
				out.println("Checkings Selected");
				a[0].displayInfo();
				break;
			case 2:
				out.println("Savings Selected");
				a[1].displayInfo();
				break;
			}
			
		} else {
			a[0].displayInfo();
		}
		
	}
	
	//deposit money
	public static void depMoney(BankAccount[] a, Scanner s) {
		int choice;
		double amount;
		BankAccount b = null;
		if (twoAccounts(a)){
			
			do {
				out.println("Which account would you like to deposit money to?");
				out.println("Enter 1 for checkings and 2 for savings");
				s.nextLine();
				choice = s.nextInt();
				if(!isValid(choice,2)) {
					err.println("Error: Invalid input");
				}
				
			}while(!isValid(choice,2));
			
			switch(choice) {
			case 1:
				b = a[0];
				out.println("Checkings Selected");
				break;
			case 2:
				b = a[1];
				out.println("Savings Selected");
				break;
			}
			
		} else {
			b = a[0];
		}
		do {
			out.println("How much money would you like to deposit?");
			out.println("Enter any number from 1 to infinity");
			s.nextLine();
			amount = s.nextDouble();
			if (!isValidAmount(amount)) {
				err.println("Error: Please enter a positive number");
			}
		}while(!isValidAmount(amount));
		b.depositeMoney(amount);
	}
	
	//with draw money
	public static void withMoney(BankAccount[] a, Scanner s) {
		int choice;
		double amount;
		BankAccount b = null;
		if (twoAccounts(a)){
			do {
				out.println("Which account would you like to withdraw money from?");
				out.println("Enter 1 for checkings and 2 for savings");
				s.nextLine();
				choice = s.nextInt();
				if(!isValid(choice,2)) {
					err.println("Error: Invalid input");
				}
				
			}while(!isValid(choice,2));
			
			switch(choice) {
			case 1:
				b = a[0];
				out.println("Checkings Selected");
				break;
			case 2:
				b = a[1];
				out.println("Savings Selected");
				break;
			}
			
		} else {
			b = a[0];
		}
		do {
			out.println("How much money would you like to withdraw?");
			out.println("Enter any number from 1 to infinity");
			s.nextLine();
			amount = s.nextDouble();
			if (!isValidAmount(amount)) {
				err.println("Error: Please enter a positive number");
			} else if (!b.canWithDrawMoney(amount)) {
				b.withdrawMoney(amount, s);
			}
		}while(!isValidAmount(amount) || !b.canWithDrawMoney(amount));
		b.withdrawMoney(amount, s);
		
	}
	
	// check the account info
	public static void acctInfo(BankAccount[] a, Scanner s) {
		int choice;
		if (twoAccounts(a)){
			do {
				out.println("Which account info would you like to see?");
				out.println("Enter 1 for checkings and 2 for savings");
				s.nextLine();
				choice = s.nextInt();
				if(!isValid(choice,2)) {
					err.println("Error: Invalid input");
				}
				
			}while(!isValid(choice,2));
			switch(choice) {
			case 1:
				out.println("Checkings Selected");
				a[0].displayAcctInfo();
				break;
			case 2:
				out.println("Savings Selected");
				a[1].displayAcctInfo();
				break;
			}
			
		} else {
			a[0].displayAcctInfo();
		}
	}
	
	public static void main(String[] args) {
		// variables
		Scanner s = new Scanner(System.in);
		int choice, accountType;
		String Name;
		
		BankAccount[] accounts = new BankAccount[2];
		
		// input stuff
		out.println("Welcome to atm simulator");
		out.println("This program will simulate a atm");
		out.println("To get started what is your Name?");
		Name = s.nextLine();
		do {
			out.println("Happy to see you " + Name);
			out.println("Would you like to open a checking, savings, or both?");
			out.println("Enter 1 for checkings"
					+ "\n2 for savings"
					+ "\n3 for both");
			accountType = s.nextInt();
			if(!isValid(accountType, 3)) {
				err.println("Error!: Invalid Input");
			}
		
			
		}while(!isValid(accountType, 3));
		
		
		if(accountType == 1) {
			BankAccount checkings = new BankAccount(Name, BankAccount.AccountType.CHECKINGS);
			checkings.displayInfo();
			accounts[0] = checkings;
		} else if(accountType == 2) {
			BankAccount savings = new BankAccount(Name,BankAccount.AccountType.SAVINGS);
			accounts[0] = savings;
		} else if (accountType == 3) {
			BankAccount checkings = new BankAccount(Name, BankAccount.AccountType.CHECKINGS);
			accounts[0] = checkings;
			BankAccount savings = new BankAccount(Name,BankAccount.AccountType.SAVINGS);
			accounts[1] = savings;
		}
		while(isRunning)
		{
			do{
				displayMenu();
				choice = s.nextInt();
				if(!isValid(choice,5)) {
					err.println("Error:Invalid input");
				}
				
			}while(!isValid(choice,5));
			
			
			switch(choice){
			case 1:
				checkAcctBal(accounts,s);
				break;
			case 2:
				depMoney(accounts, s);
				break;
			case 3:
				withMoney(accounts, s);
				break;
			case 4:
				acctInfo(accounts, s);
				break;
			case 5:
				isRunning = false;
				break;
			default:
				break;
			}
		}
		
		
		s.close();
	}

}
