using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace arithmetic
{
    public partial class Form1 : Form
    {
        int a, b;
        public Form1()
        {
            InitializeComponent();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            a = int.Parse(txt_first.Text);
            b = int.Parse(txt_second.Text);
            txt_result.Text = Convert.ToString(a + b);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            a = int.Parse(txt_first.Text);
            b = int.Parse(txt_second.Text);
            txt_result.Text = Convert.ToString(a - b);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            a = int.Parse(txt_first.Text);
            b = int.Parse(txt_second.Text);
            txt_result.Text = Convert.ToString(a * b);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            a = int.Parse(txt_first.Text);
            b = int.Parse(txt_second.Text);
            txt_result.Text = Convert.ToString(a / b);
        }
        private void button5_click(object sender, EventArgs e)
        {
                txt_first.Clear();
                txt_second.Clear();
                txt_result.Clear();
            }
        }
    }

