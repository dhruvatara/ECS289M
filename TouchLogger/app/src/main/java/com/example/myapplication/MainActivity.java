package com.example.myapplication;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.os.Environment;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;

import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;


public class MainActivity extends AppCompatActivity implements View.OnTouchListener, SensorEventListener {
    boolean recordFlag;
    SensorManager sensorManager;
    Sensor gyroscope;
    long pressTime = -1l;
    long relTime = -1l;
    long gyroTime = -1l;
    File Path, buttonReadings,  gyroReadings;
    FileWriter buttonOutputStream, gyroOutputStream;
    String label = "", buttonEntry = "",gyroEntry = "";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        recordFlag = false;
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        TextView displayNumber = findViewById(R.id.displayNumber);
        sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        gyroscope = sensorManager.getDefaultSensor(Sensor.TYPE_GYROSCOPE);
        Path = new File(MainActivity.this.getFilesDir(),"readings");
        if(!Path.exists())
            Path.mkdir();
        buttonReadings = new File(Path,"button-readings.csv");
        gyroReadings = new File(Path,"gyro-readings.csv");

        if(!buttonReadings.exists()) {
            try {
                buttonReadings.createNewFile();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        if(!gyroReadings.exists()) {
            try {
                gyroReadings.createNewFile();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        try {
            buttonOutputStream = new FileWriter(buttonReadings,true);
            gyroOutputStream = new FileWriter(gyroReadings,true);
        } catch (Exception e) {
            e.printStackTrace();
        }

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

        b1.setOnTouchListener(this);
        b2.setOnTouchListener(this);
        b3.setOnTouchListener(this);
        b4.setOnTouchListener(this);
        b5.setOnTouchListener(this);
        b6.setOnTouchListener(this);
        b7.setOnTouchListener(this);
        b8.setOnTouchListener(this);
        b9.setOnTouchListener(this);
        b0.setOnTouchListener(this);
        bBack.setOnTouchListener(this);

        record.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(recordFlag) {
                    recordFlag = false;
                    record.setText(R.string.rec);
                    try {
                        buttonOutputStream.close();
                        gyroOutputStream.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                } else {
                    recordFlag = true;
                    record.setText(R.string.stoprec);
                    try {
                        buttonOutputStream = new FileWriter(buttonReadings,true);
                        gyroOutputStream = new FileWriter(gyroReadings,true);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            }
        });
    }

    @Override
    protected void onResume() {
        super.onResume();
        sensorManager.registerListener(this,gyroscope,SensorManager.SENSOR_DELAY_NORMAL);
    }

    @Override
    protected void onPause() {
        super.onPause();
        sensorManager.unregisterListener(this);
    }

    @Override
    public boolean onTouch(View v, MotionEvent event) {
        TextView displayNumber = findViewById(R.id.displayNumber);
        if(recordFlag) {
            String txt = (String) displayNumber.getText();
            if(event.getAction() == MotionEvent.ACTION_DOWN){
                pressTime = System.currentTimeMillis();
                switch (v.getId()) {
                    case R.id.button0:
                        txt+="0";
                        label = "0";
                        break;
                    case R.id.button1:
                        txt+="1";
                        label = "1";
                        break;
                    case R.id.button2:
                        txt+="2";
                        label = "2";
                        break;
                    case R.id.button3:
                        txt+="3";
                        label = "3";
                        break;
                    case R.id.button4:
                        txt+="4";
                        label = "4";
                        break;
                    case R.id.button5:
                        txt+="5";
                        label = "5";
                        break;
                    case R.id.button6:
                        txt+="6";
                        label = "6";
                        break;
                    case R.id.button7:
                        txt+="7";
                        label = "7";
                        break;
                    case R.id.button8:
                        txt+="8";
                        label = "8";
                        break;
                    case R.id.button9:
                        txt+="9";
                        label = "9";
                        break;
                    case R.id.buttonBack:
                        txt = txt.substring(0,txt.length()-1);
                        label = "b";
                        break;
                }
                displayNumber.setText(txt);
            } else if (event.getAction() == MotionEvent.ACTION_UP) {
                relTime = System.currentTimeMillis();
                buttonEntry = ""+pressTime+","+relTime+","+label+"\n";
                Log.i("entry",buttonEntry);
                try {
                    buttonOutputStream.append(buttonEntry);
                    buttonOutputStream.flush();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }


        }
        return false;
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        if(recordFlag) {
            gyroTime = System.currentTimeMillis();
            gyroEntry = "" + gyroTime + "," + event.values[0] + "," + event.values[1] + "," + event.values[2]+"\n";
            Log.i("gyro", "" + gyroEntry);
            try {
                gyroOutputStream.append(gyroEntry);
                gyroOutputStream.flush();
            } catch (IOException e) {
                Log.i("gyro", "onSensorChanged: error writing ");
                e.printStackTrace();
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