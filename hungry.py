print('I am hungry')

print('very good')
# //package com.company;
# //
# //import java.util.*;
# //
# //public class Main{
# //    public static void main(String[] args) {
# //        System.out.println("hello world");
# //
# //        int x= 34;
# //        int y= 74;
# //        int sum = x+y ;
# //        System.out.println("sum of "+ x +" and "+y+" is "+sum);
#         // */amd % priority same from left to right
#         // + and - also same priority
# //        int x = 11;
# //        if( x % 2 == 0)
# //        {
# //            System.out.println(x +" is even");
# //        }
# //        else
# //        {      System.out.println(x +" is odd");
# //
# //        }
# //            System.out.println(x +" hard work is good");
# //        int n1 =20;
# //        int n2 = 30;
# //        if(n1==n2){
# //            System.out.println(n1+ " is equal to "+ n2 );
# //        }
# //        else{
# //            if(n1>n2){
# //                System.out.println(n1+ " is greater than "+ n2 );
# //
# //            }
# //            else{
# //                System.out.println(n1+ " is less than "+ n2 );
# //
# //            }
# //
# //        }
# //        int n1 =30;
# //        int n2 = 30;
# //        if(n1==n2){
# //            System.out.println(n1 + " is equal to" + n2);
# //        }
# //        else if(n1 >n2){
# //            System.out.println(n1 + " is greater to" + n2);
# //        }
# //        else{
# //            System.out.println(n1 + " is less to" + n2);
# //
# //        }
# //        Scanner scn = new Scanner(System.in);
# //        int marks = scn.nextInt();
# //        if(marks>90){
# //            System.out.println("excellent");
# //        }
# //        else if (marks>80  ){
# //            System.out.println("good");
# //        }
# //        else if(marks>70){
# //            System.out.println("fair");
# //        }
# //        else if(marks>60){
# //            System.out.println("meets expectation");
# //        }
# //        else{
# //            System.out.println("below par");
# //        }
#
#
#
#
#
# //        }
# //}
#
# //while loop lecture 8
# //package com.company;
# //
# //        import java.util.*;
# //
# //public class Main{
# //    public static void main(String[] args){
# ////        int i=1;
# ////        while (i<=9) {
# ////            System.out.println(i);
# ////            i++;
# ////        }
# //
# //        for(int i= 1; i<= 9; i++) {
# //            System.out.println(i);
# //i=1 then check then print then increament
# //i=2 then check then print then increament
# //i=3 then check then print then increament
# //        }
# //        System.out.println("done");
# //    }
# //
# //}
# //package com.company;
# //
# //        import java.util.*;
# //
# //public class Main{
# //    public static void main(String[] args) {
# //        Scanner scn = new Scanner(System.in);
# //        int n = scn.nextInt();
# //        for (int i = 0; i <= n; i++) {
# //            System.out.println(i);
# //        }
# //        String name = scn.nextLine();
# //        System.out.println("hello " + name);
# //    }
# //}
# //package com.company;
# //
# //        import java.util.*;
# //
# //public class Main {
# //    public static void main(String[] args) {
# //        Scanner scn = new Scanner(System.in);
# //        int n = Integer.parseInt(scn.nextLine());
# //        String name = scn.nextLine();
# //        System.out.println("dear " + name + ".here is the counting");
# //        for (int i = 1; i <= n; i++) {
# //            System.out.println(i);
# //        }
# //    }
# //}
# //prime number checking
# //package com.company;
# //
# //        import java.util.*;
# //
# //public class Main{
# //    public static void main(String[] args) {
# //        Scanner scn= new Scanner(System.in);
# //        int t = scn.nextInt();
# //        for( int i=1;i<=t;i++) {
# //          int n= i;
# //
# //           int count =0;
# //           for(int div =1; div<=n; div++){
# //                if (n % div == 0){
# //                    count++;
# //                }
# //            }
# //               if (count==2){
# //                   System.out.println("prime no");
# //               }
# //               else{
# //                System.out.println(" not prime no");
# //
# //            }
# //
# //        System.out.println(n);
# //            System.out.println("for"+ n );
# //        }
# //    }
# //}
# //        time complexity
# //package com.company;
# //
# //        import java.util.*;
# //
# //public class Main {
# //        public static void main(String[] args) {
# //
# //    Scanner scn = new Scanner(System.in);
# //        int t = scn.nextInt();
# //        for(int i = 1; i<=t;i++){
# //        int n = i;
# //
# //        int count = 0;
# //        for (int div = 2; div * div <= n; div++) {
# //            if (n % div == 0) {
# //                count++;
# //                break;
# //            }
# //        }
# //        if (count == 0) {
# //            System.out.println(n + "prime no");
# //        } else {
# //            System.out.println(n +" not prime no");
# //
# //        }
# //    }
# //    }
# //    }
#
# //        Scanner scn = new Scanner(System.in);
# //        int l = scn.nextInt();
# //        int h = scn.nextInt();
# //        for (int i = l; i <= h; i++) {
# //            int count = 0;
# //            for (int div = 2; div * div <= i; div++) {
# //                if (i % div == 0) {
# //                    count++;
# //                    break;
# //                }
# //            }
# //            if (count == 0) {
# //                System.out.println(i);
# //            }
# ////        }
# ////
# //        }
# //
# //    }
# //}
# //fibonacci series
# //package com.company;
# //        import java.util.*;
# //        public class Main{
# //            public static void main(String[] args) {
# //                Scanner scn= new Scanner(System.in);
# //                int n= scn.nextInt();
# //                int a=0;
# //                int b=1;
# //                for(int i=0 ; i <n; i++){
# //                    System.out.println(a);
# //                    int c= a+b;
# //                    a=b;
# //                    b=c;
# //                }
# //            }
# //        }
# //digits of number
# //package com.company;
# //        import java.util.*;
# //        public class Main{
# //            public static void main(String[]args){
# //                Scanner scn= new Scanner(System.in);
# //                int n= scn.nextInt();
# //                int dig=0;
# //                while(n!=0){
# //                    n= n/10;
# //                    dig++;
# //                }
# //                System.out.println(dig);
# //            }
# //        }
# //actual digits of a number
# //package com.company;
# //import java.util.*;
# //public class Main {
# //    public static void main(String[]args){
# //        Scanner scn = new Scanner(System.in);
# //        int n= scn.nextInt();
# //        int nod= 0;
# //        int temp= n;
# //        while(temp!=0){
# //            temp= temp/10;
# //            nod++;
# //        }
# //        int div= (int)Math.pow(10,nod -1);
# //        while(div!=0){
# ////                this is perfectly fine check it again
# //            int q= n/div;
# //            System.out.println(q);
# //            n= n%div;
# //            div= div/10;
# //        }
# //    }
# //}
#
# //package com.company;
# //        import java.util.*;
# //public class Main {
# //    public static void main(String[]args){
# //        Scanner scn = new Scanner(System.in);
# //        int n= scn.nextInt();
# //        int nod= 0;
# //        int temp= n;
# //        while(temp!=0){
# //            temp= temp/10;
# //            nod++;
# //        }
# //        int div= (int)Math.pow(10,nod -1);
# //        while(n!=0){
# ////            this have a problem check kit again
# //            int q= n/div;
# //            System.out.println(q);
# //            n= n%div;
# //            div= div/10;
# //        }
# //    }
# //}Reverse a digit of a number
# //package com.company;
# //import java.util.*;
# //public class Main{
# //    public static void main(String[]args){
# //        Scanner scn= new Scanner(System.in);
# //     int t= scn.nextInt();
# //
# //        while (t!=0) {
# //            int value = t % 10;
# //            System.out.println(value);
# //            t=t/10;
# //        }
# //
# //     }
# //    }
# //inverse a number
# //package com.company;
# //import java.util.*;
# //public class Main{
# //    public static void main(String[]args){
# //        Scanner scn= new Scanner(System.in);
# //        int n= scn.nextInt();
# //        int inv =0;//to make inverse
# //        int op= 1;//original digit
# //        while (n!=0){
# //            int od = n%10;//original place, inverted place , inverted place
# //            int ip= od;
# //            int id= op;
# //            inv= inv+ id* (int)Math.pow(10,ip-1);
# //
# //            n=n/10;
# //            op++;
# //        }
# //        System.out.println(inv);
# //    }
# //}
# //rotate a number n=12345,k=3-->n=34512 if k=-3 then n= 45123 and 6=1,7=2 and
# //soo on for k/...
# //package com.company;
# //
# //import java.util.*;
# //
# //public class Main{
# //    public static void main(String[]args) {
# //        Scanner scn = new Scanner(System.in);
# //        int n = scn.nextInt();
# //        int k = scn.nextInt();
# //        int temp= n;
# //        int nod= 0;
# //        while(temp!=0) {
# //            temp = temp / 10;
# //            nod++;
# //        }
# //        // LEAVE FROM THIS BELOW TO UNTIL CALLED
# //        k= k % nod;
# //        // means 352 is k then means that only 2 rotations cuz 350
# ////        is a multiple of 5 ie nod
# //        if(k<0){
# //            k= k + nod;
# //        }
# //        //YES YOU ARE CALLED NOW AND THIS WAS DONE AT THE LAST
# ////        IN ACTUAL CODE FOR HANDELING -VE VALUES AND GREATER VELUES THAN
# ////        THE NUMBER N ...
# //
# //
# //        // make a divisor and mulitplier like if k = 2 then miultilpier
# ////        is 100 and divisor is 1000 for a number 35618
# //        int div=1;
# //        int mult =1;
# //        for(int i=1;i<=nod;i++){
# //            if(i<=k){
# //                div= div * 10;
# //            }
# //            else{
# //                mult = mult * 10;
# //            }
# ////example := we have number as 25398 so for k=2 divisor is 100
# ////            multiplier is 1000 remainder = 98, and quotient= 253
# //        }
# //        int quotient= n/ div;
# //        int remainder = n% div;
# //        int rotated = remainder* mult + quotient;
# //         System.out.println(rotated);
# //    }
# //}
#
# //GCD and LCM
# //package com.company;
# //
# //import java.util.*;
# //
# //public class Main {
# //    public static void main(String[] args) {
# //
# //        Scanner scn = new Scanner(System.in);
# //        int n1= scn.nextInt();
# //        int n2= scn.nextInt();
# //
# //        int on1 = n1;
# //        int on2 = n2;
# //        while(n1% n2 !=0){
# //        int rem = n1 % n2;
# //        n1 = n2;
# //        n2 = rem;
# //        }
# //        int gcd = n2;
# //        int lcm = (on1 *   on2)/ gcd;
# //        System.out.println(gcd);
# //        System.out.println(lcm);
# //
# //    }
# //}
#
# //prime factorization
#
# //package com.company;
# //
# //        import java.util.*;
# //
# //public class Main {
# //    public static void main(String[] args) {
# //        Scanner scn = new Scanner(System.in);
# //        int n = scn.nextInt();
# //
# //        for (int div = 2; div * div <= n; div++) {
# //            while (n % div == 0) {
# //                n = n / div;
# //                System.out.print(div + " ");
# //            }
# //        }
# //        if( n != 1){
# //            System.out.print(n);
# //
# //        }
# //    }
# //}
#
#
# //package com.company;
# //
# //        import java.util.*;
# //
# //public class Main {
# //    public static void main(String[] args) {
# //        Scanner scn = new Scanner(System.in);
# //        int a = scn.nextInt();
# //        int b = scn.nextInt();
# //        int c = scn.nextInt();
# //        int max = a;
# //        if(b >= max){
# //            max = b;
# //        }
# //        if(c >= max ){
# //            max = c;
# //        }
# //        if ( max == a){
# //            boolean flag =( (b*b +c*c) == (a*a) );
# //            System.out.println(flag);
# //
# //        }else if (max == b){
# //            boolean flag =( (a*a + c*c) == (b*b) );
# //            System.out.println(flag);
# //        }else {
# //            boolean flag =( (a*a + b*b) == (c*c) );
# //            System.out.println(flag);
# //        }
# //
# //    }
# //}
#
# //Benjamin bulb
#
# //package com.company;
# //
# //        import java.util.*;
# //
# //public class Main {
# //    public static void main(String[] args) {
# ////        all perfect squares have odd number of factors
# ////        all even is off and all odd is on
# //        Scanner scn = new Scanner(System.in);
# //        int n = scn.nextInt();
# //
# //        for (int i= 1; i * i <= n ; i++){
# //            System.out.println( i * i );
# //        }
# //
# //    }
# //
# //}
#
# //pattern 1
# //package com.company;
# //
# //        import java.util.*;
# //
# //public class Main {
# //    public static void main(String[] args) {
# //// abstraction means i am layering my thinking
# ////when thinking of outer loop have believe in inner loop
# //        Scanner scn = new Scanner(System.in);
# //        int n= scn.nextInt();
# //        for(int i=1 ;i <=n; i++){
# //            for( int j=1; j <= i ; j++){
# //                System.out.print("*\t");
# //            }
# //            System.out.println();
# //        }
# //    }
# //}
# //pattern 2
# //package com.company;
# //
# //        import java.util.*;
# //
# //public class Main {
# //    public static void main(String[] args) {
# //        Scanner scn = new Scanner(System.in);
# //        int n= scn.nextInt();
# //        for(int i=n ;i >=1; i--){
# //            for( int j=1; j <=i ; j++){
# //                System.out.print("*\t");
# //            }
# //            System.out.println();
# //        }
# //    }
# //}
#
# //pattern 3
# package com.company;
#
#         import java.util.*;
#
# public class Main {
#     public static void main(String[] args) {
#         Scanner scn = new Scanner(System.in);
#         int n = scn.nextInt();
#
#         int sp = n - 1;
#         int st = 1;
#
# //            System.out.print(sp + ","+ st);
#         for (int i = 1; i <= n; i++) {
#             for (int j = 1; j <= sp; j++) {
#                 System.out.print("\t");
#             }
#             for (int j = 1; j <= st; j++) {
#                 System.out.print("*\t");
#             }
#             sp--;
#             st++;
#             System.out.println();
#         }
#     }
# }