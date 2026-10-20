
public class Driver {

	public static void main(String[] args) {
		int x = 10;
		switch(x)
		{
		case 10:
			x+=15;
		case 12:
			x-=5;
			break;
		default:
			x*=3;
		}
		System.out.println("Value of X: " + x);

	}

}
