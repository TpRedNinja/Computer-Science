import java.util.Random;

public class Job {
	private double m_HourlyPay;
	private Role m_Role;
	private String m_StoreName;
	private final double MINWAGE = 15.00;
	enum Role{
		STOCKER(1),
		CASHIER(2),
		MANAGER(3);
		
		private final int ROLE;
		
		Role(int role){
			this.ROLE = role;
		}
		
		public int getRole() {
			return ROLE;
		}
	}
	
	// constructors
	Job(){ // default constructor
		m_StoreName = "";
		m_Role = Role.CASHIER;
		m_HourlyPay = 0.0;
	}
	Job(String SN){// set store name
		m_StoreName = SN;
		m_Role = Role.CASHIER;
		m_HourlyPay = 0.0;
	}
	Job(String SN, Role r){// set store name and role
		m_StoreName = SN;
		m_Role = r;
		m_HourlyPay = pickwage();
	}
	
	//getters and setters
	public String getStore(){
		return m_StoreName;
	}
	
	public double getPay() {
		return m_HourlyPay;
	}
	
	public void setStore(String s) {
		m_StoreName = s;
	}
	
	public void setPay(double p) {
		m_HourlyPay = p;
	}
	
	// other functions
	private double pickwage() { // picks the wage based off the role if theirs no asking wage
		Role r = m_Role;
		Random RD = new Random();
		double wage = 0.0;
		if(r == Role.CASHIER)
			wage = MINWAGE;
		else if (r == Role.STOCKER) {
			double bonus = RD.nextDouble(1, 5);
			wage = MINWAGE + bonus;
		} else if (r == Role.MANAGER) {
			double bonus = RD.nextDouble(5, 40);
			wage = MINWAGE + bonus;
		}
			
		return wage;
	}
}
