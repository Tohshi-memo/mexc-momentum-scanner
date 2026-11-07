# Decision Report

- generated_at: 2026-11-07T06:01:13.696550+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18360**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18360, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.49% | **-1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +4.07% | **+1.02%** |
| LIMIT_3PCT | 16/20 | 80.0% | +1.11% | **+0.89%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.85% | **+2.42%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.89% | **+1.88%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.86% | **+1.71%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.30% | **+1.32%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.49% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,484.17** / 初期 $100.00 (+1384.17%)
- 確定: 7056件 (Win 2029 / Loss 2252 / Flat 2775) / skip 7865件
- 成長率目線: 平均log +0.000382 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,484.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$392.38** / 初期 $100.00 (+292.38%)
- 確定: 4726件 (Win 1272 / Loss 1041 / Flat 2413) / skip 7045件
- 成長率目線: 平均log +0.000289 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0745 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $392.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6520件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000284 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-07T06:01:03.629480+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=75992.9
- Funnel: target 1089 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +54.79% | $7,516,604.96 |
| AKE/USDT:USDT | +54.05% | $61,553,479.97 |
| LYN/USDT:USDT | +20.87% | $1,868,540.63 |
| ONE/USDT:USDT | +20.17% | $15,850,319.83 |
| CLSKSTOCK/USDT:USDT | +6.74% | $1,057,112.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +1.57% | +1.57% |
| LYN/USDT:USDT | below_1h_threshold | +0.77% | +0.77% |
| AGT/USDT:USDT | below_1h_threshold | +0.36% | +0.36% |
| UVXY/USDT:USDT | below_1h_threshold | +0.31% | +0.31% |
| NGAS/USDT:USDT | below_1h_threshold | +0.23% | +0.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
