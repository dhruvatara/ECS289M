package com.example.myapplication;

import android.os.Bundle;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.util.Log;
import android.view.View;

import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;

import org.w3c.dom.Text;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        TextView displayNumber = findViewById(R.id.displayNumber);
        Button b1 = findViewById(R.id.button1);
        Button b2 = findViewById(R.id.button2);
        Button b3 = findViewById(R.id.button3);
        Button b4 = findViewById(R.id.button4);
        Button b5 = findViewById(R.id.button5);
        Button b6 = findViewById(R.id.button6);
        Button b7 = findViewById(R.id.button7);
        Button b8 = findViewById(R.id.button8);
        Button b9 = findViewById(R.id.button9);
        Button b0 = findViewById(R.id.button0);
        ImageButton bBack = findViewById(R.id.buttonBack);
        Button record = findViewById(R.id.buttonRec);

        b1.setOnClickListener(this);
        b2.setOnClickListener(this);
        b3.setOnClickListener(this);
        b4.setOnClickListener(this);
        b5.setOnClickListener(this);
        b6.setOnClickListener(this);
        b7.setOnClickListener(this);
        b8.setOnClickListener(this);
        b9.setOnClickListener(this);
        b0.setOnClickListener(this);
        bBack.setOnClickListener(this);
        record.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //TODO: Write code to set Flag
                //TODO: Change text to say stop recording- and unset flag if pressed even times
            }
        });
    }

    @Override
    public void onClick(View v) {
        TextView displayNumber = findViewById(R.id.displayNumber);
        //TODO: check if Flag set
        switch (v.getId()){
            case R.id.button0:
                displayNumber.setText("0");
                Log.i("press","0");
                break;
            case R.id.button1:
                displayNumber.setText("1");
                Log.i("press","1");
                break;
            case R.id.button2:
                displayNumber.setText("2");
                Log.i("press","2");
                break;
            case R.id.button3:
                displayNumber.setText("3");
                Log.i("press","3");
                break;
            case R.id.button4:
                displayNumber.setText("4");
                Log.i("press","4");
                break;
            case R.id.button5:
                displayNumber.setText("5");
                Log.i("press","5");
                break;
            case R.id.button6:
                displayNumber.setText("6");
                Log.i("press","6");
                break;
            case R.id.button7:
                displayNumber.setText("7");
                Log.i("press","7");
                break;
            case R.id.button8:
                displayNumber.setText("8");
                Log.i("press","8");
                break;
            case R.id.button9:
                displayNumber.setText("9");
                Log.i("press","9");
                break;
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }


        return super.onOptionsItemSelected(item);
    }
}