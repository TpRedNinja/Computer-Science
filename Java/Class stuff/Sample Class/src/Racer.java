
public class Racer {
	// attributes
	private String m_Name;
	private double m_Speed;
	
	// setter for the name attribute
	public void setName(String name) {
		m_Name = name;
	}
	
	// getter for the name attribute
	public String getName() {
		return m_Name;
	}
	
	// setter for the speed attribute
	public void setSpeed(double speed) {
		m_Speed = speed;
	}
	
	// getter for the speed attribute
	public double getSpeed() {
		return m_Speed;
	}
	
	// displays the racers attributes
	public void displayInfo() {
		System.out.println("Racer name: " + m_Name + "\nSpeed: " + m_Speed);
	}
}
