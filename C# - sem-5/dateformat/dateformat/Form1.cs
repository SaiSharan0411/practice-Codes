using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace dateformat
{
    public partial class Form1 : Form
    {
        DateTime theDate;
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {
            theDate =System.DateTime.Now;
            label1.Text = Convert.ToString(theDate);
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            label2.Text = theDate.ToLongDateString();
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            label2.Text = theDate.ToShortDateString();
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            label2.Text = Convert.ToString(theDate.Month);
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}
