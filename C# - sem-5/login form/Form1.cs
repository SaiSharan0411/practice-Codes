using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace login_form
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection conn;
            SqlCommand cmd;
            string password;
            if(string.IsNullOrEmpty(textBox1.Text) | string.IsNullOrEmpty(textBox2.Text))
            {
                return;
            }
            conn = new SqlConnection("Data Source = UG164; Initial Catalog=master; User ID =sa; Password=loyola");
            cmd = new SqlCommand("Select username from login where password='" + textBox1.Text + "'", conn);
            conn.Open();
            password = Convert.ToString(cmd.ExecuteScalar());
            if (password==textBox2.Text)
            {
                MessageBox.Show("correct username & password");
                Form2 f2 = new Form2();
            }
            else
            {
                label3.Text = "Username and Password dosen't match";
                textBox1.Text = " ";
                textBox2.Text = " ";
            }
            conn.Close();
        }
    }
}
