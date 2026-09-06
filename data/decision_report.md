# Decision Report

- generated_at: 2026-09-06T00:51:33.609023+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13786**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13786, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.27% | **-0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.63% | **+0.19%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 2/13 | 15.4% | -1.31% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +2.09% | **+1.19%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.34% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$867.34** / 初期 $100.00 (+767.34%)
- 確定: 5092件 (Win 1528 / Loss 1660 / Flat 1904) / skip 5255件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARB/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $867.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.57** / 初期 $100.00 (+88.57%)
- 確定: 2531件 (Win 705 / Loss 599 / Flat 1227) / skip 4666件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0421 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $188.57

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.11** / 初期 $100.00 (+20.11%)
- 確定: 2403件 (Win 715 / Loss 911 / Flat 777) / pending 5件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000326 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARB/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $120.11

## 6. Latest Market Context

- 更新: 2026-09-06T00:51:20.626071+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=79830.0
- Funnel: target 1050 → liquid 125 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.6 >= 65=1, 4h RSI 76.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +45.40% | $89,907,779.59 |
| BASECAT/USDT:USDT | +23.12% | $2,009,962.53 |
| MAGMA/USDT:USDT | +20.34% | $2,503,317.14 |
| SUSHI/USDT:USDT | +19.40% | $3,898,192.78 |
| UAI/USDT:USDT | +13.86% | $6,924,259.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENA/USDT:USDT | below_1h_threshold | +4.46% | +4.42% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.90% | +3.86% |
| STRK/USDT:USDT | below_1h_threshold | +2.76% | +2.72% |
| AAVE/USDT:USDT | below_1h_threshold | +2.75% | +2.71% |
| APT/USDT:USDT | below_1h_threshold | +2.07% | +2.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
