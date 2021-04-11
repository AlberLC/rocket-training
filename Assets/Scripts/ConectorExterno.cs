using System.Diagnostics;
using System.IO;
using System.Text;
using UnityEngine;
using System.Linq;
using System.Collections.Generic;
using System.Threading;
using Debug = UnityEngine.Debug;
using System;
using Newtonsoft.Json;

public class ConectorExterno
{
    private List<string> datos;
    private Process proceso;
    private StreamReader sr;
    private StreamWriter sw;
    private Thread hilo;

    public static string ReadToEnd(StreamReader reader, string end = "\n")
    {
        StringBuilder sb = new StringBuilder();

        while (true)
        {
            string aux = reader.ReadLine();
            sb.AppendLine(aux);
            if (aux.Contains(end)) break;
        }

        return sb.ToString();
    }

    public ConectorExterno(string path)
    {
        datos = new List<string>();
        proceso = new Process();
        proceso.StartInfo.UseShellExecute = false;
        proceso.StartInfo.RedirectStandardInput = true;
        proceso.StartInfo.RedirectStandardOutput = true;
        proceso.StartInfo.CreateNoWindow = true;
        proceso.StartInfo.FileName = "cmd.exe";
        proceso.Start();

        sr = proceso.StandardOutput;
        sw = proceso.StandardInput;

        sw.WriteLine($"python {path}");

        ReadToEnd(sr, path);

        hilo = new Thread(LeerConsola);
        hilo.Start();
    }

    public void EnviarDatos(object datos)
    {
        Debug.Log("Enviando: " + JsonUtility.ToJson(datos));
        sw.WriteLine(JsonUtility.ToJson(datos));
    }

    public (float, float) RecibirDatos()
    {
        Debug.Log("Recibiendo: " + datos[0]);
        Dictionary<string, float> dicc = JsonConvert.DeserializeObject<Dictionary<string, float>>(datos[0]);
        datos.RemoveAt(0);
        return (dicc["angulo"], dicc["potencia"]);
    }

    public void PararHilo()
    {
        hilo.Abort();
    }

    public bool HayDatos()
    {      
        return datos.Count > 0;
    }

    private void LeerConsola()
    {
        while (true)
        {
            datos.Add(sr.ReadLine());
        }
    }

}
