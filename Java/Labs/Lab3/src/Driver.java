import java.util.Scanner;
import static java.lang.System.out;

public class Driver {
	public static void main(String[] args) {
		int program;
		// get user input
		Scanner keyboard = new Scanner(System.in);
		out.println("Eneter 1 for chocolatebars program and 2 for army rank program: ");
		program = keyboard.nextInt();
		if(program == 1) {
			out.println("How many Supreme Chocolate Bars do you want to purchase? ");
			int totalBars = keyboard.nextInt(); // how many chocolate bars a user wants
			keyboard.close();
			if (totalBars >= 0) {
				ChocolateSales sales = new ChocolateSales(totalBars);
				double subTotal = sales.getSubTotal();
				double discount = sales.calcDicount();
				double tax = sales.getSalesTax();
				double discountPrice = subTotal - discount;
				if(subTotal == discountPrice) {
					out.println("No discount was applied");
				}
				double totalPrice = discountPrice + tax;
				out.printf("Your Reciept:"
						+ "\nSubtotal: $%.2f%n"
						+ "\nDiscount Amount: $%.2f%n" 
						+ "\nSales Tax: $%.2f%n"
						+ "\nTotal Price: $%.2f%n"
						
						, subTotal, discount, tax, totalPrice);
			} else {
				out.println("Error: negative number entered");
			}
		} else if (program == 2) {
			armyProgram();
		} else {
			out.println("Error: you didnt enter any valid numbers. Run the program again to try again");
		}
		
	}
	
	public static void armyProgram() {
		int rank;
		Scanner keyboard = new Scanner(System.in);
		out.println("Enter your enlisted rank here: E-");
		rank = keyboard.nextInt();
		keyboard.close();
		switch(rank) {
		case 1:
			out.println("You are a Private (no insignia)");
			break;
		case 2:
			out.println("You are a Private");
			break;
		case 3:
			out.println("You are a Private First Class");
			break;
		case 4:
			out.println("You are a Specialist/Corporal");
			break;
		case 5:
			out.println("You are a Sergeant");
			break;
		case 6:
			out.println("You are a Staff Seargeant");
			break;
		case 7:
			out.println("You are a Sergeant First Class");
			break;
		case 8:
			out.println("You are a Master Seargeant");
			break;
		case 9:
			out.println("You are a First Sergeant");
			break;
		default:
			out.println("Error: invalid rank number");
			break;
			
		}
		
	}

}
