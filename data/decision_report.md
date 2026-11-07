# Decision Report

- generated_at: 2026-11-07T23:01:05.251135+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18401**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18401, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.37% | **+0.48%** |
| LIMIT_10PCT | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_6PCT | 13/20 | 65.0% | +0.13% | **+0.08%** |
| LIMIT_5PCT | 13/20 | 65.0% | -0.09% | **-0.06%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +3.38% | **+2.20%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +3.71% | **+2.04%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.27% | **+1.71%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.94% | **+1.36%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,541.03** / 初期 $100.00 (+1441.03%)
- 確定: 7097件 (Win 2041 / Loss 2266 / Flat 2790) / skip 7865件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,541.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4754件 (Win 1277 / Loss 1047 / Flat 2430) / skip 7058件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0813 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6559件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000434 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-07T23:00:56.895253+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=75696.1
- Funnel: target 1089 → liquid 116 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +205.97% | $5,382,202.37 |
| MET/USDT:USDT | +7.23% | $1,200,417.12 |
| ESPORTS/USDT:USDT | +7.13% | $1,248,553.78 |
| BTW/USDT:USDT | +6.25% | $5,994,455.04 |
| AERO/USDT:USDT | +4.63% | $1,160,475.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +0.29% | +0.36% |
| UAI/USDT:USDT | below_1h_threshold | +0.16% | +0.23% |
| MUU/USDT:USDT | below_1h_threshold | +0.15% | +0.22% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.10% | +0.17% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.10% | +0.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
