using UnityEngine;
using UnityEngine.SceneManagement;
using System.Diagnostics;
using System.Collections.Generic;
using System.Collections;  

public class MainSceneController : MonoBehaviour
{
    public MotionPlayer motionPlayer;  // 引用 Live2D 模型的 MotionPlayer 組件
    public AnimationClip[] motionClips;  // 動畫列表，對應詞彙
    private Dictionary<string, AnimationClip> signToMotionMap;  // 詞彙到動畫的映射

    private List<string> signWords = new List<string> { "我", "刷牙", "穿衣服", "讀書", "開心", "懶惰", "我讀書", "懶得刷牙" };  // 詞彙列表
    private List<string> practiceWords = new List<string> { "我讀書", "懶得刷牙" };  // 需要練習的詞彙

    void Start()
    {
        // 初始化詞彙到動畫的映射
        signToMotionMap = new Dictionary<string, AnimationClip>();
        for (int i = 0; i < signWords.Count && i < motionClips.Length; i++)
        {
            signToMotionMap[signWords[i]] = motionClips[i];
        }
    }

    // 點擊詞彙按鈕時調用
    public void OnSignButtonClicked(string signWord)
    {
        // 播放 Live2D 動畫
        if (signToMotionMap.ContainsKey(signWord))
        {
            AnimationClip clip = signToMotionMap[signWord];
            motionPlayer.PlayMotion(clip);
            UnityEngine.Debug.Log($"Playing motion for: {signWord}, duration: {clip.length} seconds");
        }
        else
        {
            UnityEngine.Debug.LogWarning($"No motion found for: {signWord}");
            return;  // 如果沒有動畫，直接返回
        }

        // 檢查是否需要啟動練習功能
        if (practiceWords.Contains(signWord))
        {
            // 拆分詞彙（例如“我讀書”拆為“我”和“讀書”）
            List<string> signsToPractice;
            if (signWord == "我讀書")
            {
                signsToPractice = new List<string> { "我", "讀書" };
            }
            else if (signWord == "懶得刷牙")
            {
                signsToPractice = new List<string> { "懶惰", "刷牙" };
            }
            else
            {
                signsToPractice = new List<string> { signWord };
            }

            // 啟動協程，等待動畫播放完成後再啟動 Python 程式
            StartCoroutine(WaitForMotionAndStartPractice(signToMotionMap[signWord], signsToPractice));
        }
        // 其他詞彙僅播放動畫，不啟動練習
    }

    private IEnumerator WaitForMotionAndStartPractice(AnimationClip clip, List<string> signs)
    {
        // 等待動畫播放完成（使用動畫長度）
        yield return new WaitForSeconds(clip.length);

        UnityEngine.Debug.Log("Motion finished, starting Python program.");

        // 動畫播放完成後，啟動 Python 程式
        StartPythonProgram(signs);
    }

    private void StartPythonProgram(List<string> signs)
    {
        try
        {
            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.FileName = "python";
            // 將詞彙列表轉為逗號分隔的字串作為參數
            string signsArg = $"\"{string.Join(",", signs)}\"";
            startInfo.Arguments = $"\"C:/Users/gfaui/My project (3)/SignLanguage-Unity.py\" {signsArg}";
            startInfo.UseShellExecute = true;
            startInfo.CreateNoWindow = false;  // 顯示 Python 視窗

            // 啟動 Python 程式並等待其完成
            Process process = Process.Start(startInfo);
            process.WaitForExit();  // 等待 Python 程式關閉
            UnityEngine.Debug.Log("Python program finished.");
        }
        catch (System.Exception e)
        {
            UnityEngine.Debug.LogError("Failed to start Python program: " + e.Message);
        }
    }
}