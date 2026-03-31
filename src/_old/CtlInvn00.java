//****************************************************************************************
//   TITLE   :  商品マスタ / ビジネス層　コントローラ
//   SYSTEM  :
//
//   PROJECT :
//   FILE-ID :
//
//   WRITE   :  2018/12/20   by Nakatani
//   UPDATE  :
//
//   REMRAKS :
//
//****************************************************************************************
package PG_Business.Master.Invn.List;

import java.util.ArrayList;

import javax.faces.context.FacesContext;
import javax.faces.model.SelectItem;

import org.apache.poi.hssf.usermodel.HSSFCellStyle;
import org.apache.poi.hssf.usermodel.HSSFFont;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;

import PG_Business.Common.constant.CommonConst;
import PG_Business.Common.importfile.ImportBean;
import PG_Business.Common.importfile.ImportErrorListData;
import PG_Business.Common.importfile.ImportUtil;
import PG_Business.Common.poi.PoiEngine;
import PG_Business.Common.properties.CommonApplication;
import PG_Business.Input.I02Jtensu.Jtestten2Util;
import PG_Business._Base.CtlBase;
import PG_Common.CConst;
import PG_Common.exception.ClException;
import PG_Common.message.Messages;
import PG_Database.Master.Invn.MdlInvnGet;
import PG_Database.Master.Invn.MdlInvnItem;
import PG_Database.Master.Invn.MdlInvnUpdate;

//****************************************************************************************
//  Class         : ビジネス層クラス
//  Succession    :
//  Note          :
//****************************************************************************************
public class  CtlInvn00 extends CtlBase implements CConst{
 private    PrmInvn                  soPrmInvn                = null;                       //パラメータBean
 private    FomInvn                  fomInvn                  = null;                       //初期画面Bean
 private    MdlInvnGet               soMdlInvnGet             = null;                       //DB検索メソッド
 private    MdlInvnUpdate            soMdlInvnUpdate          = null;                       //DB更新メソッド
 private    MdlInvnItem              soMdlInvnItem            = null;                       //DB項目
 private    ArrayList<MdlInvnItem>   soaryMdlInvnItem         = null;                       //DB項目配列

 //======================================================================================
  //   コンストラクタ
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  public CtlInvn00(Object  aoObject) throws Exception{

	    super();                                                                            //基本クラス（DB接続）実行

		try {
              this.soPrmInvn = (PrmInvn)aoObject;
      		  this.fomInvn   = (FomInvn)soPrmInvn.getObject();                              //パラメータBeanにバッキングBeanセット

      		  this.Gen_Obj_New();                                                           //オブジェクト生成
              this.Gen_Init();                                                              //DBコネクションセット
	    }
        catch (Exception ex){
             soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005);                     //Error
        }
  }
  //======================================================================================
  //   オブジェクト生成（実装）
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  private void Gen_Obj_New() throws Exception{
	    try{
	        soaryMdlInvnItem      = new ArrayList<MdlInvnItem>();
	        if (soMdlInvnItem     == null)    soMdlInvnItem         = new MdlInvnItem();                                 //
	        if (soMdlInvnGet      == null)    soMdlInvnGet          = new MdlInvnGet(soMdlInvnItem, soaryMdlInvnItem,soPrmInvn);   //
	        if (soMdlInvnUpdate   == null)    soMdlInvnUpdate       = new MdlInvnUpdate(soMdlInvnItem);                  //
	    }
        catch (Exception ex){
            soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005);                      //Error
        }
  }
  //======================================================================================
  //   初期処理
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  private void Gen_Init() throws Exception{

	    try{
	    	this.stPgID                         = "";                                        //PG-ID

	        if(super.soConnection != null){
	        	soMdlInvnGet.PSet_Connection(super.soConnection);                            //Get用DBハンドルの設定
	        	soMdlInvnUpdate.PSet_Connection(super.soConnection);                         //Update用DBハンドルの設定
	        }
	     }
         catch (Exception ex){
            soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005);                       //Error
         }
  }
  //======================================================================================
  //   イベント判定実行
  //   Parameter :処理区分
  //   Return    :
  //   Note      :メッソドorクラス実行
  //======================================================================================
  public void Gen_Act_Cmd(int piCmdFunc)  throws ClException {

	  super.Gen_Act_Cmd(this.soPrmInvn.getFacesContext(),piCmdFunc );                        //ログ作成

	   switch (piCmdFunc) {
	        case gciCmd_VIEWINIT:
                this.Gen_Cmd_ViewInit();                                                     //初期画面項目作成
                break;
            case gciCmd_GET:
                this.Gen_Cmd_Get();                                                          //データ検索処理
                break;
            case gciCmd_PRINT:
                this.Gen_Cmd_Print();                                                        //印刷ファイル作成
                break;
            case gciCmd_DOWNLOAD:
                this.Gen_Cmd_Download();                                                     //印刷ファイル出力
                break;
            case gciCmd_UPLOADVIEW:
                this.Gen_Cmd_Upload_VIEW();                                                  //ファイル取り込み選択画面
                break;
            case gciCmd_UPLOAD:
                this.Gen_Cmd_Upload();                                                       //ファイルアップロード
                break;
            case gciCmd_IMPORT:
                this.Gen_Cmd_ViewBody_Import();                                              //ファイル画面取り込み
                break;
            case gciCmd_UPDATE:
                this.Gen_Cmd_Update();                                                       //ファイル更新
                break;
            case gciCmd_CANSEL:
                this.Gen_Cmd_Upload_Cansel();                                                 //ファイル取り込みキャンセル
                break;
            default:
                break;
        }
        super.Gen_Obj_Del();                                                                  //ＤＢクローズ
  }
  //======================================================================================
  //   初期画面の選択画面項目作成
  //   Parameter :
  //   Return    :
  //   Note      :クラスの引数に処理内容（振る舞い）を記述
  //              内部クラス（オブジェクト）を取得して対象メソッドを実行
  //======================================================================================
  public void Gen_Cmd_ViewInit()  {
   ArrayList<SelectItem> aoNendoOptions = null;
	  try{

		   //this.fomInvn.setSortMode("9");
		   this.fomInvn.setStyle("basic");
		   this.fomInvn.setDispFlag(false);
		   this.fomInvn.setReadonly(false);

		   this.fomInvn.setResultData(null);
    }
    catch (Exception ex){
        soPrmInvn.siRet = 1;                                                                   //Invalid
        ex.printStackTrace();
        soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005 + " ※ ");                    //Error
    }
  }
  //======================================================================================
  //   データ検索処理
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  public void Gen_Cmd_Get() throws ClException {
  FomInvnBody            aoFomInvnBody    = null;                                               //明細画面Bean
  ArrayList<FomInvnBody> aoaryFomInvnBody = new ArrayList<FomInvnBody>();                       //明細画面配列

	  try{
		    //データ検索
	        soItfAction           = soMdlInvnGet.getProcClass(gctGet);                          //内部クラス取得
	        soaryMdlInvnItem      = (ArrayList<MdlInvnItem>) soItfAction.Gen_Get01();           //内部クラスのメソッド実行、データ結果を配列にセット

	        if (soaryMdlInvnItem != null && soaryMdlInvnItem.size() != 0) {//データ有無
		        //データ結果を配列件数分処理
	        	for (int i = 0; i < soaryMdlInvnItem.size(); i++) {
	        		MdlInvnItem aoResultSet = (MdlInvnItem) soaryMdlInvnItem.get(i);
	        		aoFomInvnBody = new FomInvnBody();                                          //明細画面Bean
	        		//明細画面Beanにテーブル項目セット
	        		aoFomInvnBody.setSid(aoResultSet.getSid() );                                //SID
                    aoFomInvnBody.setDescription1(aoResultSet.getDescription1() );              //商品名1
                    aoFomInvnBody.setDescription2(aoResultSet.getDescription2() );              //商品名2
                    aoFomInvnBody.setDescription3(aoResultSet.getDescription3() );              //商品名3
    				aoaryFomInvnBody.add(aoFomInvnBody);                                        //明細画面Beanを明細画面配列に格納
 				}
	        	//初期画面Beanに明細画面配列をセット
	        	this.fomInvn.setResultData(aoaryFomInvnBody);
	        }

	        //初期画面Beanにセット
	        this.fomInvn.setCurrentValue(100);
    	    this.fomInvn.setStyle("notEdit");
    	    this.fomInvn.setReadonly(true);
    	    this.fomInvn.setDispFlag(true);
    	    this.fomInvn.setChangeFlg(false);
    	    this.fomInvn.setEnterCheck("");
	}
    catch (Exception ex){
    	this.soPrmInvn.siRet = 1;                                                              //Invalid
        ex.printStackTrace();
        soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005 + " ※ ");                    //Error
    }
  }
  //======================================================================================
  //   印刷処理
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  public void Gen_Cmd_Print() {
  PoiEngine          poiEngine           = new PoiEngine();
  HSSFWorkbook       workbook            = new HSSFWorkbook(); // テンプレートを取得する。
  HSSFSheet          sheet               = null;

      try{
	      // テンプレート取得
	      workbook = poiEngine.getTemplate(CommonApplication.getString("invnlist.fileName"));    // テンプレートを取得する。
	      workbook.setSheetName(0, CommonApplication.getString("invnlist.sheet1"));
	      sheet = workbook.getSheetAt(0);
	      workbook.setSheetName(0, CommonApplication.getString("invnlist.sheet1"));
	      sheet = workbook.getSheetAt(0);

	      //実行
 		  this.Gen_Cmd_Print_Init(poiEngine, workbook,sheet,fomInvn);                                //初期処理
		  this.Gen_Cmd_Print_Body(poiEngine,workbook,sheet,fomInvn);                                 //明細印刷
		  this.Gen_Cmd_Print_FileCreate(poiEngine,workbook,fomInvn);                                 //印刷結果出力ファイル作成
	  }
      catch (Exception ex){
      	    this.soPrmInvn.siRet = 1;                                                                //Invalid
            ex.printStackTrace();
            soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005 + " ※ ");                      //Error
     }
  }
  //======================================================================================
  //   印刷処理／初期処理
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  public void Gen_Cmd_Print_Init(PoiEngine poiEngine,
		                         HSSFWorkbook workbook,
		                         HSSFSheet sheet,
		                         FomInvn fomInvn) {
  HSSFRow row;

	  try{
	      fomInvn.setCurrentValue(40);

	      // フォント設定
	      HSSFFont font = workbook.createFont();
	      font.setFontName(CommonApplication.getString("poi.excel.fontName"));
	      font.setFontHeightInPoints(Short.parseShort(CommonApplication.getString("poi.excel.fontSize")));

	      // 共通設定
	      HSSFCellStyle commonStyle = workbook.createCellStyle();
	      commonStyle.setFont(font);

	      // 表設定
	      HSSFCellStyle tableStyle = workbook.createCellStyle();
	      tableStyle.cloneStyleFrom(commonStyle);
	      tableStyle.setBorderTop(HSSFCellStyle.BORDER_THIN);
	      tableStyle.setBorderLeft(HSSFCellStyle.BORDER_THIN);
	      tableStyle.setBorderRight(HSSFCellStyle.BORDER_THIN);
	      tableStyle.setBorderBottom(HSSFCellStyle.BORDER_THIN);

	      // ここからシートの処理
	      //sheet = workbook.getSheetAt(0);
	      // シート名変更
	      //workbook.setSheetName(0, CommonApplication.getString("jitiranhyou2.sheet1"));
	      // シート取得
	      //sheet = workbook.getSheetAt(0);
	  }
      catch (Exception ex){
      	    this.soPrmInvn.siRet = 1;                                                                //Invalid
            ex.printStackTrace();
            soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005 + " ※ ");                      //Error
      }
  }
  //======================================================================================
  //   印刷処理／ヘッダ
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  public void Gen_Cmd_Print_Head(PoiEngine poiEngine,
		                         HSSFWorkbook workbook,
                                 HSSFSheet sheet,
                                 FomInvn fomInvn) {
  HSSFRow row;

      try{
            // ヘッダー部編集
            row = poiEngine.getRow(sheet, 5);

            //String testNm = fomInvn.getSearchNendo()
            //              + CommonConst.NENDO_NM
            //              + NameGet.getCdNm(fomInvn.getSearchTestNo(), fomInvn.getJtestNoOptions());
            String testNm = "2019";

            poiEngine.setValueToCell(sheet, row, 1, testNm, null);

            // 教科名
            //setKyouka(sheet, fomInvn.getKyoukaNmList(), poiEngine);

	  }
      catch (Exception ex){
      	    this.soPrmInvn.siRet = 1;                                                                //Invalid
            ex.printStackTrace();
            soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005 + " ※ ");                      //Error
      }
  }
  //======================================================================================
  //   印刷処理／明細
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  public void Gen_Cmd_Print_Body( PoiEngine     poiEngine,
		                          HSSFWorkbook  workbook,
		                          HSSFSheet     sheet,
		                          FomInvn       fomInvn ) {
  HSSFRow row;

        try{
	        Jtestten2Util util = new Jtestten2Util();

	        //結果を取得
	        ArrayList<FomInvnBody> aoaryFomInvnBody = fomInvn.getResultData();

	        // データ出力
	        for (int i = 0; i < aoaryFomInvnBody.size(); i++) {
	        	FomInvnBody fomInvnBody = (FomInvnBody) aoaryFomInvnBody.get(i);

	        	// ヘッダー部編集
	            if (i == 0) {
	      		    this.Gen_Cmd_Print_Head(poiEngine,workbook,sheet,fomInvn);                                                       //ヘッダ
	            }

	            //明細部編集
	            row = poiEngine.getRow(sheet, i + 8);                                                                               //明細開始行
	            //poiEngine.setValueToCell(sheet,row,1,fomInvn.getSearchGakunen(),sheet.getRow(8).getCell(1).getCellStyle());        //
	            poiEngine.setValueToCell(sheet,row, 2, fomInvnBody.getSid(), sheet.getRow(8).getCell(2).getCellStyle());            //SID
	            poiEngine.setValueToCell(sheet,row, 3, fomInvnBody.getDescription1(), sheet.getRow(8).getCell(3).getCellStyle());   //商品名1
	            poiEngine.setValueToCell(sheet,row, 4, fomInvnBody.getDescription2(), sheet.getRow(8).getCell(4).getCellStyle());   //商品名2
	            poiEngine.setValueToCell(sheet,row, 5, fomInvnBody.getDescription3(), sheet.getRow(8).getCell(5).getCellStyle());   //商品名3
	        }
	        fomInvn.setCurrentValue(60);
	  }
      catch (Exception ex){
        	this.soPrmInvn.siRet = 1;                                                                //Invalid
            ex.printStackTrace();
            soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005 + " ※ ");                      //Error
      }
  }
   //======================================================================================
   //   印刷処理／ファイル作成
   //   Parameter :
   //   Return    :
   //   Note      :
   //======================================================================================
   public void Gen_Cmd_Print_FileCreate(PoiEngine poiEngine,
		                                HSSFWorkbook workbook,
		                                FomInvn fomInvn) {
   ArrayList<SelectItem> aoNendoOptions = null;

	  try{
	        //String str = loginInfo.getLoginMySchoolCd()
	        //		   + CommonConst.UNDER_BAR
	        //           + loginInfo.getLoginTcherCd()
	        //           + CommonConst.UNDER_BAR
	        //           + CommonApplication.getString("jitiranhyou2.fileName");


	        String str = "subsidary"
	        		   + CommonConst.UNDER_BAR
	                   + "store"
	                   + CommonConst.UNDER_BAR
	                   + CommonApplication.getString("invnlist.fileName");


	        // ファイルに書き出す
	        String filePath = poiEngine.createOutputFile(str, workbook);
	        fomInvn.setOutputFileName(filePath);

	        fomInvn.setCurrentValue(100);
	  }
      catch (Exception ex){
      	    this.soPrmInvn.siRet = 1;                                                                //Invalid
            ex.printStackTrace();
            soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005 + " ※ ");                      //Error
     }
  }
  //======================================================================================
  //   ファイルダウンロード
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  public void Gen_Cmd_Download(){
  FomInvn  fomInvn   = null;

     try{
	        //fomInvn fomInvn = (fomInvn) form;
		    fomInvn = this.fomInvn;

	    	String outputFileName = fomInvn.getOutputFileName();

	        // 検索条件の文字列を格納する。
	        StringBuffer sb = new StringBuffer();
	        //sb.append(CommonConst.UNDER_BAR);
	        //sb.append(fomInvn.getSearchNendo());
	        //sb.append(CommonUtil.getFileName(fomInvn.getSearchGakunen(),null));
	        //sb.append(CommonUtil.getFileName(fomInvn.getSearchGakkyu(),fomInvn.getGakkyuOptions()));
	        //sb.append(CommonUtil.getFileName(fomInvn.getSearchTestNo(),fomInvn.getJtestNoOptions()));

	        String dispFileName = CommonApplication.getString("invnlist.fileName00") + sb.toString();

	        // JSFは内部でサーブレット情報を管理しているので、それを取得する必要がある。
	        //FacesContext fContext = getFacesContext();
	        FacesContext fContext = soPrmInvn.getFacesContext();

	        PoiEngine poiEngine = new PoiEngine();
	        poiEngine.outputExcelFile(outputFileName, dispFileName, fContext);
	        fContext.responseComplete();
	  }
	  catch (Exception ex){
	    	this.soPrmInvn.siRet = 1;                                                                //Invalid
	        ex.printStackTrace();
	        soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005 + " ※ ");                      //Error
	    }
  }
 //======================================================================================
  //   ファイルアップロード/初期画面
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  public void Gen_Cmd_Upload_VIEW(){

	  //      Jtestten2ListForm jtestten2ListForm = (Jtestten2ListForm) form;
      /**
       * 取込情報初期化
       */
//     Jtestten2ImportBean jtestten2ImportBean = new Jtestten2ImportBean();
//     jtestten2ListForm.setJtestten2ImportBean(jtestten2ImportBean);
//     ImportUtil importUtil = new ImportUtil();
//     jtestten2ListForm.getJtestten2ImportBean().setImportBean(importUtil.initImportBean(loginInfo.getLoginTcherCd(), loginInfo.getLoginMySchoolCd()));
//     setActionForwardName("jtestten2ListImport");


      FomInvnImport fomInvnImport = new FomInvnImport();                                                //アップロード画面Form
      ImportUtil    importUtil    = new ImportUtil();                                                   //取り込み共通処理

     try{
         this.fomInvn.setFomInvnImport(fomInvnImport);                                                  //初期画面Fromへアップロード画面Form セット
         this.fomInvn.getFomInvnImport().setImportBean(importUtil.initImportBean("001", "994"));        //
         //setActionForwardName("ImportInvnList");                                                      //
     }
	  catch (Exception ex){
	    	this.soPrmInvn.siRet = 1;                                                                   //Invalid
	        ex.printStackTrace();
	        soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005 + " ※ ");                         //Error
	    }
  }
  //======================================================================================
  //   ファイルアップロード
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  public void Gen_Cmd_Upload(){


//      Jtestten2ListForm jtestten2ListForm = (Jtestten2ListForm) form;
 	  // データ取得
//      try {
//          ImportUtil importUtil = new ImportUtil();
//          importUtil.getUploadData(jtestten2ListForm.getJtestten2ImportBean().getImportBean());
//          HSSFWorkbook workbook = importUtil.getExcelWorkbook(jtestten2ListForm.getJtestten2ImportBean().getImportBean().getUploadItem());
          // インポート情報を初期化
//          clearImportData(jtestten2ListForm);
          // データ妥当性チェックおよび取込
//          getJtestten2FileData(jtestten2ListForm, workbook);
          // テンプレートファイルの実体を削除
//          importUtil.deleteTempFile(jtestten2ListForm
//                  .getJtestten2ImportBean().getImportBean()); // 添付ファイル削除
//      }

	  ImportBean importBean = fomInvn.getFomInvnImport().getImportBean();
      importBean.setUploadItem(this.fomInvn.event.getUploadItem());

      ImportUtil importUtil = new ImportUtil();                                                         //取り込み共通処理

     try{

         importUtil.getUploadData(fomInvn.getFomInvnImport().getImportBean());                          //アップロードファイルのデータを取得します

         HSSFWorkbook workbook = importUtil.getExcelWorkbook(fomInvn.getFomInvnImport().getImportBean().getUploadItem());//アップロードファイルをワークブックに読み込み

         this.Gen_Cmd_Upload_Init();                                                                    // インポート情報を初期化
         this.Gen_Cmd_Upload_Check(workbook);                                                           // データ妥当性チェックおよび取込
         this.Gen_Cmd_Upload_Import();                                                                  //アップロードファイルのデータをセット
         importUtil.deleteTempFile(fomInvn.getFomInvnImport().getImportBean());                         // テンプレートファイルの実体を削除
     }
	 catch (Exception ex){
	    	this.soPrmInvn.siRet = 1;                                                                   //Invalid
	        ex.printStackTrace();
	        soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005 + " ※ ");                         //Error
	 }
  }

  //======================================================================================
  //   ファイルアップロード/初期処理
  //   Parameter :
  //   Return    :
  //   Note      :インポート点数情報を初期化する
  //======================================================================================
  public void Gen_Cmd_Upload_Init(){


//      for (int i = 0; i < jtestten2ListForm.getResultData().size(); i++) {
//          Jtestten2ListData data = (Jtestten2ListData) jtestten2ListForm
//                  .getResultData().get(i);
//          for (int kyoukaCnt = 0; kyoukaCnt < data.getKyoukaTenList().size(); kyoukaCnt++) {
//              Jtestten2KyoukaTenData kyoukaTenData = (Jtestten2KyoukaTenData) data.getKyoukaTenList().get(kyoukaCnt);
//             kyoukaTenData.setImportTen("");
//             kyoukaTenData.setImportFlg(false);
//          }
//      }


	 try{
          //初期化
	      for (int i = 0; i < fomInvn.getResultData().size(); i++) {

	    	  FomInvnBody aoFomInvnBody = (FomInvnBody) fomInvn.getResultData().get(i);

               //for (int kyoukaCnt = 0; kyoukaCnt < aoFomInvnBody.getKyoukaTenList().size(); kyoukaCnt++) {
               //    Jtestten2KyoukaTenData kyoukaTenData = (Jtestten2KyoukaTenData) aoFomInvnBody.getKyoukaTenList().get(kyoukaCnt);
               //    aoFomInvnBody.setImportTen("");
               //    aoFomInvnBody.setImportFlg(false);
               //}

          }
     }
	 catch (Exception ex){
	    	this.soPrmInvn.siRet = 1;                                                                  //Invalid
	        ex.printStackTrace();
	        soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005 + " ※ ");                        //Error
	 }
  }
  //======================================================================================
  //   ファイルアップロード/検査、取り込み
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  public void Gen_Cmd_Upload_Check( HSSFWorkbook workbook){

  /*

   HSSFWorkbook workbook) throws ClException {

   PoiEngine poiEngine = new PoiEngine();
   int importDataCount = 0;
   int errorDataCount = 0;
   ArrayList<?> listImportData = null;
   ArrayList<ImportErrorListData> listErrorData = new ArrayList<ImportErrorListData>();
   Jtestten2ImportBean jtestten2ImportBean = jtestten2ListForm
           .getJtestten2ImportBean();
   HSSFSheet sheet = null;


   try {
       sheet = workbook.getSheetAt(0);

   } catch (Exception e) {
       // シートの取得に失敗した場合は、エラーを出力して処理を中断
       ImportErrorListData errData = new ImportErrorListData();
       errData.setRowCount(6); // 行番号(ヘッダー行番号)
       errData.setRecordString(""); // レコード文字列
       errData.setErrorMessage(Messages
               .getString("jTestTenList.sheet1Error")); // エラーメッセージ
       errorDataCount++;
       listErrorData.add(errData);
       jtestten2ImportBean.getImportBean()
               .setListImportDataRecord(listImportData);
       jtestten2ImportBean.getImportBean()
               .setListImportErrorRecord(listErrorData);
       jtestten2ImportBean.getImportBean()
               .setImportRecortCount(importDataCount);
       jtestten2ImportBean.getImportBean()
               .setErrorRecordCount(errorDataCount);
       return;
   }
   if (workbook != null) {
       if (!checkHeader(jtestten2ListForm, sheet, poiEngine)) {
           // ヘッダーの内容が正しくない場合はエラー 異常の場合は、読み飛ばしデータに格納
           ImportErrorListData errData = new ImportErrorListData();
           errData.setRowCount(6); // 行番号(ヘッダー行番号)
           errData.setRecordString(""); // レコード文字列
           errData.setErrorMessage(Messages
                   .getString("jTestTenList.headerError")); // エラーメッセージ
           errorDataCount++;
           listErrorData.add(errData);
       } else if (!checkTitle(jtestten2ListForm, sheet, poiEngine)) {
           // タイトルの内容が正しくない場合はエラー 異常の場合は、読み飛ばしデータに格納
           ImportErrorListData errData = new ImportErrorListData();
           errData.setRowCount(8); // 行番号(ヘッダー行番号)
           errData.setRecordString(""); // レコード文字列
           errData.setErrorMessage(Messages
                   .getString("jTestTenList.titleError")); // エラーメッセージ
           errorDataCount++;
           listErrorData.add(errData);
       } else {
           int rowNo = 8; // 検索行初期設定（データ開始行）
           int lastRowCount = sheet.getLastRowNum(); // シートの最終行取得

           while (rowNo <= lastRowCount) {
               boolean dataCheck = false;
               boolean skipCheck = false;
               String errorMessage = "";
               String gakunen = poiEngine.getCellString(sheet, rowNo, 1);
               String gakkyu = poiEngine.getCellString(sheet, rowNo, 2);
               String seiriNo = poiEngine.getCellString(sheet, rowNo, 3);
               // 学年が空白の場合はデータ終了とみなし処理を中断する。
               if ("".equals(gakunen) || "".equals(gakkyu)
                       || "".equals(seiriNo)) {
                   rowNo++;
                   continue;
               } else {
                   // データ格納
                   ArrayList<String> listKyoukaTensu = new ArrayList<String>(); // 教科毎得点情報
                   for (int kyoukaCnt = 0; kyoukaCnt < jtestten2ListForm.getKyoukaNmList().size(); kyoukaCnt++) {
                       listKyoukaTensu.add(poiEngine.getCellString(sheet,rowNo, 5 + kyoukaCnt));
                   }
                   // 学年・学級・出席番号の存在チェック
                   int index = checkGakunenGakkyuSeiriBango(jtestten2ListForm,gakunen,gakkyu,seiriNo);
                   if (index != -1) {
                       // 点数が妥当かチェック
                       StringBuffer sbMessage = new StringBuffer("");
                       // 教科毎の点数の妥当性チェック
                       for (int kyoukaCnt = 0; kyoukaCnt < jtestten2ListForm .getKyoukaNmList().size(); kyoukaCnt++) {
                           String kyoukaSoTen = listKyoukaTensu.get(kyoukaCnt).toString();
                           sbMessage.append(checkSoten(100, kyoukaSoTen));
                       }
                       if ("".equals(sbMessage.toString())) {
                           // エラーがなかった場合はデータ格納
                           Jtestten2ListData jtestten2ListData = (Jtestten2ListData) jtestten2ListForm
                                   .getResultData().get(index);
                           for (int kyoukaCnt = 0; kyoukaCnt < jtestten2ListForm
                                   .getKyoukaNmList().size(); kyoukaCnt++) {
                               String kantenSoTen = listKyoukaTensu
                                       .get(kyoukaCnt).toString();
                               Jtestten2KyoukaTenData jtestten2KyoukaTenData = (Jtestten2KyoukaTenData) jtestten2ListData
                                       .getKyoukaTenList().get(kyoukaCnt);
                               jtestten2KyoukaTenData.setImportFlg(true);
                               jtestten2KyoukaTenData.setImportFlg(true);
                               jtestten2KyoukaTenData
                                       .setImportTen(kantenSoTen);
                           }
                           dataCheck = true;
                       } else {
                           errorMessage = errorMessage
                                   + sbMessage.toString();
                           dataCheck = false;
                       }
                   } else {
                       skipCheck = true;
                   }
                   if (!skipCheck) {
                       if (dataCheck) {
                           importDataCount++;
                       } else {
                           // 異常の場合は、読み飛ばしデータに格納
                           ImportErrorListData errData = new ImportErrorListData();
                           errData.setRowCount(rowNo + 1); // 行番号
                           errData.setRecordString(""); // レコード文字列
                           errData.setErrorMessage(errorMessage); // エラーメッセージ
                           errorDataCount++;
                           listErrorData.add(errData);
                       }
                   }
               }
               rowNo++;
           }
       }
   }
   // 該当するデータが1件も存在しない場合、エラーを出力する。
   if (errorDataCount == 0 && importDataCount == 0) {
       errorDataCount++;
       ImportErrorListData errData = new ImportErrorListData();
       errData.setRowCount(0); // 行番号
       errData.setErrorMessage(Messages.getString("importError.notData")); // エラーメッセージ
       listErrorData.add(errData);
   }
   // データ格納
   jtestten2ImportBean.getImportBean()
           .setListImportDataRecord(listImportData);
   jtestten2ImportBean.getImportBean()
           .setListImportErrorRecord(listErrorData);
   jtestten2ImportBean.getImportBean()
           .setImportRecortCount(importDataCount);
   jtestten2ImportBean.getImportBean().setErrorRecordCount(errorDataCount);
*/
/* ----------------------------------------------------------------------------------------------------- */
	  PoiEngine                        poiEngine                                     = new PoiEngine();
	  int                              importDataCount                               = 0;
	  int                              errorDataCount                                = 0;
	  ArrayList<?>                     listImportData                                = null;
	  ArrayList<ImportErrorListData>   listErrorData                                 = new ArrayList<ImportErrorListData>();
	  FomInvnImport                    fomInvnImport                                 = fomInvn.getFomInvnImport();
	  HSSFSheet                        sheet                                         = null;

      try {

    	  sheet = workbook.getSheetAt(0);                                                            //アップロードデータワークシート取得

      } catch (Exception e) {

     	  // シートの取得に失敗した場合は、エラーを出力して処理を中断
          ImportErrorListData errData = new ImportErrorListData();

          errData.setRowCount(6);                                                                    // 行番号(ヘッダー行番号)
          errData.setRecordString("");                                                               // レコード文字列
          errData.setErrorMessage(Messages.getString("jTestTenList.sheet1Error"));                   // エラーメッセージ
          errorDataCount++;

          listErrorData.add(errData);

          fomInvnImport.getImportBean().setListImportDataRecord(listImportData);
          fomInvnImport.getImportBean().setImportRecortCount(importDataCount);

          fomInvnImport.getImportBean().setListImportErrorRecord(listErrorData);
          fomInvnImport.getImportBean().setErrorRecordCount(errorDataCount);

          return;
      }

      //シートの妥当性検査
/*
      if (workbook != null) {
          if (!checkHeader(jtestten2ListForm, sheet, poiEngine)) {
              // ヘッダーの内容が正しくない場合はエラー 異常の場合は、読み飛ばしデータに格納
              ImportErrorListData errData = new ImportErrorListData();
              errData.setRowCount(6);                                                               // 行番号(ヘッダー行番号)
              errData.setRecordString("");                                                          // レコード文字列
              errData.setErrorMessage(Messages.getString("jTestTenList.headerError"));              // エラーメッセージ
              errorDataCount++;
              listErrorData.add(errData);
          } else if (!checkTitle(jtestten2ListForm, sheet, poiEngine)) {
              // タイトルの内容が正しくない場合はエラー 異常の場合は、読み飛ばしデータに格納
              ImportErrorListData errData = new ImportErrorListData();
              errData.setRowCount(8);                                                               // 行番号(ヘッダー行番号)
              errData.setRecordString("");                                                          // レコード文字列
              errData.setErrorMessage(Messages.getString("jTestTenList.titleError"));               // エラーメッセージ
              errorDataCount++;
              listErrorData.add(errData);
          } else {
*/
              int rowNo        = 9;                                                                 // 検索行初期設定（データ開始行）
              int lastRowCount = sheet.getLastRowNum();                                             // シートの最終行取得

              int index        = 0;

              //アップロードデータ取得
              while (rowNo <= lastRowCount) {

            	  boolean dataCheck    = false;
                  boolean skipCheck    = false;

                  String errorMessage  = "";

                  String gakunen       = poiEngine.getCellString(sheet, rowNo, 2);                 //CD
                  String gakkyu        = poiEngine.getCellString(sheet, rowNo, 3);                 //名1
                  String seiriNo       = poiEngine.getCellString(sheet, rowNo, 4);                 //名2


                  // 空白の場合はデータ終了とみなし処理を中断する。
                  if ("".equals(gakunen) || "".equals(gakkyu) || "".equals(seiriNo)) {
                      rowNo++;
                      continue;
                  } else {

                	  // データ格納
                      //ArrayList<String> listKyoukaTensu = new ArrayList<String>(); // 教科毎得点情報
                      //for (int kyoukaCnt = 0; kyoukaCnt < jtestten2ListForm.getKyoukaNmList().size(); kyoukaCnt++) {
                      //    listKyoukaTensu.add(poiEngine.getCellString(sheet,rowNo, 5 + kyoukaCnt));
                      //}

                      // 学年・学級・出席番号の存在チェック
                      //int index = checkGakunenGakkyuSeiriBango(jtestten2ListForm, gakunen, gakkyu, seiriNo);

                      //if (index != -1) {
                          // 点数が妥当かチェック
                          //StringBuffer sbMessage = new StringBuffer("");
                          // 教科毎の点数の妥当性チェック
                          //for (int kyoukaCnt = 0; kyoukaCnt < jtestten2ListForm.getKyoukaNmList().size(); kyoukaCnt++) {
                          //    String kyoukaSoTen = listKyoukaTensu.get(kyoukaCnt).toString();
                          //    sbMessage.append(checkSoten(100, kyoukaSoTen));
                          //}

                          //if ("".equals(sbMessage.toString())) {


                        	  // エラーがなかった場合はデータ格納
                              FomInvnBody formInvnBody = (FomInvnBody) fomInvn.getResultData().get(index);

                              formInvnBody.setDescription1(gakkyu);                                //名1

                              index = index +1;

                              //for (int kyoukaCnt = 0; kyoukaCnt < fomInvn.getKyoukaNmList().size(); kyoukaCnt++) {
                              //    String kantenSoTen = listKyoukaTensu.get(kyoukaCnt).toString();
                              //    Jtestten2KyoukaTenData jtestten2KyoukaTenData = (Jtestten2KyoukaTenData) formInvnBody.getKyoukaTenList().get(kyoukaCnt);
                              //    jtestten2KyoukaTenData.setImportFlg(true);
                              //    jtestten2KyoukaTenData.setImportFlg(true);
                              //    jtestten2KyoukaTenData.setImportTen(kantenSoTen);
                              //}

                              //dataCheck = true;

                          //} else {
                          //    errorMessage = errorMessage + sbMessage.toString();
                          //    dataCheck = false;
                          //}

                     // } else {
                     //     skipCheck = true;
                     // }
                     // if (!skipCheck) {
                     //     if (dataCheck) {

                               importDataCount++;                                                             //アップロードデータ件数（正常）

                      //     } else {
                              // 異常の場合は、読み飛ばしデータに格納
                      //        ImportErrorListData errData = new ImportErrorListData();
                      //        errData.setRowCount(rowNo + 1);                                               // 行番号
                      //        errData.setRecordString("");                                                  // レコード文字列
                      //        errData.setErrorMessage(errorMessage);                                        // エラーメッセージ
                      //        errorDataCount++;
                      //        listErrorData.add(errData);
                      //    }
                      //}
                  }

                  rowNo++;
              }

          //}
      //}


      // 該当するデータが1件も存在しない場合、エラーを出力する。
      if ( errorDataCount == 0 && importDataCount == 0 ) {
          errorDataCount++;
          ImportErrorListData errData = new ImportErrorListData();
          errData.setRowCount(0);                                                                      // 行番号
          errData.setErrorMessage(Messages.getString("importError.notData"));                          // エラーメッセージ
          listErrorData.add(errData);
      }

	  // データ格納
      fomInvnImport.getImportBean().setListImportDataRecord(listImportData);
      fomInvnImport.getImportBean().setImportRecortCount(importDataCount);

      fomInvnImport.getImportBean().setListImportErrorRecord(listErrorData);
      fomInvnImport.getImportBean().setErrorRecordCount(errorDataCount);

      // テンプレートファイルの実体を削除
      //importUtil.deleteTempFile(fomInvn.getFomInvnImport().getImportBean());                                // 添付ファイル削除

  }
  //======================================================================================
  //   ファイルアップロード/取り込み
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  public void Gen_Cmd_Upload_Import(){

      try {
    	   // データ格納
           //FomInvnImport.getImportBean().setListImportDataRecord(listImportData);
           //FomInvnImport.getImportBean().setListImportErrorRecord(listErrorData);
           //FomInvnImport.getImportBean().setImportRecortCount(importDataCount);
           //FomInvnImport.getImportBean().setErrorRecordCount(errorDataCount);

           // テンプレートファイルの実体を削除
           //importUtil.deleteTempFile(fomInvn.getFomInvnImport().getImportBean());                    // 添付ファイル削除
      }
	  catch (Exception ex){
	    	this.soPrmInvn.siRet = 1;                                                                  //Invalid
	        ex.printStackTrace();
	        soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005 + " ※ ");                        //Error
	 }
  }

  //======================================================================================
  //   ファイルアップロード/明細画面へ取り込み
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  public void Gen_Cmd_ViewBody_Import(){


  //private void importJtestten2(Jtestten2ListForm jtestten2ListForm) throws ClException {

  /*
   * 点数データを、メイン画面に反映する
   */
  // 教科毎の点数をセット

/*
  for (int i = 0; i < jtestten2ListForm.getResultData().size(); i++) {
      Jtestten2ListData bean = (Jtestten2ListData) jtestten2ListForm
              .getResultData().get(i);
      for (int kyoukaCnt = 0; kyoukaCnt < bean.getKyoukaTenList().size(); kyoukaCnt++) {
          Jtestten2KyoukaTenData kyoukaTenBean = (Jtestten2KyoukaTenData) bean
                  .getKyoukaTenList().get(kyoukaCnt);
          if (kyoukaTenBean.isImportFlg()) {
              if (!kyoukaTenBean.getSoTen()
                      .equals(kyoukaTenBean.getImportTen())) {
                  kyoukaTenBean.setSoTen(kyoukaTenBean.getImportTen());
                  kyoukaTenBean.setChangeFlg(true);
                  kyoukaTenBean.setStyle("changePart");
                  jtestten2ListForm.setChangeFlg(true);
              }
          }
      }
  }
*/
  // 合計点再計算
  //MaximumScale maximumScale = new MaximumScale();
  //maximumScale.calculateMaximumScale(jtestten2ListForm);
 }

  //======================================================================================
  //   ファイルアップロードキャンセル
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  public void Gen_Cmd_Upload_Cansel(){

/*
	  public class Jtestten2ImportOutputCancelProcess extends BaseProcess {

		    @Override
		    public void execute() throws ClException {

		        Jtestten2ListForm jtestten2ListForm = (Jtestten2ListForm) form;
		        ImportBean importBean = jtestten2ListForm.getJtestten2ImportBean().getImportBean();
		        ImportUtil importUtil = new ImportUtil();
		        importUtil.clearOutputData(importBean);
		        setActionForwardName("");

		    }
*/
     try{
	        ImportBean importBean = fomInvn.getFomInvnImport().getImportBean();
	        ImportUtil importUtil = new ImportUtil();
	        importUtil.clearOutputData(importBean);

     }
	 catch (Exception ex){
	    	this.soPrmInvn.siRet = 1;                                                                   //Invalid
	        ex.printStackTrace();
	        soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005 + " ※ ");                         //Error
	 }
  }

  //======================================================================================
  //   データ更新処理
  //   Parameter :
  //   Return    :
  //   Note      :
  //======================================================================================
  public void Gen_Cmd_Update(){

	  try{
		    //
	        soItfActionUpdate           = soMdlInvnUpdate.getProcClass(gctUpdate);                     //内部クラス取得
	        soItfActionUpdate.Gen_Update();                                                            //内部クラスのメソッド実行
     }
	  catch (Exception ex){
	    	this.soPrmInvn.siRet = 1;                                                                  //Invalid
	        ex.printStackTrace();
	        soList.add(ex); super.Gen_Err(soList,gctComon_Err_000005 + " ※ ");                        //Error
	 }
  }


}
