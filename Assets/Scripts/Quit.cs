
using UnityEditor;
using UnityEngine;

public class Quit : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown("escape"))
        {
            Debug.Log("quit");
            Application.Quit(); //關閉應用程式
        }
    }
}
