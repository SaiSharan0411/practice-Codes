using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace calculator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        int a;
        char o;
        private void button1_Click(object sender, EventArgs e)
        {
            textBox1.AppendText("1");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.AppendText("2");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            textBox1.AppendText("3");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            textBox1.AppendText("4");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            textBox1.AppendText("5");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            textBox1.AppendText("6");
        }

        private void button7_Click(object sender, EventArgs e)
        {
            textBox1.AppendText("7");
        }

        private void button8_Click(object sender, EventArgs e)
        {
            textBox1.AppendText("8");
        }

        private void button9_Click(object sender, EventArgs e)
        {
            textBox1.AppendText("9");
        }

        private void button11_Click(object sender, EventArgs e)
        {
            textBox1.AppendText("0");
        }

        private void button10_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            textBox1.AppendText(".");
        }

        private void button13_Click(object sender, EventArgs e)
        {
            string s1;
            s1 = textBox1.Text;
            {
                if ((s1.Length > 0))
                    textBox1.Text = s1.Substring(0, s1.Length-1);
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            switch(o)
            {
                case '+':
                    {
                        textBox1.Text = Convert.ToString(a + Convert.ToInt32(textBox1.Text));
                        break;
                    } 
                case '-':
                    {
                        textBox1.Text = Convert.ToString(a - Convert.ToInt32(textBox1.Text));
                        break;
                    }
                case '*':
                    {
                        textBox1.Text = Convert.ToString(a * Convert.ToInt32(textBox1.Text));
                        break;
                    }
                case '/':
                    {
                        textBox1.Text = Convert.ToString(a / Convert.ToInt32(textBox1.Text));
                        break;
                    }
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            a = int.Parse(textBox1.Text);
            o = '+';
            textBox1.Clear();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            a = int.Parse(textBox1.Text);
            o = '-';
            textBox1.Clear();
        }

        private void button17_Click(object sender, EventArgs e)
        {
            a = int.Parse(textBox1.Text);
            o = '*';
            textBox1.Clear();
        }

        private void button18_Click(object sender, EventArgs e)
        {
            a = int.Parse(textBox1.Text);
            o = '/';
            textBox1.Clear();
        }
    }
}
