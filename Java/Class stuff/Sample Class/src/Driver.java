
public class Driver {
	public static void main(String[] args) {
		//racer 1
		Racer racer1 = new Racer();
		racer1.setName("Mario");
		racer1.setSpeed(120.5);
		racer1.displayInfo();
		
		// print stuff
		System.out.println("\nUsing the name accesor for racer1: " + racer1.getName());
		System.out.println("Using the speed accesor for racer1: " + racer1.getSpeed());
		
		//racer 2
		System.out.println();
		Racer racer2 = new Racer();
		racer2.setName("Luigi");
		racer2.setSpeed(100.99);
		//racer2.displayInfo();
		
		//test to string method
		System.out.println(racer2.toString());
		
		// using a constructor to create a object
		System.out.println();
		Racer racer3 = new Racer();
		System.out.println(racer3.toString());
		
		// racer 4
		System.out.println();
		Racer racer4 = new Racer("toad", 100.10);
		System.out.println(racer4.toString());
	}
}
