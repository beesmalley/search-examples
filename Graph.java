
import java.util.HashMap;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

/*
  for loading and visualizing graphs G = (V,E) stored in a CSV format.
  Graphs have vertices V with integer heuristic values h(v), for each
  v in V, and edges E with integer weights w(e), for each e in E
*/

public class Graph {

    private HashMap<String,Integer> h;

    public Graph(String filename) {

	h = new HashMap<String,Integer>();

	try {

	    BufferedReader reader = new BufferedReader(new FileReader(filename));

	    String line = reader.readLine();
	    String[] header = line.split(",");

	    assert header[0] == "v";
	    String es = header[1];
	    String orientation = header[2];

	    boolean heur = false;
	    if(header[1] == "h") {
		heur = true;

		es = header[2];
		orientation = header[3];
	    }
	}
	catch (IOException e) {
	    e.printStackTrace();
	}
    }
}
