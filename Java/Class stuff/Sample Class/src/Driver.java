
public class Driver {
	public static void main(String[] args) {
		Racer racer1 = new Racer();
		racer1.setName("Mario");
		racer1.setSpeed(120.5);
		racer1.displayInfo();
		System.out.println("Using the name accesor for racer1: " + racer1.getName());
		System.out.println("Using the speed accesor for racer1: " + racer1.getSpeed());

		Racer racer2 = new Racer();
		racer2.setName("Luigi");
		racer2.setSpeed(100.99);
		racer2.displayInfo();
	}
}
