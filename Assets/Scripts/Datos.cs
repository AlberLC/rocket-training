using System;
using UnityEngine;

[Serializable]
public class DatosCuerpoCeleste
{
    public string nombre;
    public Vector2 posicion;
    public Vector2 velocidad;
    public float masa;    
}

[Serializable]
public class DatosEsferaCeleste : DatosCuerpoCeleste
{
    public float radio;
}

[Serializable]
public class DatosNave : DatosCuerpoCeleste
{
    public float altura;
    public float ancho;
    public float angulo;
    public float combustible;
}

[Serializable]
public class Datos
{
    public float g;
    public DatosNave datosNave;
    public DatosEsferaCeleste[] datosEsferasCelestes;
}


