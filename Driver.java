
import java.util.ArrayList;

public class Driver {

    public static void main(String[] args) {

	Search search = new Search(args[0]);

	ArrayList<String> order = search.BFS("s","g");
	System.out.println("BFS: " + order);

	order = search.DFS("s","g");
	System.out.println("DFS:    " + order);

	order = search.DFSrec("s","g");
	System.out.println("DFSrec: " + order);
    }
}
