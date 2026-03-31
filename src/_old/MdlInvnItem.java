//****************************************************************************************
//
//   TITLE   :  商品マスタ／テーブル項目
//   SYSTEM  :
//
//   PROJECT :
//   FILE-ID :
//
//   WRITE   :  2018/12/20      By. Nakatani
//   UPDATE  :
//
//   REMRAKS :
//
//****************************************************************************************
package  PG_Database.Master.Invn;

import java.io.Serializable;
import java.sql.ResultSet;
import java.sql.SQLException;

//****************************************************************************************
//  Class       :
//  Succession  :
//  Note        :
//****************************************************************************************
public class MdlInvnItem  implements Serializable {
private  byte             sbInvalid                  =  0;                                                  //Invalid Flg

private  long             sid;                                                                              //bigint(20) NOT NULL,
private  String           alu;                                                                              //varchar(20) COLLATE utf8_bin DEFAULT NULL,
private  String           description1;                                                                     //varchar(30) COLLATE utf8_bin DEFAULT NULL,
private  String           description2;                                                                     //varchar(30) COLLATE utf8_bin DEFAULT NULL,
private  String           description3;                                                                     //varchar(30) COLLATE utf8_bin DEFAULT NULL,

 //======================================================================================
 //   コンストラクタ
 //   Parameter :
 //   Return    :
 //   Note      :
 //======================================================================================
 public MdlInvnItem(){
 }
 //======================================================================================
 //   INVALID
 //   Parameter :  void
 //   Return    :  byte
 //   Note      :
 //======================================================================================
 public byte getSbInvalid() {
	return sbInvalid;
 }
 public void setSbInvalid(byte sbInvalid) {
	this.sbInvalid = sbInvalid;
 }
 //======================================================================================
 //   テーブル項目を変数へ移送
 //   Parameter :
 //   Return    :
 //   Note      :
 //======================================================================================
 public MdlInvnItem Gen_Mov_TtoW(ResultSet poResultSet) throws SQLException {
 int index = 0;

 try{//項目位置No
     this.setSid(poResultSet.getLong(1));                                                     //SID
     this.setDescription1(poResultSet.getString(20));                                         //商品名1
     this.setDescription2(poResultSet.getString(21));                                         //商品名2
     this.setDescription3(poResultSet.getString(22));                                         //商品名3
   }
   catch(SQLException sqle){
       sqle.printStackTrace();
       new SQLException(sqle.getMessage());
   }
	return this;
 }
 //======================================================================================
 //   プロパティ
 //   Parameter :
 //   Return    :
 //   Note      :
 //======================================================================================
 public long getSid() {
	return sid;
 }
 public void setSid(long sid) {
	this.sid = sid;
 }
 /**
 * aluを取得します。
 * @return alu
 */
public String getAlu() {
    return alu;
}
/**
 * aluを設定します。
 * @param alu alu
 */
public void setAlu(String alu) {
    this.alu = alu;
}
/**
 * description1を取得します。
 * @return description1
 */
public String getDescription1() {
return description1;
}
/**
 * description1を設定します。
 * @param description1 description1
 */
public void setDescription1(String description1) {
this.description1 = description1;
}
public String getDescription2() {
	return description2;
 }
 public void setDescription2(String description2) {
	this.description2 = description2;
 }
 public String getDescription3() {
	return description3;
 }
 public void setDescription3(String description3) {
	this.description3 = description3;
 }

}
