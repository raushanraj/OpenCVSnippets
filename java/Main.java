import org.opencv.core.*;
import org.opencv.highgui.*;
 
public class Main {
 
public static void main(String[] args)
       {
System.loadLibrary("opencv_java244");
   Mat m=Highgui.imread("C:/Users/raj/Desktop/sa1.png",Highgui.CV_LOAD_IMAGE_COLOR);
new LoadImage("C:/Users/raj/Desktop/dst1.jpg",m);
       }
       }
