using UnityEngine;
using System.IO;

public class SignLanguageReceiver : MonoBehaviour
{
    public string receivedSign = "";
    private string filePath = "sign.txt";  // �ɮ׸��|
    private float updateInterval = 0.2f;   // �C 0.1 ���ˬd�@��
    private float timer = 0f;

    void Start()
    {
        // �T�O�ɮת�l�s�b
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
                if (sign != receivedSign)  // �u�����e���ܮɧ�s
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