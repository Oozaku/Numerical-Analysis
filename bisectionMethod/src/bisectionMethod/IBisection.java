package bisectionMethod;

public interface IBisection {
	public boolean calculate(int max, double tolerance, double xi, double xf);
	public double getX();
	public double getError();
	public int getN();
}
