package bisectionMethod;
public class Bisection implements IBisection{
	private int n;
	private double X;
	private double error;
	public Bisection() {
		n = 0;
		
	}
	private double equationF(double t){
		return Math.exp(0.2 * t) - Math.exp(-0.8*t) - 2;
	}
	
	private double modulo(double t) {
		double out = t;
		if ( t < 0 )
			out = - t;
		return out;
	}
	public boolean calculate(int max, double tolerance, double xi, double xf) {
		boolean out = true;
		error = modulo( xf - xi );
		while ( modulo(xf - xi) > tolerance ) {
			n++;
			if (n > max)
				out = false;
			X = (xf + xi) / 2;
			if ((equationF(xi) * equationF(X)) < 0)
				xf = X;
			else
				xi = X;
			error = modulo( xf - xi );
		}
		return out;
	}
	public double getX() {
		return X;
	}
	public double getError() {
		return error;
	}
	public int getN() {
		return n;
	}
	public String toString() {
		return "x = " + X + "\n" + n + " iterations";
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		IBisection novo = new Bisection();
		novo.calculate(40, 0.0001, -500, 1000);
		System.out.println(novo);
		System.out.println("Aproximation error = " + novo.getError());
	}

}
