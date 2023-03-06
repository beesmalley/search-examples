
import java.util.HashMap;
import java.util.ArrayList;
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
    private HashMap<String,ArrayList<String>> N;

    public Graph(String filename) {

	h = new HashMap<String,Integer>();
	N = new HashMap<String,ArrayList<String>>();

	try {

	    BufferedReader reader = new BufferedReader(new FileReader(filename));

	    // process header

	    String line = reader.readLine();
	    String[] s = line.split(",");

	    assert s[0].equals("v");
	    String es = s[1];
	    String orientation = s[2];

	    boolean heur = false;
	    if(s[1].equals("h")) {
		heur = true;

		es = s[2];
		orientation = s[3];
	    }

	    assert es.equals("es");

	    boolean undir = false;
	    if(orientation.equals("undir"))
		undir = true;
	    else
		assert orientation.equals("dir");

	    // process remaining lines

	    String v;
	    int i;
	    line = reader.readLine();
	    while(line != null) {

		s = line.split(",");
		v = s[0];

		i = 1;
		if(heur) {
		    h.put(v, Integer.valueOf(s[1]));
		    ++i;
		}

		System.out.print(v + ": ");
		N.put(v, new ArrayList<String>());
		while(i < s.length) {
		    System.out.print("," + s[i]);
		    ++i;
		}
		System.out.println();
		
		// next line
		line = reader.readLine();
	    }

	}
	catch (IOException e) {
	    e.printStackTrace();
	}

	System.out.println(h);

    }   
}
