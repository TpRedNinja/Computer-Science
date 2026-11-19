import static java.lang.System.out;
import static java.lang.System.err;
import java.util.Scanner;
import java.util.ArrayList;
import java.io.*;


public class Driver {
	public static void displayMenu() {
		out.println("===== Please select a menu option from bellow =====\r\n"
				+ "1. Lab part 1\r\n"
				+ "2. Lab part 2\r");
	}
	public static boolean isValid(int thing, int numinputs) {
		int[] validInputs = new int[numinputs];
		//populate list with valid inputs
		for (int i = 0; i < validInputs.length; i++) {
			validInputs[i] = i+1;
		}
		
		// check list against user input
		for (int i = 0; i < validInputs.length; i++) {
			if(thing == validInputs[i])
				return true;
				
		}
		return false;
	}
	public static void main(String[] args) {
		int choice;
		Scanner s = new Scanner(System.in);
		do {
			displayMenu();
			choice = s.nextInt();
			if(!isValid(choice,2))
				err.println("Error: please enter 1 or 2");
			
		}while (!isValid(choice,2));
		s.close();
		switch(choice) {
			case 1:
				LoShu();
				break;
			case 2:
				Gas();
				break;
			default:
				break;
		}
		
		

	}
	
	public static void Gas() {
		ArrayList<FileInfo> info = new ArrayList<FileInfo>(60);
		double price;
		int week = 1;
		try {
			File f = new File("1994_Weekly_Gas_Averages.txt");
			Scanner input = new Scanner(f);
			while(input.hasNext()) {
				price = input.nextDouble();
				info.add(new FileInfo(price, week));
				week++;
			}
		}catch (FileNotFoundException e) {
			err.println("Error: File not found: " + e.getMessage());
		}
		out.println();
		
		
		
	}
	
	public static void LoShu() {
		int [][] hell = {{1,5,8},{9,7,6},{2,3,4}};
		int [][] Test1LoShu = {{4,9,2},{3,5,7},{8,1,6}};
		int [][] test2LoShu = {{4,1,2},{3,5,7},{8,9,6}};
		out.println("This will determine if an 2d array is a Lo Shu Magic Square");
		isLoShu(hell);
		isLoShu(Test1LoShu);
		isLoShu(test2LoShu);
	}
	
	public static String arrayToString(int[][] arr) {
		String m = "{";
		for(int i = 0; i < arr.length; i++) {
			for(int j = 0;  j < arr[i].length; j++) {
				if(j == 0) {
					 m += "{ " + arr[i][j] + ", ";
				} else if(j == 2 && i == 2) {
					m += arr[i][j] + " }";
				} else if(j == 2) {
					m += arr[i][j] + " }, ";
				}  else {
					m += arr[i][j] + ", ";
				}
			}
			if(i == 2) {
				m += "}";
			}
		}
		return m;
	}
	
	public static int test1(int[][] hell) {
		int value1 = 0;
		int value2 = 0;
		int value3 = 0;
		
		//test 1 do the rows equal the same value
		for(int i = 0; i < hell.length; i++) {
			if(value1 == 0) {
				value1 = hell[i][0]+ hell[i][1]+ hell[i][2];
				continue;
			} else if (value2 == 0) {
				value2 = hell[i][0]+ hell[i][1]+ hell[i][2];
				continue;
			} else if (value3 == 0) {
				value3 = hell[i][0]+ hell[i][1]+ hell[i][2];
				continue;
			}
			
		}
		
		if(value1 == value2 && value1 == value3 && value1 == 15) {
			return value1;
		} else {
			return -1;
		}
	}
	
	public static int test2(int[][] hell) {
		int value1 = 0;
		int value2 = 0;
		int value3 = 0;
		int i = 0;
		//  test 2 do the columns equal each other
		for(int j = 0; j < hell[i].length; j++) {
			if(value1 == 0) {
				value1 = hell[i][j]+ hell[i+1][j]+ hell[i+2][j];
				continue;
			} else if (value2 == 0) {
				value2 = hell[i][j]+ hell[i+1][j]+ hell[i+2][j];
				continue;
			} else if (value3 == 0) {
				value3 = hell[i][j]+ hell[i+1][j]+ hell[i+2][j];
				continue;
			}
		}
				
		if(value1 == value2 && value1 == value3 && value1 == 15) {
			return value1;
		} else {
			return -2;
		}
	}
	
	public static int test3(int[][] hell) {
		//test 3 diagonals
		int value1 = 0,value2 = 0;
		for(int i = 0; i < hell.length;i++) {
			for(int j = 0; j < hell[i].length;j++) {
				if(i == j) {
					value1 += hell[i][j];
					if(i == 1 && j == 1) {
						value2 += hell[i][j];
					}
				} else if(i == j+2) {
					// when i is 2 and j is 0 add
					value2 += hell[i][j];
				} else if(j == i+2) {
					// when j is 2 and i is 0 add
					value2 += hell[i][j];
					
				}
			}
		}
		
		
		if(value1 == value2 && value1 == 15) {
			return value1;
		} else {
			return -3;
		}
	}
	
	public static void isLoShu(int[][] hell) {
		boolean test;
		test = test1(hell) == test2(hell) && test1(hell) == test3(hell);
		//out.println(test1(hell) + ", "+ test2(hell) + ", " + test3(hell));
		if(test) {
			out.println("Yes, the array " + arrayToString(hell) + " is LoShu");
		} else {
			out.println("No, the array " + arrayToString(hell) + " is not LoShu");
		}
	}
}
