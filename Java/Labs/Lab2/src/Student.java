public class Student {
	// attributes
	private String m_Name;
	private String m_Major;
	private int m_Id;
	private int m_Credits;
	
	// constructors
	Student(){ // default constructor
		m_Name = "";
		m_Major = "";
		m_Id = 0;
		m_Credits = 0;
	}
	Student(String n, String m, int id, int c){
		m_Name = n;
		m_Major = n;
		m_Id = id;
		m_Credits = c;
	}
	
	// setters
	public void setName(String name) {
		m_Name = name;
	}
	public void setMajor(String major) {
		m_Major = major;
	}
	public void setId(int id) {
		m_Id = id;
	}
	public void setCredits(int credits) {
		m_Credits = credits;
	}
	
	// getters
	public String getName() {
		return m_Name;
	}
	public String getMajor() {
		return m_Major;
	}
	public int getId() {
		return m_Id;
	}
	public int getCredits() {
		return m_Credits;
	}
	
	public String toString() {
		return "Student Name: " + m_Name + "\nStudent Major: " + m_Major +
				"\nStudent Id: " + m_Id + "\nStudents Credits: " + m_Credits;
	}
}
