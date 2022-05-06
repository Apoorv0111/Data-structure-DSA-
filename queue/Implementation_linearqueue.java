import java.util.*;

public class linearqueue{
	int size,front,rear;
	int arr[];
	public linearqueue(int s){
		size=s;
		front=0;
		rear=-1;
		arr=new int[size];
		System.out.println("created queue of size "+size);
	}
	public int push(int value){
		if(rear==size-1){
			System.out.println(rear+" "+(size-1));
			System.out.println("queue is full");
			return 0;
		}
		else{
			rear++;
			arr[rear]=value;
			System.out.println(value+" is added in queue");
			return 1;
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		linearqueue qu = new linearqueue(10);
		int x = sc.nextInt();
		System.out.println(x);

		
	}

}
