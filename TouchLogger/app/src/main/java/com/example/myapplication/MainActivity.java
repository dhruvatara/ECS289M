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


public class MainActivity extends AppCompatActivity implements View.OnClickListener{
    boolean recordFlag;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        recordFlag = false;
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
                if(recordFlag) {
                    recordFlag = false;
                    record.setText(R.string.rec);
                } else {
                    recordFlag = true;
                    record.setText(R.string.stoprec);
                }
            }
        });
    }

    @Override
    public void onClick(View v) {
        TextView displayNumber = findViewById(R.id.displayNumber);
        if(recordFlag) {
            String txt = (String) displayNumber.getText();
            switch (v.getId()) {
                case R.id.button0:
                    txt+="0";
                    displayNumber.setText(txt);
                    Log.i("press", txt);
                    break;
                case R.id.button1:
                    txt+="1";
                    displayNumber.setText(txt);
                    Log.i("press", txt);
                    break;
                case R.id.button2:
                    txt+="2";
                    displayNumber.setText(txt);
                    Log.i("press", txt);
                    break;
                case R.id.button3:
                    txt+="3";
                    displayNumber.setText(txt);
                    Log.i("press", txt);
                    break;
                case R.id.button4:
                    txt+="4";
                    displayNumber.setText(txt);
                    Log.i("press", txt);
                    break;
                case R.id.button5:
                    txt+="5";
                    displayNumber.setText(txt);
                    Log.i("press", txt);
                    break;
                case R.id.button6:
                    txt+="6";
                    displayNumber.setText(txt);
                    Log.i("press", txt);
                    break;
                case R.id.button7:
                    txt+="7";
                    displayNumber.setText(txt);
                    Log.i("press", txt);
                    break;
                case R.id.button8:
                    txt+="8";
                    displayNumber.setText(txt);
                    Log.i("press", txt);
                    break;
                case R.id.button9:
                    txt+="9";
                    displayNumber.setText(txt);
                    Log.i("press", txt);
                    break;
                case R.id.buttonBack:
                    txt = txt.substring(0,txt.length()-1);
                    displayNumber.setText(txt);
                    Log.i("press",txt);
                    break;
            }
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