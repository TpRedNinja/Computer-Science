public class SurfaceArea {
	
	private final int sphereNum = 4;
	private final int rectPrismNum = 2;
	
	//sphere calculate surface area
	public double calSurfArea(double r) {
		double surfaceArea;
		surfaceArea = 4*Math.PI*Math.pow(r,2);
		
		return surfaceArea;
	}
	//cone calculate surface  area
	public double calSurfArea(double r, double h) {
		double surfaceArea;
		surfaceArea = Math.PI*r*(r+Math.sqrt(Math.pow(r, 2)+Math.pow(h, 2)));
		
		return surfaceArea;
	}
	// rectangular prism calculate surface area
	public double calSurfArea(double l, double h, double b) {
		double surfaceArea;
		double val1 = l*b;
		double val2 = b*h;
		double val3 = h*l;
		
		surfaceArea = 2*(val1+val2+val3);
		
		return surfaceArea;
	}
}
