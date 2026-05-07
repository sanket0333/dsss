'''Yes 👍 — your steps are **almost perfectly correct**, and yes 👉 **all these commands are run in the Ubuntu terminal**.

But I’ll fix a couple of **important small mistakes** so it works **without errors 💯**

---

# ✅ ANSWER TO YOUR QUESTION

👉 **“All this is to put in terminal?”**
✔ YES — every command you wrote goes in **Terminal (Ctrl + Alt + T)**

---

# ⚠️ SMALL CORRECTIONS (IMPORTANT)

## ❌ Problem 1: `scalac` may not work

👉 You didn’t install Scala compiler

### ✅ Fix:

```bash
sudo apt install scala -y
```

---

## ❌ Problem 2: Running Spark program

You wrote:

```bash
spark-submit SparkExample
```

👉 ❌ This is WRONG

---

## ✅ Correct command:

```bash
spark-submit SparkExample.scala
```

✔ No need to compile
✔ Best method

---

# ✅ FINAL CORRECT STEPS (CLEAN VERSION)

## 🔹 Step 1: Install Java

```bash
sudo apt update
sudo apt install openjdk-11-jdk -y
```

---

## 🔹 Step 2: Download Spark

```bash
wget https://downloads.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
```

---

## 🔹 Step 3: Extract

```bash
tar -xvzf spark-3.5.1-bin-hadoop3.tgz
sudo mv spark-3.5.1-bin-hadoop3 /opt/spark
```

---

## 🔹 Step 4: Set Environment

```bash
nano ~/.bashrc
```

Add:

```bash
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

Then:

```bash
source ~/.bashrc
```

---

## 🔹 Step 5: Check Spark

```bash
spark-shell
```

👉 If `scala>` comes → OK ✅

---

# 🧑‍💻 RUN YOUR PROGRAM

## 🔥 BEST METHOD (Use this)

```bash
cd your-folder
ls
spark-submit SparkExample.scala
```

---

# ❌ OPTIONAL (only if you want compile)

```bash
sudo apt install scala -y
scalac SparkExample.scala
spark-submit SparkExample
```

'''

import org.apache.spark.sql.SparkSession 
 
object SparkExample { 
  def main(args: Array[String]): Unit = { 
     
    // Step 1: Initialize Spark Session 
    val spark = SparkSession.builder() 
      .appName("Simple Spark Program") 
    
 
 
      .config("spark.master", "local") 
      .getOrCreate() 
 
    // Step 2: Load data from a CSV file into a DataFrame 
    val df = spark.read.option("header", "true").csv("data/people.csv") 
 
    // Step 3: Show the first few rows of the DataFrame 
    df.show() 
 
    // Step 4: Perform a simple transformation and action 
    val ageData = df.filter(df("age") > 30).select("name", "age") 
     
    // Step 5: Show the filtered results 
    ageData.show() 
 
    // Step 6: Group by and Aggregate Data 
    val avgAge = df.groupBy("department").avg("age") 
    avgAge.show() 
 
    // Stop the Spark session 
    spark.stop() 
  } 
}'''Example Input (people.csv): 
name,age,department 
Alice,30,HR 
Bob,35,Engineering 
Charlie,40,Engineering 
David,50,HR 
Eve,28,Marketing'''