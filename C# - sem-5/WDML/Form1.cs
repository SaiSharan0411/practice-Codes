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

namespace WDML
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            SqlConnection con;
            SqlCommand cmd;

            con = new SqlConnection("Data source =UG153; Initial Catalog = master; User ID= sa; Password =loyola");
            cmd = new SqlCommand("Insert into Student (dno,name) values('" + textBox1.Text + "','" + textBox2.Text + "')", con);

            con.Open();
            cmd.ExecuteNonQuery();
            MessageBox.Show("Record Inserted");
            con.Close();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            SqlConnection con;
            SqlCommand cmd;

            con= new SqlConnection("Data Source = UG153; Initial Catalog = master; User ID= sa; Password =loyola");
            cmd = new SqlCommand("Delete from Student where dno= '" + textBox1.Text + "'", con);
            con.Open();
            cmd.ExecuteNonQuery();
            MessageBox.Show("Record Deleted");
            con.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection con;
            SqlCommand cmd;

            con = new SqlConnection("Data Source = UG153; Initial Catalog = master; User ID= sa; Password =loyola");
            cmd = new SqlCommand("Update Student set dno= '" + textBox1.Text + "' where name= '" + textBox2.Text +"'", con);
            con.Open();
            cmd.ExecuteNonQuery();
            MessageBox.Show("Record Updated");
            con.Close();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
