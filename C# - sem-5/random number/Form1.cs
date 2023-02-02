using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace random_number
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int a = 1,y;
            Random ran = new Random();
            listBox1.Items.Clear();
            while(a<10)
            {
                y = ran.Next(0, 20);
                listBox1.Items.Add(y);
                a++;
            }
        }
    }
}
