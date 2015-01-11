import java.util.Random;

class MonteCarloPiFinder implements Runnable {
    //Instance variable number of samples.
    int N;
    
    //Class variable each instance has access to.
    static volatile double pi; 
    
    // Constructor setting number of samples for a particular PiFinder
    MonteCarloPiFinder(int n) {
        N = n;    
    }

    @Override
    public void run() {            
        double res = getPi();
        pi += res;
        //System.out.println("done: "+res+", total: "+pi); //checking behaviour.

    }
    
    //MonteCarlo algorithm
    public double getPi() {        
        Random r = new Random();
        double x, y, Lpi;
        Lpi = 0;
        for (int i = 0; i < N; i++) {
            x = r.nextDouble();
            y = r.nextDouble();
            if (x * x + y * y <= 1) {
                Lpi += 1;
            }
        }
        return 4.0 * Lpi / N;

    }

    public static void main(String args[]) throws Exception {
        //Get thread no. and sample no. from command line
        int ThreadNum = Integer.parseInt(args[0]);     
        int SampleNum = Integer.parseInt(args[1]);
        
        //Start timing.
        long t1 = System.currentTimeMillis();
        
        //Create thread array, fill with PiFinders and start them off.
        Thread[] finders = new Thread[ThreadNum];       
        for (int i = 0; i < ThreadNum; i++) {                       
            finders[i] = new Thread(new MonteCarloPiFinder(SampleNum));   
            finders[i].start();
        }
        
        //Tell each thread to block the main thread until they are finished.
        for (Thread finder : finders) {         
            finder.join();
        }
        
        //Finish Timing
        long t2 = System.currentTimeMillis();
        
        System.out.println("Time taken in milliseconds: "+ (t2 - t1));
        System.out.println("Estimate: " + pi / ThreadNum);

        pi = 0;
        
        //Time doing everything in one thread.
        t1 = System.currentTimeMillis();
        Thread soloFinder = new Thread(new MonteCarloPiFinder(SampleNum * ThreadNum));
        soloFinder.start();
        soloFinder.join();
        t2 = System.currentTimeMillis();
        
        System.out.println("Time taken in milliseconds :"+ (t2 - t1));
        System.out.println("Estimate: " + pi );

    }
}
