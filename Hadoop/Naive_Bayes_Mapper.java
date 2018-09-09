import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;
import java.io.IOException;

public class Naive_Bayes_Mapper extends Mapper<Object, Text, Text, IntWritable> {
//    private RecordParser recordParser = new RecordParser();

    private final static IntWritable one = new IntWritable(1);

    @Override
    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
        // System.out.println("LOG: "+value);
        RecordParser recordParser = new RecordParser();
        String line = value.toString();
        recordParser.Parse(line);
        String[] labels = recordParser.getLabels();

        String document = recordParser.getDoc();

        StringTokenizer itr = new StringTokenizer(document, " ");
        for (String label : labels) {
            context.write(new Text("1=Y="+label.trim()), one);
            context.write(new Text("2=Y=ANYTITLE"), one);
            while (itr.hasMoreTokens()) {
                String nxtToken=itr.nextToken();
                if (!RecordParser.stopWordSet.contains(nxtToken.trim())){
                    context.write(new Text("3=Y="+label.trim()+"="+nxtToken.trim()), one);
                    context.write(new Text("4=X="+nxtToken.trim()),one);
                    context.write(new Text("5=Y="+label.trim()+"=ANYWORD"), one);

                }

            }

        }
    }
}
