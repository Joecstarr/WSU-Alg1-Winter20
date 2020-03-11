using System;
using System.Collections.Generic;
using System.Linq;
using System.Collections;


namespace sieveoferatosthenes
{
    class Program
    {
        Program(int low, int up)
        {
            for (int i = low; i <= up; i++)
            {
                listofstuff.Add(i, true);
            }

        }
        Program(int up)
        {
            for (int i = 2; i < up; i++)
            {
                listofstuff.Add(i, true);
            }
            
        }
        SortedDictionary<int, bool> listofstuff = new SortedDictionary<int, bool>();
        static void Main(string[] args)
        {
            int up = 200;
            Program initial = new Program(up);
            for (int i = 2; i < up; i++)
            {
                if (initial.listofstuff[i])
                    initial.seive(i, up);
            }
            //Console.WriteLine("\\begin{center}\n\\begin{tabular}{| c | c | c | c | c | c | c | c | c | c |}\n");
            //string table = " ";
            //for (int i = 2; i < up; i++)
            //{
            //    if (listofstuff[i])
            //        table += "$"+i+"$ ";
            //    else
            //        table += "$\\msout{" + i+"}$ ";
            //    if (i % 10 == 0)
            //        table += "\\\\\n\\hline\n";
            //    else
            //        table += "& ";
            //}
            //Console.WriteLine(table);
            //Console.WriteLine("\\end{tabular}\n\\end{center}\n");




            //SortedDictionary<int, List<int>> factors = new SortedDictionary<int, List<int>>();
            //factors.Add(35, new List<int>());
            //factors.Add(14, new List<int>());
            //factors.Add(15, new List<int>());
            //factors.Add(11, new List<int>());
            //factors.Add(252, new List<int>());
            //factors.Add(180, new List<int>());
            //factors.Add(7684, new List<int>());
            //factors.Add(4148, new List<int>());
            //factors.Add(6643, new List<int>());
            //factors.Add(2873, new List<int>());
            //foreach (KeyValuePair<int, List<int>> target in factors)
            //{
            //    int tk = target.Key;
            //    while (tk > 1)
            //    {
            //        foreach (KeyValuePair<int, bool> p in listofstuff)
            //        {
            //            if (p.Value)
            //            {
            //                if (tk % p.Key == 0)
            //                {
            //                    target.Value.Add(p.Key);
            //                    target.Value.Sort();
            //                    tk = (tk / p.Key);
            //                }
            //            }
            //        }
            //    }
            //}
            //foreach (KeyValuePair<int, List<int>> target in factors)
            //{
            //    Console.WriteLine("${0}: {1}$",target.Key, string.Join(",", target.Value.ToArray()));
            //}





            //SortedDictionary<int, List<int>> factors = new SortedDictionary<int, List<int>>();
            //for(int i = 2; i <= 20;i++)
            //{
            //    factors.Add(i,new List<int>());
            //}
            //foreach (KeyValuePair<int, List<int>> target in factors)
            //{
            //    int tk = target.Key;
            //    while (tk > 1)
            //    {
            //        foreach (KeyValuePair<int, bool> p in initial.listofstuff)
            //        {
            //            if (p.Value)
            //            {
            //                if (tk % p.Key == 0)
            //                {
            //                    target.Value.Add(p.Key);
            //                    target.Value.Sort();
            //                    tk = (tk / p.Key);
            //                }
            //            }
            //        }
            //    }
            //}
            //foreach (KeyValuePair<int, List<int>> target in factors)
            //{
            //    Program q2 = new Program(2, 20);
            //    string outstr = "";
            //    q2.seivesRelpri(20, target.Value);
            //    foreach (KeyValuePair<int, bool> indx in q2.listofstuff)
            //    {
            //        if (indx.Value)
            //            outstr +=  indx.Key +", ";
            //    }
            //    Console.WriteLine("\\item[${0}:$] ###${1}$^^^", target.Key, outstr);
            //
            //}

            SortedDictionary<int, List<int>> factors = new SortedDictionary<int, List<int>>();
            factors.Add(60, new List<int>());
            foreach (KeyValuePair<int, List<int>> target in factors)
            {
                int tk = target.Key;
                while (tk > 1)
                {
                    foreach (KeyValuePair<int, bool> p in initial.listofstuff)
                    {
                        if (p.Value)
                        {
                            if (tk % p.Key == 0)
                            {
                                target.Value.Add(p.Key);
                                target.Value.Sort();
                                tk = (tk / p.Key);
                            }
                        }
                    }
                }
            }
            foreach (KeyValuePair<int, List<int>> target in factors)
            {
                Program q2 = new Program(2, 60);
                string outstr = "";
                q2.seivesRelpri(60, target.Value);
                foreach (KeyValuePair<int, bool> indx in q2.listofstuff)
                {
                    if (indx.Value)
                        outstr += indx.Key + ", ";
                }
                Console.WriteLine("\\item[${0}:$] ###${1}$^^^", target.Key, outstr);

            }
        }
        void seive(int indx, int upbnd)
        {
            for (int i = 2; (i * indx) < upbnd; i++)
            {
                listofstuff[(i * indx)] = false;
            }
        }
        void seivesRelpri(int upbnd, List<int> primes)
        {
            foreach (int prime in primes)
            {
                for (int i = 2; (i * prime) <= upbnd; i++)
                {
                    listofstuff[(i * prime)] = false;
                }
            }

        }
    }



    /*
     * \begin{center}
\begin{tabular}{ c c c }
 cell1 & cell2 & cell3 \\ 
 cell4 & cell5 & cell6 \\  
 cell7 & cell8 & cell9    
\end{tabular}
\end{center}*/

}
