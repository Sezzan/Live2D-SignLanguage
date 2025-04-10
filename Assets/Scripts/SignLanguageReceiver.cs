using UnityEngine;
using System.IO;

public class SignLanguageReceiver : MonoBehaviour
{
    public string receivedSign = "";
    private string filePath = "sign.txt";  // 檔案路徑
    private float updateInterval = 0.2f;   // 每 0.1 秒檢查一次
    private float timer = 0f;

    void Start()
    {
        // 確保檔案初始存在
        if (!File.Exists(filePath))
        {
            File.WriteAllText(filePath, "");
        }
    }

    void Update()
    {
        timer += Time.deltaTime;
        if (timer >= updateInterval)
        {
            timer = 0f;
            try
            {
                string sign = File.ReadAllText(filePath);
                if (sign != receivedSign)  // 只有當內容改變時更新
                {
                    receivedSign = sign;
                    Debug.Log("Received sign: " + receivedSign);
                }
            }
            catch (System.Exception e)
            {
                Debug.LogError("Error reading file: " + e.Message);
            }
        }
    }
}