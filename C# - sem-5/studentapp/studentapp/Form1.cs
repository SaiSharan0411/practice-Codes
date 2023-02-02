using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace studentapp
{
    public partial class Form1 : Form
    {
        string name;
        string gender;
        string qualification;
        string food;
        string hobbies;

        public Form1()
        {
            InitializeComponent();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(textBox1.Text))
            {
                textBox1.Focus();
                MessageBox.Show("Enter Name");
                return;
            }

            else
            {
                name += textBox1.Text;
            }
            if (string.IsNullOrEmpty(Convert.ToString(comboBox1.SelectedItem)))
            {
                MessageBox.Show("Choose gender");
                return; 
            }
            else
                gender = Convert.ToString(comboBox1.SelectedItem);

            if (string.IsNullOrEmpty(Convert.ToString(checkedListBox1.SelectedItem)))
            {
                MessageBox.Show("Choose qualification");
                return;
            }
            else
                qualification = Convert.ToString(checkedListBox1.SelectedItem);

            if (!(radioButton1.Checked | radioButton2.Checked | radioButton3.Checked))
            {
                MessageBox.Show("select food");
                return;
            }
            else

                if (radioButton1.Checked)
            {
                food = "veg";
            }
            else if (radioButton2.Checked)
            {
                food = "non-veg";
            }
            else
                food = "both";

            if (string.IsNullOrEmpty(textBox2.Text))
            {
                textBox2.Focus();
                MessageBox.Show("Enter hobby");
                return;
            }

            else
            {
                hobbies += textBox2.Text;
            }
            textBox3.Text = ("name:" + textBox1.Text + "\r\nGender:" + comboBox1.SelectedItem + "\r\nQualification:" + checkedListBox1.SelectedItem + "\r\nFood:" + food + "\r\nHobbies:" + textBox2.Text);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Clear();
            comboBox1.ResetText();
            textBox2.Clear();
            textBox3.Clear();
            checkedListBox1.ClearSelected();
        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }
    }
}