/*import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.SwingUtilities;*/
import javax.swing.*;

public class TestGUI {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame window = new JFrame("My First GUI");

            window.setSize(500, 350);
            window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            JButton button = new JButton("Click Me!");
            window.add(button);

            window.setLocationRelativeTo(null);
            window.setVisible(true);
            button.addActionListener(e -> {
                JOptionPane.showMessageDialog(window, "Hello!");
            });
        });
    }
}
