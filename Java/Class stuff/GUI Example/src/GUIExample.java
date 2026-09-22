import javax.swing.JOptionPane;

public class GUIExample {
	public static void main(String[] args) {
		String dozens = JOptionPane.showInputDialog("How many cookies do you have?");
		int cookies = Integer.parseInt(dozens);
		int multiply = 12;
		cookies *= multiply;
		JOptionPane.showMessageDialog(null, String.format("I have %d cookies.", cookies));
		System.exit(0);
	}

}
