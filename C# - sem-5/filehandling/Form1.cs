using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace filehandling
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            FileStream fs = new FileStream("Text1.txt", FileMode.Open);
            int i;
            string str = " ";
            i = fs.ReadByte();
            while (i != -1)
            {
                str += Convert.ToChar(i);
                i = fs.ReadByte();
            }
            fs.Close();
            textBox1.Text = str;
        }
    }
}
