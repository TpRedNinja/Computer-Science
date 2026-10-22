import java.util.Random;
import java.util.Scanner;
import java.io.*;
import static java.lang.System.out;

public class Driver {
	public static void main(String[] args)throws IOException { 
		int choice;
		Scanner s = new Scanner(System.in);
		out.println("Press:"
				+ "\n1 for coin toss program"
				+ "\n2 for making the groccery list file"
				+ "\n3 for reading groccery list file");
		choice = s.nextInt();
		
		switch (choice) {
		case 1:
			coinToss();
			break;
		case 2:
			groceryList();
			break;
		case 3:
			readGroceryList();
			break;
		default: 
			out.println("Error: Invalid input...\ngood bye");
			break;
		}
		s.close();
		
	}
	
	// function for reading grocery list file
	public static void readGroceryList()throws IOException {
		// variables
		Scanner s = new Scanner(System.in);
		out.println("What is the name of the file?");
		String fileName = s.nextLine();
		s.close();
		String product;
		double price,wholeSale;
		boolean closeOut;
		int totalProducts = 0, totalCloseOut = 0;
		double averagePrice, averageWholeSalePrice, totalPrices = 0, totalWholeSalePrice = 0;
		
		// try this but if file not found then print error
		try {
			File f = new File(fileName);
			Scanner inputFile = new Scanner(f);
			while(inputFile.hasNext()) {
				product = inputFile.nextLine();
				price = inputFile.nextDouble();
				wholeSale = inputFile.nextDouble();
				closeOut = inputFile.nextBoolean();
				inputFile.nextLine();
				totalProducts ++;
				if(closeOut) {
					totalCloseOut ++;
				}
				totalPrices += price;
				totalWholeSalePrice += wholeSale;
				out.println("\n");
				out.println("Summary:");
				out.printf("product name: %s"
						+ "\nPrice: %.2f"
						+ "\nWhole Sale Price: %.2f"
						+ "\nClose out: %b", product, price, wholeSale, closeOut);
			}
			averagePrice = totalPrices/totalProducts;
			averageWholeSalePrice = totalWholeSalePrice/totalProducts;
			out.println("\n");
			out.println("Product Info:");
			out.printf("Average Product Price: %.2f"
					+ "\nAverage Whole Sale Price: %.2f"
					+ "\nTotal Close outs: %d", averagePrice,averageWholeSalePrice, totalCloseOut);
			
			
			inputFile.close();
		}catch (FileNotFoundException e) {
			out.println("Error: File not found: " + e.getMessage());
		}
		
	}
	
	// function for creating grocery list file and writing to it
	public static void groceryList() throws IOException{ 
		// define variables
		File f = new File("GroceryList.txt");
		int numGroceries;
		Scanner s = new Scanner(System.in);
		PrintWriter pw = new PrintWriter(new FileWriter("GroceryList.txt", false));
		
		// main logic here
		out.println("How many Groceries do you want?");
		numGroceries = s.nextInt();
		for(int i = 0; i < numGroceries; i++) {
			out.println("What is the name of the product?");
			s.nextLine();
			String product = s.nextLine();
			//out.println(product);
			out.println("How much is " + product + "?");
			double price = s.nextDouble();
			out.println("What is the wholesale price of " + product + "?");
			double wholeSale = s.nextDouble();
			boolean closeOut = false;
			if (price == wholeSale) {
				closeOut = true;
			}
			if (f.exists()) {
				pw.println(product);
				pw.println(price);
				pw.println(wholeSale);
				pw.println(closeOut);
			}
			
		}
		pw.close();
		s.close();
	}
	
	
	// function for the coin toss program
	public static void coinToss() {
		// define variables
		int flips, guess, score = 0;
		
		//define scanner object
		Scanner s = new Scanner(System.in);
		//define random object
		Random r = new Random();
		
		// display purpose of program to user
		out.println("This program will simulate a coin toss.");
		
		//input validation
		do {
			out.println("How many times would you like to try and guess a coin flip?");
			flips = s.nextInt();
			if (flips < 0) {
				out.println("Error: Please enter a positive number.");
			}
		}while(flips < 0);
		
		// flips
		for (int i = 0; i < flips; i++) {
			out.println("Flipped coined");
			int coin = r.nextInt(2);
			
			// input validation part 2 boo-ga-loo
			do {
				out.println("Enter 1 for heads and 0 for tails");
				guess = s.nextInt();
				if (guess != 0 && guess != 1) {
					out.println("Error: Please enter 1 or 0");
				}
			}while(guess != 0 && guess != 1);
			
			//check guess 
			if (guess == coin) {
				out.println("Good job thats right");
				score++;
			} else {
				String answer;
				if(coin == 1) {
					answer = "heads";
				} else {
					answer = "tails";
				}
				out.println("Nope sorry the correct answer is " + answer);
			}
		}
		
		out.println("You got " + score + " correct out of " + flips);
		s.close();
	}
}
