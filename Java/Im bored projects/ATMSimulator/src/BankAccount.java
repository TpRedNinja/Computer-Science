import java.util.Scanner;
import static java.lang.System.out;
import static java.lang.System.err;

public class BankAccount {
	// attributes
	private double m_AccountBalance;
	private String m_AccountName;
	
	// constructor
	BankAccount(String aN){
		m_AccountBalance = 10000.00;
		m_AccountName = aN;
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
	private boolean canWithDrawMoney(double money) {
		if (m_AccountBalance - money < 0)
			return false;
		if (money > m_AccountBalance)
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
	public void withdrawMoney(double money) {
		boolean canWithDraw = canWithDrawMoney(money);
		if (canWithDraw) {
			if (m_AccountBalance - money == 0) {
				Scanner s = new Scanner(System.in);
				int choice;
				do {
					out.printf("\nWarning!: Withdrawing %.2f will put your account to 0.");
					out.println("Are you sure you want to continue?");
					out.println("Enter 1 for yes 2 for no");
					choice = s.nextInt();
					if (choice != 1 || choice != 2)
						err.println("Error!: Invalid Numbers");
				}while(choice != 1 || choice != 2);
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
				
				s.close();
			} else {
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
		out.printf("Current Balance for %s account: %.2f", name, bal);
	}
}
