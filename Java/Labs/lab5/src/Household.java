public class Household {
	//attributes
	private String name;
	private String address;
	private String city;
	private String state;
	private String zip;
	private int type;
	private Pet pet;
	
	//no arg constructor
	Household(){
		name = "";
		address = "";
		city = "";
		state = "";
		zip = "";
		type = 0;
		pet = new Pet();
	}
	//10 argument constructor
	Household(String n, String a, String c, String s, String z, int t, String np, Pet.species ss, Pet.color cc, boolean mma){
		name = n;
		address = a;
		city = c;
		state = s;
		zip = z;
		type = t;
		pet = new Pet(np, mma, ss, cc);
	}
	
	public String toString() {
		String info = "";
		info = String.format("Name: %S\n"
				+ "Address: %s\n"
				+ "City: %s\n"
				+ "State: %S\n"
				+ "Zip: %s\n"
				+ pet.toString(), name,address,city,state,zip);
		return info;
	}
	
	//inner class
	public class Pet{
		enum species{DOG, CAT, BIRD, RABBIT, HAMSTER, FISH, LYNC, NONE};
		enum color{BLACK, WHITE, BROWN, RED, ORANGE, GOLD, BLUE, GREEN, YELLOW, NA};
		private species animal;
		private color animalColor;
		private String name;
		private boolean mailManAttacker;
		
		// no args constructor
		Pet(){
			animal = species.NONE;
			animalColor = color.NA;
			name = "";
			mailManAttacker = false;
		}
		// copy constructor
		Pet(Pet p){
			animal = p.animal;
			animalColor = p.animalColor;
			name = p.name;
			mailManAttacker = p.mailManAttacker;
		}
		// 4 argument constructor
		Pet(String n, boolean mma, species s, color c){
			name = n;
			mailManAttacker = mma;
			animal = s;
			animalColor = c;
		}
		
		public String toString() {
			String info = "";
			info = String.format("Pet: %S\n"
					+ "Pet Color: %S\n"
					+ "Pet Name: %s\n"
					+ "Bit the mailman: %b", animal, animalColor, name, mailManAttacker);
			return info;
		}
		
	}
}
