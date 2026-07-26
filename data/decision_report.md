# Decision Report

- generated_at: 2026-07-26T20:01:13.863509+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9582**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.17% / filled 20/20。**
- 全期間 MARKET基準: n=9582, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.17% | **+2.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.77% | **+2.63%** |
| MARKET | 20/20 | 100.0% | +2.17% | **+2.17%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.62% | **+1.05%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.69% | **+0.38%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.47% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.13% | **+0.53%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -0.03% | **-0.02%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | -0.10% | **-0.04%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.19% | **-0.12%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | -0.28% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$105.87** / 初期 $100.00 (+5.87%)
- 確定トレード: 141件 (TP 48 / SL 88 / EXP 5)
- 最新: ESPORTS/USDT:USDT TP_HIT PnL +8.00% 残高後 $105.87
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$452.56** / 初期 $100.00 (+352.56%)
- 確定: 3399件 (Win 1078 / Loss 1106 / Flat 1215) / skip 2744件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $452.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.72** / 初期 $100.00 (+37.72%)
- 確定: 1222件 (Win 338 / Loss 274 / Flat 610) / skip 1771件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0683 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.21** / 初期 $100.00 (+8.21%)
- 確定: 616件 (Win 207 / Loss 238 / Flat 171) / pending 0件 / skip 437件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000171 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.11% 残高後 $108.21

## 6. Latest Market Context

- 更新: 2026-07-26T20:01:07.006380+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64668.8
- Funnel: target 898 → liquid 120 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +11.21% | $18,181,021.07 |
| UB/USDT:USDT | +9.27% | $1,259,400.21 |
| CROSS/USDT:USDT | +8.33% | $1,629,328.52 |
| ESP/USDT:USDT | +5.55% | $3,183,367.04 |
| BANK/USDT:USDT | +4.88% | $70,499,096.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHIB/USDT:USDT | below_1h_threshold | +0.47% | +0.47% |
| USOIL/USDT:USDT | below_1h_threshold | +0.42% | +0.41% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.41% | +0.40% |
| PRL/USDT:USDT | below_1h_threshold | +0.41% | +0.40% |
| DIA/USDT:USDT | below_1h_threshold | +0.29% | +0.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
