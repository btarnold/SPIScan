<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="6.2">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="6" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="national-semiconductor">
<description>&lt;b&gt;National Semiconductor&lt;/b&gt;&lt;p&gt;
http://www.national.com&lt;br&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
<package name="DIL18">
<description>&lt;b&gt;Dual In Line Package&lt;/b&gt;</description>
<wire x1="11.43" y1="2.921" x2="-11.43" y2="2.921" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="-2.921" x2="11.43" y2="-2.921" width="0.1524" layer="21"/>
<wire x1="11.43" y1="2.921" x2="11.43" y2="-2.921" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="2.921" x2="-11.43" y2="1.016" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="-2.921" x2="-11.43" y2="-1.016" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="1.016" x2="-11.43" y2="-1.016" width="0.1524" layer="21" curve="-180"/>
<pad name="1" x="-10.16" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="2" x="-7.62" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="7" x="5.08" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="8" x="7.62" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="3" x="-5.08" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="4" x="-2.54" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="6" x="2.54" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="5" x="0" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="9" x="10.16" y="-3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="10" x="10.16" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="11" x="7.62" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="12" x="5.08" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="13" x="2.54" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="14" x="0" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="15" x="-2.54" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="16" x="-5.08" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="17" x="-7.62" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<pad name="18" x="-10.16" y="3.81" drill="0.8128" shape="long" rot="R90"/>
<text x="-11.684" y="-3.048" size="1.27" layer="25" ratio="10" rot="R90">&gt;NAME</text>
<text x="-9.525" y="-0.635" size="1.27" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="PLCC20S">
<description>&lt;b&gt;PLCC&lt;/b&gt;&lt;p&gt;
20 lead square</description>
<wire x1="4.9" y1="4.9" x2="-2.665" y2="4.9" width="0.2032" layer="51"/>
<wire x1="-4.9" y1="2.665" x2="-4.9" y2="-4.9" width="0.2032" layer="51"/>
<wire x1="-4.9" y1="-4.9" x2="4.9" y2="-4.9" width="0.2032" layer="51"/>
<wire x1="4.9" y1="-4.9" x2="4.9" y2="4.9" width="0.2032" layer="51"/>
<wire x1="-2.665" y1="4.9" x2="-4.9" y2="2.665" width="0.2032" layer="51"/>
<circle x="0" y="3.8" radius="0.3" width="0.6096" layer="51"/>
<smd name="1" x="0" y="4.3" dx="0.6" dy="2.2" layer="1"/>
<smd name="2" x="-1.27" y="4.3" dx="0.6" dy="2.2" layer="1"/>
<smd name="3" x="-2.54" y="4.3" dx="0.6" dy="2.2" layer="1"/>
<smd name="4" x="-4.3" y="2.54" dx="2.2" dy="0.6" layer="1"/>
<smd name="5" x="-4.3" y="1.27" dx="2.2" dy="0.6" layer="1"/>
<smd name="6" x="-4.3" y="0" dx="2.2" dy="0.6" layer="1"/>
<smd name="7" x="-4.3" y="-1.27" dx="2.2" dy="0.6" layer="1"/>
<smd name="8" x="-4.3" y="-2.54" dx="2.2" dy="0.6" layer="1"/>
<smd name="9" x="-2.54" y="-4.3" dx="0.6" dy="2.2" layer="1"/>
<smd name="10" x="-1.27" y="-4.3" dx="0.6" dy="2.2" layer="1"/>
<smd name="11" x="0" y="-4.3" dx="0.6" dy="2.2" layer="1"/>
<smd name="12" x="1.27" y="-4.3" dx="0.6" dy="2.2" layer="1"/>
<smd name="13" x="2.54" y="-4.3" dx="0.6" dy="2.2" layer="1"/>
<smd name="14" x="4.3" y="-2.54" dx="2.2" dy="0.6" layer="1"/>
<smd name="15" x="4.3" y="-1.27" dx="2.2" dy="0.6" layer="1"/>
<smd name="16" x="4.3" y="0" dx="2.2" dy="0.6" layer="1"/>
<smd name="17" x="4.3" y="1.27" dx="2.2" dy="0.6" layer="1"/>
<smd name="18" x="4.3" y="2.54" dx="2.2" dy="0.6" layer="1"/>
<smd name="19" x="2.54" y="4.3" dx="0.6" dy="2.2" layer="1"/>
<smd name="20" x="1.27" y="4.3" dx="0.6" dy="2.2" layer="1"/>
<text x="-3.175" y="5.715" size="1.778" layer="25">&gt;NAME</text>
<text x="-4.445" y="-7.485" size="1.778" layer="27">&gt;VALUE</text>
<rectangle x1="-0.26" y1="4.95" x2="0.26" y2="5.4" layer="51"/>
<rectangle x1="-1.53" y1="4.95" x2="-1.01" y2="5.4" layer="51"/>
<rectangle x1="-2.8" y1="4.95" x2="-2.28" y2="5.4" layer="51"/>
<rectangle x1="-5.4" y1="2.28" x2="-4.95" y2="2.8" layer="51"/>
<rectangle x1="-5.4" y1="1.01" x2="-4.95" y2="1.53" layer="51"/>
<rectangle x1="-5.4" y1="-0.26" x2="-4.95" y2="0.26" layer="51"/>
<rectangle x1="-5.4" y1="-1.53" x2="-4.95" y2="-1.01" layer="51"/>
<rectangle x1="-5.4" y1="-2.8" x2="-4.95" y2="-2.28" layer="51"/>
<rectangle x1="-2.8" y1="-5.4" x2="-2.28" y2="-4.95" layer="51"/>
<rectangle x1="-1.53" y1="-5.4" x2="-1.01" y2="-4.95" layer="51"/>
<rectangle x1="-0.26" y1="-5.4" x2="0.26" y2="-4.95" layer="51"/>
<rectangle x1="1.01" y1="-5.4" x2="1.53" y2="-4.95" layer="51"/>
<rectangle x1="2.28" y1="-5.4" x2="2.8" y2="-4.95" layer="51"/>
<rectangle x1="4.95" y1="-2.8" x2="5.4" y2="-2.28" layer="51"/>
<rectangle x1="4.95" y1="-1.53" x2="5.4" y2="-1.01" layer="51"/>
<rectangle x1="4.95" y1="-0.26" x2="5.4" y2="0.26" layer="51"/>
<rectangle x1="4.95" y1="1.01" x2="5.4" y2="1.53" layer="51"/>
<rectangle x1="4.95" y1="2.28" x2="5.4" y2="2.8" layer="51"/>
<rectangle x1="2.28" y1="4.95" x2="2.8" y2="5.4" layer="51"/>
<rectangle x1="1.01" y1="4.95" x2="1.53" y2="5.4" layer="51"/>
</package>
</packages>
<symbols>
<symbol name="LM3915">
<wire x1="-10.16" y1="25.4" x2="12.7" y2="25.4" width="0.254" layer="94"/>
<wire x1="12.7" y1="25.4" x2="12.7" y2="-25.4" width="0.254" layer="94"/>
<wire x1="12.7" y1="-25.4" x2="-10.16" y2="-25.4" width="0.254" layer="94"/>
<wire x1="-10.16" y1="-25.4" x2="-10.16" y2="25.4" width="0.254" layer="94"/>
<text x="-10.16" y="26.67" size="1.778" layer="95">&gt;NAME</text>
<text x="-10.16" y="-27.94" size="1.778" layer="96">&gt;VALUE</text>
<pin name="RHI" x="-12.7" y="15.24" length="short" direction="in"/>
<pin name="RLO" x="-12.7" y="-2.54" length="short" direction="in"/>
<pin name="REFOUT" x="-12.7" y="10.16" length="short" direction="out"/>
<pin name="REFADJ" x="-12.7" y="5.08" length="short" direction="pas"/>
<pin name="V+" x="-12.7" y="22.86" length="short" direction="pwr"/>
<pin name="V-" x="-12.7" y="-22.86" length="short" direction="pwr"/>
<pin name="SIGIN" x="-12.7" y="-17.78" length="short" direction="in"/>
<pin name="LED1" x="15.24" y="22.86" length="short" direction="out" rot="R180"/>
<pin name="LED2" x="15.24" y="17.78" length="short" direction="out" rot="R180"/>
<pin name="LED3" x="15.24" y="12.7" length="short" direction="out" rot="R180"/>
<pin name="LED4" x="15.24" y="7.62" length="short" direction="out" rot="R180"/>
<pin name="LED5" x="15.24" y="2.54" length="short" direction="out" rot="R180"/>
<pin name="LED6" x="15.24" y="-2.54" length="short" direction="out" rot="R180"/>
<pin name="LED7" x="15.24" y="-7.62" length="short" direction="out" rot="R180"/>
<pin name="LED8" x="15.24" y="-12.7" length="short" direction="out" rot="R180"/>
<pin name="LED9" x="15.24" y="-17.78" length="short" direction="out" rot="R180"/>
<pin name="LED10" x="15.24" y="-22.86" length="short" direction="out" rot="R180"/>
<pin name="MODE" x="-12.7" y="-10.16" length="short" direction="in"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="LM391" prefix="IC">
<description>&lt;b&gt;Dot/Bar Display Driver&lt;/b&gt;&lt;p&gt;
Source:&lt;br&gt;
&lt;a href="http://www.national.com/ds/LM/LM3915.pdf"&gt; Data sheet LM3915&lt;/a&gt;&lt;br&gt;
&lt;a href="http://www.national.com/ds/LM/LM3914.pdf"&gt; Data sheet LM3914 &lt;/a&gt;</description>
<gates>
<gate name="G$1" symbol="LM3915" x="0" y="0"/>
</gates>
<devices>
<device name="N" package="DIL18">
<connects>
<connect gate="G$1" pin="LED1" pad="1"/>
<connect gate="G$1" pin="LED10" pad="10"/>
<connect gate="G$1" pin="LED2" pad="18"/>
<connect gate="G$1" pin="LED3" pad="17"/>
<connect gate="G$1" pin="LED4" pad="16"/>
<connect gate="G$1" pin="LED5" pad="15"/>
<connect gate="G$1" pin="LED6" pad="14"/>
<connect gate="G$1" pin="LED7" pad="13"/>
<connect gate="G$1" pin="LED8" pad="12"/>
<connect gate="G$1" pin="LED9" pad="11"/>
<connect gate="G$1" pin="MODE" pad="9"/>
<connect gate="G$1" pin="REFADJ" pad="8"/>
<connect gate="G$1" pin="REFOUT" pad="7"/>
<connect gate="G$1" pin="RHI" pad="6"/>
<connect gate="G$1" pin="RLO" pad="4"/>
<connect gate="G$1" pin="SIGIN" pad="5"/>
<connect gate="G$1" pin="V+" pad="3"/>
<connect gate="G$1" pin="V-" pad="2"/>
</connects>
<technologies>
<technology name="4"/>
<technology name="5"/>
</technologies>
</device>
<device name="V" package="PLCC20S">
<connects>
<connect gate="G$1" pin="LED1" pad="1"/>
<connect gate="G$1" pin="LED10" pad="12"/>
<connect gate="G$1" pin="LED2" pad="20"/>
<connect gate="G$1" pin="LED3" pad="19"/>
<connect gate="G$1" pin="LED4" pad="18"/>
<connect gate="G$1" pin="LED5" pad="17"/>
<connect gate="G$1" pin="LED6" pad="16"/>
<connect gate="G$1" pin="LED7" pad="15"/>
<connect gate="G$1" pin="LED8" pad="14"/>
<connect gate="G$1" pin="LED9" pad="13"/>
<connect gate="G$1" pin="MODE" pad="11"/>
<connect gate="G$1" pin="REFADJ" pad="10"/>
<connect gate="G$1" pin="REFOUT" pad="8"/>
<connect gate="G$1" pin="RHI" pad="6"/>
<connect gate="G$1" pin="RLO" pad="4"/>
<connect gate="G$1" pin="SIGIN" pad="5"/>
<connect gate="G$1" pin="V+" pad="3"/>
<connect gate="G$1" pin="V-" pad="2"/>
</connects>
<technologies>
<technology name="4"/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="customparts">
<packages>
<package name="MOLEX2PINSCREWTERM">
<pad name="P$1" x="3.1525" y="0" drill="0.9" shape="long" rot="R90"/>
<pad name="P$2" x="-3.1525" y="0" drill="0.9" shape="long" rot="R90"/>
<wire x1="-6.35" y1="6.7" x2="6.35" y2="6.7" width="0.127" layer="51"/>
<wire x1="6.35" y1="6.7" x2="6.35" y2="-5.8" width="0.127" layer="51"/>
<wire x1="6.35" y1="-5.8" x2="-6.35" y2="-5.8" width="0.127" layer="51"/>
<wire x1="-6.35" y1="-5.8" x2="-6.35" y2="6.7" width="0.127" layer="51"/>
<wire x1="-6.35" y1="6.7" x2="-4.45" y2="3.4" width="0.127" layer="51"/>
<wire x1="-4.45" y1="3.4" x2="-2.55" y2="3.45" width="0.127" layer="51"/>
<wire x1="-2.55" y1="3.45" x2="-0.65" y2="6.6" width="0.127" layer="51"/>
<wire x1="-0.65" y1="6.6" x2="0.65" y2="6.65" width="0.127" layer="51"/>
<wire x1="0.65" y1="6.65" x2="2" y2="3.5" width="0.127" layer="51"/>
<wire x1="2" y1="3.5" x2="4.65" y2="3.5" width="0.127" layer="51"/>
<wire x1="4.65" y1="3.5" x2="6.3" y2="6.6" width="0.127" layer="51"/>
</package>
</packages>
<symbols>
<symbol name="SCREWTERM">
<pin name="1" x="-5.08" y="0" length="middle"/>
<pin name="2" x="-5.08" y="-5.08" length="middle"/>
<wire x1="-2.54" y1="2.54" x2="-2.54" y2="-10.16" width="0.254" layer="94"/>
<wire x1="-2.54" y1="-10.16" x2="7.62" y2="-10.16" width="0.254" layer="94"/>
<wire x1="7.62" y1="-10.16" x2="7.62" y2="2.54" width="0.254" layer="94"/>
<wire x1="7.62" y1="2.54" x2="-2.54" y2="2.54" width="0.254" layer="94"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="SCREWTERM">
<gates>
<gate name="G$1" symbol="SCREWTERM" x="-2.54" y="5.08"/>
</gates>
<devices>
<device name="" package="MOLEX2PINSCREWTERM">
<connects>
<connect gate="G$1" pin="1" pad="P$1"/>
<connect gate="G$1" pin="2" pad="P$2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="IC1" library="national-semiconductor" deviceset="LM391" device="V" technology="4"/>
<part name="U$1" library="customparts" deviceset="SCREWTERM" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="IC1" gate="G$1" x="63.5" y="53.34"/>
<instance part="U$1" gate="G$1" x="5.08" y="68.58"/>
</instances>
<busses>
<bus name="24IN">
<segment>
<wire x1="-15.24" y1="73.66" x2="-15.24" y2="35.56" width="0.762" layer="92"/>
<label x="2.54" y="68.58" size="1.778" layer="95"/>
</segment>
</bus>
</busses>
<nets>
<net name="24IN" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="1"/>
<wire x1="0" y1="68.58" x2="-15.24" y2="68.58" width="0.1524" layer="91"/>
<wire x1="-15.24" y1="68.58" x2="-15.24" y2="66.04" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$2" class="0">
<segment>
<pinref part="IC1" gate="G$1" pin="V+"/>
<wire x1="2.54" y1="68.58" x2="43.18" y2="68.58" width="0.1524" layer="91"/>
<wire x1="43.18" y1="68.58" x2="50.8" y2="76.2" width="0.1524" layer="91"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
