# Decision Report

- generated_at: 2026-08-08T23:21:18.824504+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10894**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.97% / filled 20/20。**
- 全期間 MARKET基準: n=10894, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.97% | **+0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.67% | **+1.58%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.26% | **+1.01%** |
| MARKET | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.51% | **+0.33%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.09% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.06% | **+0.83%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.67% | **+0.33%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.07% | **-0.04%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -0.69% | **-0.28%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | -0.57% | **-0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$636.22** / 初期 $100.00 (+536.22%)
- 確定: 3895件 (Win 1224 / Loss 1269 / Flat 1402) / skip 3560件
- 成長率目線: 平均log +0.000475 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $636.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2794件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0387 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.55** / 初期 $100.00 (+17.55%)
- 確定: 1247件 (Win 390 / Loss 479 / Flat 378) / pending 1件 / skip 1123件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000110 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FORM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.03% 残高後 $117.55

## 6. Latest Market Context

- 更新: 2026-08-08T23:21:10.736491+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64932.0
- Funnel: target 961 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +51.63% | $21,379,283.69 |
| COOKIE/USDT:USDT | +26.38% | $2,786,992.96 |
| CYS/USDT:USDT | +16.11% | $31,024,145.09 |
| BTW/USDT:USDT | +15.86% | $15,806,990.47 |
| SAGA/USDT:USDT | +15.26% | $1,174,032.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_1h_threshold | +3.66% | +3.64% |
| BLUAI/USDT:USDT | below_1h_threshold | +3.04% | +3.02% |
| BICO/USDT:USDT | below_1h_threshold | +2.05% | +2.02% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.95% | +0.92% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.91% | +0.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
