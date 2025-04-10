using UnityEngine;
using UnityEngine.SceneManagement;
using System.Diagnostics;
using System.Collections.Generic;
using System.Collections;  

public class MainSceneController : MonoBehaviour
{
    public MotionPlayer motionPlayer;  // �ޥ� Live2D �ҫ��� MotionPlayer �ե�
    public AnimationClip[] motionClips;  // �ʵe�C��A�������J
    private Dictionary<string, AnimationClip> signToMotionMap;  // ���J��ʵe���M�g

    private List<string> signWords = new List<string> { "��", "���", "���A", "Ū��", "�}��", "�i�k", "��Ū��", "�i�o���" };  // ���J�C��
    private List<string> practiceWords = new List<string> { "��Ū��", "�i�o���" };  // �ݭn�m�ߪ����J

    void Start()
    {
        // ��l�Ƶ��J��ʵe���M�g
        signToMotionMap = new Dictionary<string, AnimationClip>();
        for (int i = 0; i < signWords.Count && i < motionClips.Length; i++)
        {
            signToMotionMap[signWords[i]] = motionClips[i];
        }
    }

    // �I�����J���s�ɽե�
    public void OnSignButtonClicked(string signWord)
    {
        // ���� Live2D �ʵe
        if (signToMotionMap.ContainsKey(signWord))
        {
            AnimationClip clip = signToMotionMap[signWord];
            motionPlayer.PlayMotion(clip);
            UnityEngine.Debug.Log($"Playing motion for: {signWord}, duration: {clip.length} seconds");
        }
        else
        {
            UnityEngine.Debug.LogWarning($"No motion found for: {signWord}");
            return;  // �p�G�S���ʵe�A������^
        }

        // �ˬd�O�_�ݭn�Ұʽm�ߥ\��
        if (practiceWords.Contains(signWord))
        {
            // ������J�]�Ҧp����Ū�ѡ�����ڡ��M��Ū�ѡ��^
            List<string> signsToPractice;
            if (signWord == "��Ū��")
            {
                signsToPractice = new List<string> { "��", "Ū��" };
            }
            else if (signWord == "�i�o���")
            {
                signsToPractice = new List<string> { "�i�k", "���" };
            }
            else
            {
                signsToPractice = new List<string> { signWord };
            }

            // �Ұʨ�{�A���ݰʵe���񧹦���A�Ұ� Python �{��
            StartCoroutine(WaitForMotionAndStartPractice(signToMotionMap[signWord], signsToPractice));
        }
        // ��L���J�ȼ���ʵe�A���Ұʽm��
    }

    private IEnumerator WaitForMotionAndStartPractice(AnimationClip clip, List<string> signs)
    {
        // ���ݰʵe���񧹦��]�ϥΰʵe���ס^
        yield return new WaitForSeconds(clip.length);

        UnityEngine.Debug.Log("Motion finished, starting Python program.");

        // �ʵe���񧹦���A�Ұ� Python �{��
        StartPythonProgram(signs);
    }

    private void StartPythonProgram(List<string> signs)
    {
        try
        {
            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.FileName = "python";
            // �N���J�C���ର�r�����j���r��@���Ѽ�
            string signsArg = $"\"{string.Join(",", signs)}\"";
            startInfo.Arguments = $"\"C:/Users/gfaui/My project (3)/SignLanguage-Unity.py\" {signsArg}";
            startInfo.UseShellExecute = true;
            startInfo.CreateNoWindow = false;  // ��� Python ����

            // �Ұ� Python �{���õ��ݨ䧹��
            Process process = Process.Start(startInfo);
            process.WaitForExit();  // ���� Python �{������
            UnityEngine.Debug.Log("Python program finished.");
        }
        catch (System.Exception e)
        {
            UnityEngine.Debug.LogError("Failed to start Python program: " + e.Message);
        }
    }
}