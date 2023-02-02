using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace dynamic_arrays
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            int[] scores = new int[2];
            scores[0] = 100;
            scores[1] = 200;
            for(i=0;i<=scores.Length-1; i++)
            {
                MessageBox.Show("scores :" + scores[i]);
            }
            Array.Resize(ref scores, 3);
            scores[2] = 300;
            for(i=0;i<=scores.Length-1; i++)
            {
                MessageBox.Show("new.Scores: " + scores[i]);
            }
        }
    }
}
