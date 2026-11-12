import java.awt.EventQueue;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import javax.swing.SwingConstants;
import java.awt.GridLayout;
import java.awt.FlowLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.Color;

public class TestWindow extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					TestWindow frame = new TestWindow();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}
	
	

	/**
	 * Create the frame.
	 */
	public TestWindow() {
		Color background = new Color(16, 25, 35);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBackground(new Color(38, 45, 54));
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JPanel panel = new JPanel();
		panel.setBackground(new Color(16, 25, 35));
		panel.setBounds(110, 0, 192, 158);
		contentPane.add(panel);
		panel.setLayout(null);
		
		JButton BottomLeft = new JButton("Balance");
		BottomLeft.setBounds(0, 135, 98, 23);
		panel.add(BottomLeft);
		
		JButton BottomRight = new JButton("Account Info");
		BottomRight.setBounds(94, 135, 98, 23);
		panel.add(BottomRight);
		
		JButton TopLeft = new JButton("Deposit");
		TopLeft.setForeground(Color.WHITE);
		TopLeft.setBackground(background);
		TopLeft.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		TopLeft.setBounds(0, 113, 98, 22);
		panel.add(TopLeft);
		
		JButton TopRight = new JButton("Withdraw");
		TopRight.setForeground(new Color(16, 25, 35));
		TopRight.setBounds(98, 113, 98, 22);
		panel.add(TopRight);
		
		JButton btn1 = new JButton("1");
		btn1.setBounds(110, 157, 64, 20);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.setBounds(174, 157, 64, 20);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.setBounds(238, 157, 64, 20);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.setBounds(110, 176, 64, 22);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.setBounds(174, 176, 64, 22);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.setBounds(238, 176, 64, 22);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.setBounds(110, 196, 64, 22);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.setBounds(174, 196, 64, 22);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.setBounds(238, 196, 64, 22);
		contentPane.add(btn9);
		
		JButton btnBack = new JButton("Back");
		btnBack.setBounds(110, 216, 64, 22);
		contentPane.add(btnBack);
		
		JButton btn0 = new JButton("0");
		btn0.setBounds(174, 216, 64, 22);
		contentPane.add(btn0);
		
		JButton btnEnter = new JButton("Enter");
		btnEnter.setBounds(238, 216, 64, 22);
		contentPane.add(btnEnter);
		BottomRight.addActionListener(e -> {
            JOptionPane.showMessageDialog(contentPane, "Hello!");
        });
	}
}
