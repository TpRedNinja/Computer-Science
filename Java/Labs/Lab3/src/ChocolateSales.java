public class ChocolateSales {
	// attributes
	private final double m_Price = 3.50;
	private final double m_StateTax = 0.06;
	private int m_Bars;
	
	// constructors
	ChocolateSales(){ // default constructor
		m_Bars = 0;
	}
	ChocolateSales(int bars){ // set bars constructor
		m_Bars = bars;
	}
	
	//methods
	public double getSubTotal() {
		double total = m_Bars * m_Price;
		return total;
	}
	
	public double calcDicount() {
		double subTotal = getSubTotal();
		double discount;
		double discountedPrice;
		if(m_Bars > 76) {
			discount = 0.2;
		} else if (m_Bars > 41 ) {
			discount = 0.15;
		} else if (m_Bars > 21) {
			discount = 0.1;
		} else if (m_Bars > 10) {
			discount = 0.05;
		} else {
			discount = 0.0;
		}
		
		discountedPrice = discount*subTotal;
		
		return discountedPrice;
	}
	
	public double getSalesTax() {
		double subTotal = getSubTotal();
		double salesTaxPrice = subTotal * m_StateTax;
		return salesTaxPrice;
	}
}
