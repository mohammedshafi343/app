// MultiThreadDemo.java
class MultiThreadDemo implements Runnable {
    private String threadName;

    MultiThreadDemo(String name) {
        threadName = name;
    }

    public void run() {
        try {
            for (int i = 4; i > 0; i--) {
                System.out.println("Thread: " + threadName + ", " + i);
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
            System.out.println("Thread " + threadName + " interrupted.");
        }
        System.out.println("Thread " + threadName + " exiting.");
    }
}

// Usage
public class TestThread {
    public static void main(String args[]) {
        Thread t1 = new Thread(new MultiThreadDemo("Thread-1"));
        Thread t2 = new Thread(new MultiThreadDemo("Thread-2"));
        
        t1.start();
        t2.start();
    }
}
