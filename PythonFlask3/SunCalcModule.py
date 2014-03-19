import datetime, jdcal, parser

#just discoverd this lib https://github.com/pingswept/pysolar/wiki/examples

def testext():
    extstr = 'from external py'
    return extstr
   
def VariablesCalcSunPosition():
    #string date = DateTime.Now.ToShortDateString();
    #string time = DateTime.Now.ToShortTimeString();

    GeomMeanLongSun 
    GeomMeanAnomSun 
    EccentEarthOrbit
    SunEqOfCtr 
    SunTrueLong
    SunTrueAnom
    SunRadVector
    SunAppLong
    MeanObliqEcliptic
    ObliqCorr
    #SunRtAscen
    SunDeclin
    VarY
    EqOfTime
    HA_Sunrise
    SolarNoon
    SunriseTime
    SunsetTime
    SunlightDuration 
    TrueSolarTime
    dateValue #DateTime
    HourAngle
    SolarZenithAngle
    SolarElevationAngle
    SolarAzimuthAngle #(deg cw from N)
    

    timezone
    latitude
    longtitude
    return
    


date = datetime.datetime.now()

def ConvertToRadians(val):
    return (Math.PI / 180) * val
    
def ConvertToDegrees(val):
    return (180 / Math.PI) * val

def ToJulianDate(date):
    DateToArray = date.strftime('%Y.%m.%d').split(".") 
    JulianDate = sum(jdcal.gcal2jd(DateToArray[0],DateToArray[1],DateToArray[2]))
    return JulianDate
    #F2
JulianDate = ToJulianDate(date)
    

def ToJulianCentury(JulianDate):
    JulianCentury = (JulianDate - 2451545) / 36525;
    return JulianCentury;
    #G2
JulianCentury = ToJulianCentury(JulianDate)



print "x"
print JulianDate
print JulianCentury


"""
    public string FormatTime(double val)
    {
        return TimeSpan.FromMinutes(val/0.000694444).ToString("c");
    }



    private void fn_calculate(string datetime)
    {
        fn_showMap();
        string MD = datetime;
        if (datetime == "")
        {
             MD = txt_datetime.Text.Trim();
        }
        //dateValue = new DateTime(2014, 1, 23, 00, 06, 00);
        //2014-01-22-00-00-00

        dateValue = new DateTime(Convert.ToInt16(MD.Substring(0, 4)), Convert.ToInt16(MD.Substring(5, 2)), Convert.ToInt16(MD.Substring(8, 2)), Convert.ToInt16(MD.Substring(11, 2)), Convert.ToInt16(MD.Substring(14, 2)), Convert.ToInt16(MD.Substring(17, 2)));

        JulianDate = ToJulianDate(dateValue);
        JulianCentury = ToJulianCentury(JulianDate);
        GeomMeanLongSun = ToGeomMeanLongSun();
        GeomMeanAnomSun = ToGeomMeanAnomSun();
        latitude = Convert.ToDouble(txt_Latitude.Text.Trim());
        longtitude = Convert.ToDouble(txt_Longtitude.Text.Trim());
        timezone = Convert.ToInt16(txt_timezone.Text.Trim());

        EccentEarthOrbit = ToEccentEarthOrbit();
        SunEqOfCtr = ToSunEqOfCtr();
        SunTrueLong = ToSunTrueLong();
        SunTrueAnom = ToSunTrueAnom();
        SunRadVector = ToSunRadVector();
        SunAppLong = ToSunAppLong();
        MeanObliqEcliptic = ToMeanObliqEcliptic();
        ObliqCorr = ToObliqCorr();
        //ToSunRtAscen();
        SunDeclin = ToSunDeclin();
        VarY = GetVarY();
        EqOfTime = ToEqOfTime();
        HA_Sunrise = ToHA_Sunrise();
        SolarNoon = ToSolarNoon();
        SunriseTime = ToSunriseTime();
        SunsetTime = ToSunsetTime();
        SunlightDuration = ToSunlightDuration();
        TrueSolarTime = ToTrueSolarTime();
        HourAngle = ToHourAngle();
        SolarZenithAngle = ToSolarZenithAngle();
        SolarElevationAngle = ToSolarElevationAngle();
        SolarAzimuthAngle = ToSolarAzimuthAngle();//(degcwfromN)();

    }


    protected void Button1_Click(object sender, EventArgs e)
    {
        fn_calculate("");
        //0.004166667 je rovnake ako dateValue.TimeOfDay.TotalDays pre 00:06:00
        //0.000694444 je rovnake ako dateValue.TimeOfDay.TotalDays pre 00:01:00
        //Response.Write(TimeSpan.FromMinutes(dateValue.TimeOfDay.TotalDays/0.000694444).ToString("c"));

       /* 
        lbl_status.Text = "ToJulianDate: " + JulianDate + "<br/>JulianCentury:" + JulianCentury + "<br> Date:" + dateValue.ToString("f") + " TimeOfDay.TotalDays:" + dateValue.TimeOfDay.TotalDays.ToString() + " <br/> GeomMeanLongSun:" + GeomMeanLongSun;
        lbl_status.Text += "<br/> ToGeomMeanAnomSun:" + ToGeomMeanAnomSun() + "<br/> ToEccentEarthOrbit:" + ToEccentEarthOrbit() + "<br/> ToSunEqOfCtr:" + ToSunEqOfCtr();
        lbl_status.Text += "<br/>ToSunTrueLong:" + ToSunTrueLong() + "<br/>ToSunTrueAnom:" + ToSunTrueAnom() + "<br/>ToSunRadVector:" + ToSunRadVector() + "<br>ToSunAppLong:" + ToSunAppLong();
        lbl_status.Text += "<br/>MeanObliqEcliptic:" + ToMeanObliqEcliptic() + "<br/>ToObliqCorr:" + ToObliqCorr() + "<br/>ToSunDeclin:" + ToSunDeclin();
        lbl_status.Text += "<br/>GetVarY:" + GetVarY() + "<br/>ToEqOfTime:" + ToEqOfTime() + "<br>ToHA_Sunrise" + ToHA_Sunrise(); */
        lbl_status.Text = "<br/><br/>Date:" + dateValue.ToString() + "<br>Najvyssie/SolarNoon:" + FormatTime(ToSolarNoon()) + "<br>Vychod/Sunrise:" + FormatTime(ToSunriseTime()) + "<br/>Zapad/SunsetTime:" + FormatTime(ToSunsetTime()) + "<br/>SunlightDuration:" + ToSunlightDuration();
        lbl_status.Text += "<b><br/SolarZenithAngle:" + ToSolarZenithAngle() + "</b><br>SolarElevationAngle" + ToSolarElevationAngle() + "<br><b>SolarAzimuthAngle(v smere CW from North):<b>" + ToSolarAzimuthAngle();
        
    }

    private void fn_showMap()
    {
        frameMap.Attributes["src"] = "https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=sk&amp;ie=UTF8&amp;ll=" + txt_Latitude.Text.Trim() + "," + txt_Longtitude.Text.Trim() + "&amp;spn=0.024801,0.055747&amp;t=h&amp;z=10&amp;output=embed";
        lbl_showmap.Text = "https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=sk&amp;ie=UTF8&amp;ll=" + txt_Latitude.Text.Trim() + "," + txt_Longtitude.Text.Trim() + "&amp;spn=0.024801,0.055747&amp;t=h&amp;z=10&amp;output=embed";
    }

  

    public double ToJulianCentury(double JulianDate)
    {
        JulianCentury = (JulianDate - 2451545) / 36525;
        return JulianCentury;
        //G2
    }

    public double ToGeomMeanLongSun()
    {
        GeomMeanLongSun = (280.46646 + JulianCentury * (36000.76983 + JulianCentury * 0.0003032) % 360);
        return GeomMeanLongSun;
        //I2
    }

    public double ToGeomMeanAnomSun()
    {
        GeomMeanAnomSun = 357.52911 + JulianCentury * (35999.05029 - 0.0001537 * JulianCentury);
        return GeomMeanAnomSun;
        //J2
    }

    public double ToEccentEarthOrbit()
    {
        EccentEarthOrbit = 0.016708634 - JulianCentury * (0.000042037 + 0.0000001267 * JulianCentury);
        return EccentEarthOrbit;
        //K2
    }
    
    public double ToSunEqOfCtr()
    {
        
        SunEqOfCtr = Math.Sin(ToRadians(GeomMeanAnomSun)) * (1.914602 - JulianCentury * (0.004817 + 0.000014 * JulianCentury)) + Math.Sin(ToRadians(2 * GeomMeanAnomSun)) * (0.019993 - 0.000101 * JulianCentury) + Math.Sin(ToRadians(3 * GeomMeanAnomSun)) * 0.000289;
        return SunEqOfCtr;
        //L2
    }

    public double ToSunTrueLong()
    {
        SunTrueLong = GeomMeanLongSun + SunEqOfCtr;
        return SunTrueLong;
        //M2
    }

    public double ToSunTrueAnom()
    {
       SunTrueAnom = GeomMeanAnomSun + SunEqOfCtr;
       return SunTrueAnom;
        //N2
    }

    public double ToSunRadVector()
    {
        SunRadVector = (1.000001018 * (1 - EccentEarthOrbit * EccentEarthOrbit)) / (1 + EccentEarthOrbit * Math.Cos(ToRadians(SunTrueAnom)));
        return SunRadVector;
        //02
    }

    public double ToSunAppLong()
    {
        SunAppLong = SunTrueLong - 0.00569 - 0.00478 * Math.Sin(ToRadians(125.04 - 1934.136 * JulianCentury));
        return SunAppLong;
        //P2
    }

    public double ToMeanObliqEcliptic()
    {
        MeanObliqEcliptic = 23 + (26 + ((21.448 - JulianCentury * (46.815 + JulianCentury * (0.00059 - JulianCentury * 0.001813)))) / 60) / 60;
        return MeanObliqEcliptic;
        //Q2
    }

    public double ToObliqCorr()
    {
        ObliqCorr = MeanObliqEcliptic + 0.00256 * Math.Cos(ToRadians(125.04 - 1934.136 * JulianCentury));
        return ObliqCorr;
        //R2
    }

    //public double ToSunRtAscen()
    //{
    //    SunRtAscen = ToDegrees(Math.Atan2(Math.Cos(ToRadians(SunAppLong)), Math.Cos(ToRadians(ObliqCorr)) * Math.Sin(ToRadians(SunAppLong))));
    //    return SunRtAscen;
    //    //S2        
    //}

    public double ToSunDeclin()
    {
        SunDeclin = ToDegrees(Math.Asin(Math.Sin(ToRadians(ObliqCorr)) * Math.Sin(ToRadians(SunAppLong))));
        return SunDeclin;
        //T2
    }

    public double GetVarY()
    {
        VarY = Math.Tan(ToRadians(ObliqCorr / 2)) * Math.Tan(ToRadians(ObliqCorr / 2));
        return VarY;
        //U2
    }

    public double ToEqOfTime()
    {
        EqOfTime = 4 * ToDegrees(VarY * Math.Sin(2 * ToRadians(GeomMeanLongSun)) - 2 * EccentEarthOrbit * Math.Sin(ToRadians(GeomMeanAnomSun)) + 4 * EccentEarthOrbit * VarY * Math.Sin(ToRadians(GeomMeanAnomSun)) * Math.Cos(2 * ToRadians(GeomMeanLongSun)) - 0.5 * VarY * VarY * Math.Sin(4 * ToRadians(GeomMeanLongSun)) - 1.25 * EccentEarthOrbit * EccentEarthOrbit * Math.Sin(2 * ToRadians(GeomMeanAnomSun)));
        return EqOfTime;
        //V2
    }

    public double ToHA_Sunrise()
    {
        HA_Sunrise = ToDegrees(Math.Acos(Math.Cos(ToRadians(90.833)) / (Math.Cos(ToRadians(latitude)) * Math.Cos(ToRadians(SunDeclin))) - Math.Tan(ToRadians(latitude)) * Math.Tan(ToRadians(SunDeclin))));
        return HA_Sunrise;
        //W2
    }

    public double ToSolarNoon()
    {
        //=(720-4*$B$4-V2+$B$5*60)/1440  //time
        SolarNoon = (720 - (4 * longtitude) - EqOfTime + timezone * 60) / 1440;
        return SolarNoon;
        //X2
    }

    public double ToSunriseTime()
    {
        SunriseTime = SolarNoon - HA_Sunrise * 4 / 1440;
        return SunriseTime;
        //Y2
    }

    public double ToSunsetTime()
    {
        SunsetTime = SolarNoon + HA_Sunrise * 4 / 1440;
        return SunsetTime;
        //Z2
    }

    public double ToSunlightDuration()
    {
        SunlightDuration = 8 * HA_Sunrise;
        return SunlightDuration;
        //AA2
    }

    public double ToTrueSolarTime()
    {
        TrueSolarTime = (dateValue.TimeOfDay.TotalDays * 1440 + EqOfTime + 4 * longtitude - 60 * timezone % 1440);
        return TrueSolarTime;
        //AB2
    }

    public double ToHourAngle()
    {
        if((TrueSolarTime/4)<0) { HourAngle = TrueSolarTime/4+180;} else { HourAngle = TrueSolarTime/4-180;}     
        return HourAngle;
        //AC2
    }

    public double ToSolarZenithAngle()
    {
        SolarZenithAngle = ToDegrees(Math.Acos(Math.Sin(ToRadians(latitude)) * Math.Sin(ToRadians(SunDeclin)) + Math.Cos(ToRadians(latitude)) * Math.Cos(ToRadians(SunDeclin)) * Math.Cos(ToRadians(HourAngle))));
        return SolarZenithAngle;
        //AD2
    }

    public double ToSolarElevationAngle()
    {
        SolarElevationAngle = 90 - SolarZenithAngle;
        return SolarElevationAngle;
        //AE2
    }

    private void ToSolarNoonElevationAngle()
    {

        fn_calculate("2014-01-23-12-00-00");
        //AE2
    }


    public double ToSolarAzimuthAngle()
    {
        if(HourAngle>0)
        { SolarAzimuthAngle = (ToDegrees(Math.Acos(((Math.Sin(ToRadians(latitude)) * Math.Cos(ToRadians(SolarZenithAngle))) - Math.Sin(ToRadians(SunDeclin))) / (Math.Cos(ToRadians(latitude)) * Math.Sin(ToRadians(SolarZenithAngle))))) + 180 % 360); }            
        else { SolarAzimuthAngle = (540-ToDegrees(Math.Acos(((Math.Sin(ToRadians(latitude))*Math.Cos(ToRadians(SolarZenithAngle)))-Math.Sin(ToRadians(SunDeclin)))/(Math.Cos(ToRadians(latitude))*Math.Sin(ToRadians(SolarZenithAngle))))) - 360); }
        return SolarAzimuthAngle;        
    }



}

"""