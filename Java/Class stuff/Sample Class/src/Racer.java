
public class Racer {
	// attributes
	private String m_Name;
	private double m_Speed;
	
	// constructors for racer class
	Racer(){ // default constructor
		m_Name = "";
		m_Speed = 0.0;
	};
	Racer(String name) { // only name attribute
		m_Name = name;
		m_Speed = 0.0;
	}
	Racer(double speed) { // only speed attribute
		m_Name = "";
		m_Speed = speed;
	}
	Racer(String name, double speed) { // all attributes
		m_Name = name;
		m_Speed = speed;
	}
	
	// setters
	public void setName(String name) {
		m_Name = name;
	}
	public void setSpeed(double speed) {
		m_Speed = speed;
	}
	
	// getters
	public String getName() {
		return m_Name;
	}
	public double getSpeed() {
		return m_Speed;
	}
	
	// displays the racers attributes
	public void displayInfo() {
		System.out.println("Racer name: " + m_Name + "\nSpeed: " + m_Speed);
	}
	
	//return attributes as a string
	public String toString() {
		return "Racer name: " + m_Name + "\nSpeed: " + m_Speed;
	}
}
