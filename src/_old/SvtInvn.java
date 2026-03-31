//****************************************************************************************
//   TITLE   :  商品マスタ  /画面イベントワークフロー処理（サーブレット受信）
//   SYSTEM  :
//
//   FILE-ID :
//   PROJECT :
//
//   WRITE   :  2019/12/20   By Nakatani
//   UPDATE  :
//
//   REMRAKS :  ユーザー層コマンドキー処理判定を行う
//              マルチスレッド動作にてインスタンス変数は共有しないこと！
//              スレッド毎にビジネス層のインスタンスを生成・消滅する（＝スレッドセーフ）
//
//****************************************************************************************
package  PG_Business.Master.Invn.List;

import javax.faces.context.FacesContext;

import org.richfaces.event.UploadEvent;

import PG_Business.Common.utils.SessionUtil;
import PG_Business._Base.SvtBase;
import PG_Common.CConst;

//****************************************************************************************
//  Class       : managed-bean
//  Scope       :イベント
//  Note        :
//****************************************************************************************
public class SvtInvn extends SvtBase implements CConst {
private    FomInvn           fomInvn          = null;                                         //初期画面Bean

  //======================================================================================
  //   バッキングBean
  //   Scope     :セッション
  //   Note      :
  //======================================================================================
  public void setFomInvn(FomInvn fomInvn) {
      this.fomInvn         = fomInvn;
  }
  //======================================================================================
  //   初期処理(選択画面作成)
  //   Scope     :イベント
  //   Parameter :
  //   Return    :次画面
  //   Note      :
  //======================================================================================
  public String Gen_Cmd_ViewInit()  {
  String   atStr     =  null;

   try{
	    //HTTPデータ受信
        FacesContext   facesContext  = super.Gen_Form_Get();                                   //HTTP受信 サーブレットリクエストオブジェクト取得

	    //パラメータへセット
		PrmInvn aoPrmInvn             =  new PrmInvn();                                        //パラメータBean
		aoPrmInvn.setObject(this.fomInvn);                                                     //パラメータBeanへログインフォームセット
		aoPrmInvn.setFacesContext(facesContext);                                               //パラメータBeanへメッセージセット

		//実行
		CtlInvn00 aoCtlInvn00         =  new CtlInvn00(aoPrmInvn);
		aoCtlInvn00.Gen_Act_Cmd(gciCmd_VIEWINIT);                                              //年度
		//return "InvnListInit";                                                               //siteMap";
		return "InitInvnList";
   }
   catch (Exception ex){
        ex.printStackTrace();
   }
   return "";
  }
  //======================================================================================
  //   データ検索ボタン押下処理
  //   Scope     :イベント
  //   Parameter :
  //   Return    :次画面
  //   Note      :
  //======================================================================================
  public String Gen_Cmd_Get()   {
  String   atStr     =  null;

	try{
        // セッション情報をクリア
        SessionUtil util = new SessionUtil();
        util.removeExcludingSessionForm(this.fomInvn);
		FacesContext   facesContext = super.Gen_Form_Get();                                     //HTTP受信 サーブレットリクエストオブジェクト取得

	    //パラメータへセット
		PrmInvn aoPrmInvn             =  new PrmInvn();                                         //パラメータBean
		aoPrmInvn.setObject(this.fomInvn);                                                      //パラメータBeanへログインフォームセット
		aoPrmInvn.setFacesContext(facesContext);                                                //パラメータBeanへメッセージセット

		//実行
		CtlInvn00 aoCtlInvn00         =  new CtlInvn00(aoPrmInvn);
		aoCtlInvn00.Gen_Act_Cmd(gciCmd_GET);                                                    //
		return "InitInvnList";
	}
	catch (Exception ex){
	        ex.printStackTrace();
	}
	return "";
  }
  //======================================================================================
  //   印刷ファイル作成ボタン押下処理
  //   Scope     :イベント
  //   Parameter :
  //   Return    :次画面
  //   Note      :
  //======================================================================================
  public String Gen_Cmd_Print()   {
  String   atStr     =  null;

	try{
        // セッション情報をクリア
        SessionUtil util = new SessionUtil();
        util.removeExcludingSessionForm(this.fomInvn);
		FacesContext   facesContext = super.Gen_Form_Get();                                     //HTTP受信 サーブレットリクエストオブジェクト取得

	    //パラメータへセット
		PrmInvn aoPrmInvn             =  new PrmInvn();                                         //パラメータBean
		aoPrmInvn.setObject(this.fomInvn);                                                      //パラメータBeanへログインフォームセット
		aoPrmInvn.setFacesContext(facesContext);                                                //パラメータBeanへメッセージセット

		//実行
		CtlInvn00 aoCtlInvn00         =  new CtlInvn00(aoPrmInvn);
		aoCtlInvn00.Gen_Act_Cmd(gciCmd_PRINT);                                                  //
		return "success";
	}
	catch (Exception ex){
	     ex.printStackTrace();
	}
	return "";
  }
  //======================================================================================
  //   印刷ファイル出力（ダウンロード）ボタン押下処理
  //   Scope     :イベント
  //   Parameter :
  //   Return    :次画面
  //   Note      :
  //======================================================================================
  public String Gen_Cmd_Download()   {
  String   atStr     =  null;

	try{
        // セッション情報をクリア
        SessionUtil util = new SessionUtil();
        util.removeExcludingSessionForm(this.fomInvn);
		FacesContext   facesContext = super.Gen_Form_Get();                                     //HTTP受信 サーブレットリクエストオブジェクト取得

	    //パラメータへセット
		PrmInvn aoPrmInvn             =  new PrmInvn();                                         //パラメータBean
		aoPrmInvn.setObject(this.fomInvn);                                                      //パラメータBeanへログインフォームセット
		aoPrmInvn.setFacesContext(facesContext);                                                //パラメータBeanへメッセージセット

		//実行
		CtlInvn00 aoCtlInvn00         =  new CtlInvn00(aoPrmInvn);
		aoCtlInvn00.Gen_Act_Cmd(gciCmd_DOWNLOAD);                                               //
		return "success";
	}
	catch (Exception ex){
	     ex.printStackTrace();
	}
	return "";
  }
  //======================================================================================
  //   ファイルアップロード選択画面
  //   Scope     :イベント
  //   Parameter :
  //   Return    :次画面
  //   Note      :
  //======================================================================================
  public String Gen_Cmd_UploadView()   {
  String   atStr     =  null;

	try{
        // セッション情報をクリア
        SessionUtil util = new SessionUtil();
        util.removeExcludingSessionForm(this.fomInvn);
		FacesContext   facesContext = super.Gen_Form_Get();                                     //HTTP受信 サーブレットリクエストオブジェクト取得

	    //パラメータへセット
		PrmInvn aoPrmInvn       =  new PrmInvn();                                               //パラメータBean
		aoPrmInvn.setObject(this.fomInvn);                                                      //パラメータBeanへログインフォームセット
		aoPrmInvn.setFacesContext(facesContext);                                                //パラメータBeanへメッセージセット

		//実行
		CtlInvn00 aoCtlInvn00   =  new CtlInvn00(aoPrmInvn);
		aoCtlInvn00.Gen_Act_Cmd(gciCmd_UPLOADVIEW);                                             //
		return "ImportInvnList";
	}
	catch (Exception ex){
	     ex.printStackTrace();
	}
	return "";
  }
  //======================================================================================
  //   ファイルアップロードボタン押下処理
  //   Scope     :イベント
  //   Parameter :
  //   Return    :次画面
  //   Note      :
  //======================================================================================
  public String Gen_Cmd_Upload(UploadEvent event)   {
  String   atStr     =  null;

	try{
        // セッション情報をクリア
        SessionUtil util = new SessionUtil();
        util.removeExcludingSessionForm(this.fomInvn);
		FacesContext   facesContext = super.Gen_Form_Get();                                     //HTTP受信 サーブレットリクエストオブジェクト取得


		//イベントオブジェクト
		this.fomInvn.event = (UploadEvent)event;


	    //パラメータへセット
		PrmInvn aoPrmInvn       =  new PrmInvn();                                               //パラメータBean
		aoPrmInvn.setObject(this.fomInvn);                                                      //パラメータBeanへログインフォームセット
		aoPrmInvn.setFacesContext(facesContext);                                                //パラメータBeanへメッセージセット

		//実行
		CtlInvn00 aoCtlInvn00   =  new CtlInvn00(aoPrmInvn);
		aoCtlInvn00.Gen_Act_Cmd(gciCmd_UPLOAD);                                                 //
		return "ImportInvnLIst";

	}
	catch (Exception ex){
	     ex.printStackTrace();
	}
	return "";
  }
  //======================================================================================
  //   ファイルアップロードボタン押下処理
  //   Scope     :イベント
  //   Parameter :
  //   Return    :次画面
  //   Note      :
  //======================================================================================
  public String Gen_Cmd_Upload_Cansel()   {
  String   atStr     =  null;

	try{
        // セッション情報をクリア
        SessionUtil util = new SessionUtil();
        util.removeExcludingSessionForm(this.fomInvn);
		FacesContext   facesContext = super.Gen_Form_Get();                                     //HTTP受信 サーブレットリクエストオブジェクト取得

	    //パラメータへセット
		PrmInvn aoPrmInvn       =  new PrmInvn();                                               //パラメータBean
		aoPrmInvn.setObject(this.fomInvn);                                                      //パラメータBeanへログインフォームセット
		aoPrmInvn.setFacesContext(facesContext);                                                //パラメータBeanへメッセージセット

		//実行
		CtlInvn00 aoCtlInvn00   =  new CtlInvn00(aoPrmInvn);
		aoCtlInvn00.Gen_Act_Cmd(gciCmd_CANSEL);                                                 //
		return "ImportInvnLIst";

	}
	catch (Exception ex){
	     ex.printStackTrace();
	}
	return "";
  }
  //======================================================================================
  //   画面へファイル取り込み（インポート）ボタン押下処理
  //   Scope     :イベント
  //   Parameter :
  //   Return    :次画面
  //   Note      :
  //======================================================================================
  public String Gen_Cmd_ViewBody_Import()   {
  String   atStr     =  null;

	try{
        // セッション情報をクリア
        SessionUtil util = new SessionUtil();
        util.removeExcludingSessionForm(this.fomInvn);
		FacesContext   facesContext = super.Gen_Form_Get();                                     //HTTP受信 サーブレットリクエストオブジェクト取得

	    //パラメータへセット
		PrmInvn aoPrmInvn       =  new PrmInvn();                                               //パラメータBean
		aoPrmInvn.setObject(this.fomInvn);                                                      //パラメータBeanへログインフォームセット
		aoPrmInvn.setFacesContext(facesContext);                                                //パラメータBeanへメッセージセット

		//実行
		CtlInvn00 aoCtlInvn00   =  new CtlInvn00(aoPrmInvn);
		aoCtlInvn00.Gen_Act_Cmd(gciCmd_IMPORT);                                                 //
		return "ImportDataInvnList";                                                            //次画面遷移
	}
	catch (Exception ex){
	     ex.printStackTrace();
	}
	return "";
  }
  //======================================================================================
  //   データ更新ボタン押下処理
  //   Scope     :イベント
  //   Parameter :
  //   Return    :次画面
  //   Note      :
  //======================================================================================
  public String Gen_Cmd_Update()   {
  String   atStr     =  null;

	try{
        // セッション情報をクリア
        SessionUtil util = new SessionUtil();
        util.removeExcludingSessionForm(this.fomInvn);
		FacesContext   facesContext = super.Gen_Form_Get();                                     //HTTP受信 サーブレットリクエストオブジェクト取得

	    //パラメータへセット
		PrmInvn aoPrmInvn             =  new PrmInvn();                                         //パラメータBean
		aoPrmInvn.setObject(this.fomInvn);                                                      //パラメータBeanへログインフォームセット
		aoPrmInvn.setFacesContext(facesContext);                                                //パラメータBeanへメッセージセット

		//実行
		CtlInvn00 aoCtlInvn00         =  new CtlInvn00(aoPrmInvn);
		aoCtlInvn00.Gen_Act_Cmd(gciCmd_UPDATE);                                                 //
		return "InitInvnList";
	}
	catch (Exception ex){
	        ex.printStackTrace();
	}
	return "";
  }
  //======================================================================================
  //   戻るボタン押下処理
  //   Scope     :イベント
  //   Parameter :
  //   Return    :次画面
  //   Note      :
  //======================================================================================
  public String Gen_Cmd_ImportReturn() {
  String   atStr     =  null;

	try{
        // セッション情報をクリア
        SessionUtil util = new SessionUtil();
        util.removeExcludingSessionForm(this.fomInvn);
		FacesContext   facesContext = super.Gen_Form_Get();                                     //HTTP受信 サーブレットリクエストオブジェクト取得

	    //パラメータへセット
		PrmInvn aoPrmInvn       =  new PrmInvn();                                               //パラメータBean
		aoPrmInvn.setObject(this.fomInvn);                                                      //パラメータBeanへログインフォームセット
		aoPrmInvn.setFacesContext(facesContext);                                                //パラメータBeanへメッセージセット

		//実行
		CtlInvn00 aoCtlInvn00   =  new CtlInvn00(aoPrmInvn);
		aoCtlInvn00.Gen_Act_Cmd(gciCmd_RETUN);                                                  //
		return "importReturnInvnLIst";
	}
	catch (Exception ex){
	     ex.printStackTrace();
	}
	return "";
  }

}
