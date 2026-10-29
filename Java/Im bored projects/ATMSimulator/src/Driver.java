import java.util.Scanner;
import static java.lang.System.out;
import static java.lang.System.err;

public class Driver {
	
	public static void displayMenu() {
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

	public static void main(String[] args) {
		// variables
		Scanner s = new Scanner(System.in);
		int choice, accountType;
		double money = 0.0;
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
			accounts[1] = savings;
		} else if (accountType == 3) {
			BankAccount checkings = new BankAccount(Name, BankAccount.AccountType.CHECKINGS);
			accounts[0] = checkings;
			BankAccount savings = new BankAccount(Name,BankAccount.AccountType.SAVINGS);
			accounts[1] = savings;
		}
		
		/*
		do {
				
				displayMenu();
			
				
				
			}while(!valid);
		*/
		
		s.close();
	}

}
