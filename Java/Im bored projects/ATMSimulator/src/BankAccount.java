import java.util.Scanner;
import static java.lang.System.out;
import static java.lang.System.err;

public class BankAccount {
	// attributes
	private double m_AccountBalance;
	private String m_AccountName;
	private AccountType m_AccountType;
	private final double MINBALANCE = 300.00; 
	enum AccountType{
		CHECKINGS(1),
		SAVINGS(2);
		
		private final int TYPE;
		
		AccountType(int type){
			this.TYPE = type;
		}
		
		public int getType() {
			return TYPE;
		}
	}
	
	// constructors
	BankAccount (){ // default
		m_AccountBalance = 0.0;
		m_AccountName = "N/A";
		m_AccountType = AccountType.CHECKINGS;
	}
	BankAccount(String aN){ // set name
		m_AccountBalance = 0.0;
		m_AccountName = aN;
		m_AccountType = AccountType.CHECKINGS;
		
	}
	BankAccount(String aN, double aB){ // set name and balance
		m_AccountBalance = aB;
		m_AccountName = aN;
		m_AccountType = AccountType.CHECKINGS;
		
	}
	BankAccount (String aN, AccountType type){ // set name and type
		m_AccountName = aN;
		m_AccountType = type;
		if (type == AccountType.SAVINGS) {
			m_AccountBalance = MINBALANCE;
		} else {
			m_AccountBalance = 0.0;
		}
	}
	BankAccount (String aN ,double aB, AccountType type){ // set all attributes
		m_AccountBalance = aB;
		m_AccountName = aN;
		m_AccountType = type;
	}
	
	//getters and setters
	public double getBalance() {
		return m_AccountBalance;
	}
	
	public String getName() {
		return m_AccountName;
	}
	
	public void setBalance(double bal) {
		m_AccountBalance = bal;
	}
	
	public void setName(String name) {
		m_AccountName = name;
	}
	
	// deposit money
	public void depositeMoney(double money) {
		m_AccountBalance += money;
		out.printf("\nDeposit Successful!" 
		+ "\nAmount Deposited: %.2f"
		+ "\nNew Balance: %.2f", money, m_AccountBalance);
	}
	
	// to check if we can withdraw;
	public boolean canWithDrawMoney(double money) {
		if (m_AccountBalance - money < MINBALANCE && m_AccountType == AccountType.SAVINGS)
			return false;
		else if (money > m_AccountBalance && m_AccountType == AccountType.CHECKINGS)
			return false;
		
		return true;
	}
	
	// displays withdraw info because i don't want the function to be long
	private void displayWithDrawInfo(double money, double bal) {
		out.printf("\nWithdraw Successful!" 
				+ "\nAmount Withdrawn: %.2f"
				+ "\nNew Balance: %.2f", money, m_AccountBalance);
	}
	
	// withdraw money
	public void withdrawMoney(double money, Scanner s) {
		boolean canWithDraw = canWithDrawMoney(money);
		if (canWithDraw) {
			boolean isZero = m_AccountBalance - money == 0;
			boolean isSavings = m_AccountType == AccountType.SAVINGS;
			boolean lessMin = (isSavings && m_AccountBalance - money < MINBALANCE);
			if (isZero && !isSavings) {
				int choice;
				do {
					out.printf("Warning!: Withdrawing %.2f will put your account to 0.", money);
					out.println("\nAre you sure you want to continue?");
					out.println("Enter 1 for yes 2 for no");
					choice = s.nextInt();
					if (choice != 1 && choice != 2)
						err.println("Error!: Invalid Numbers");
				}while(choice != 1 && choice != 2);
				switch(choice) {
				case 1:
					m_AccountBalance -= money;
					displayWithDrawInfo(money, m_AccountBalance);
					break;
				case 2:
					break;
				default:
					break;
				}
			} else if (isSavings && lessMin) {
				err.println("Error!: Can not withdraw money from account its below the min balance required");
				out.println("Min balance required: " + MINBALANCE);
			}else {
				m_AccountBalance -= money;
				displayWithDrawInfo(money, m_AccountBalance);
			}
			
		} else {
			err.println("Error: Insufficent Funds");
			out.println("Current Funds: " + m_AccountBalance);
		}
		
	}
	
	// display info
	public void displayInfo() {
		String name = getName();
		double bal = getBalance();
		AccountType type = m_AccountType;
		if (type == AccountType.CHECKINGS)
			out.printf("Current Balance for %s checkings account: %.2f", name, bal);
		else if (type == AccountType.SAVINGS)
			out.printf("Current Balance for %s savings account: %.2f", name, bal);
	}
	
	public void displayAcctInfo() {
		String name = getName();
		double bal = getBalance();
		AccountType type = m_AccountType;
		out.printf("Account Name: %s"
				+ "\nAccount Balance: %.2f"
				+ "\nAccount Type: " + type, name, bal);
	}
}
