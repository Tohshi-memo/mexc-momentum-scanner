# Decision Report

- generated_at: 2026-09-16T15:21:37.431485+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14702**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14702, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.17% | **+0.09%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +3.82% | **+3.44%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +4.13% | **+3.31%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.77% | **+2.77%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +3.82% | **+2.73%** |
| MARKET_LONG | 20/20 | 100.0% | +1.39% | **+1.39%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,187.55** / 初期 $100.00 (+1087.55%)
- 確定: 5579件 (Win 1674 / Loss 1803 / Flat 2102) / skip 5684件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,187.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$242.25** / 初期 $100.00 (+142.25%)
- 確定: 3106件 (Win 862 / Loss 734 / Flat 1510) / skip 5007件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1886 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $242.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.75** / 初期 $100.00 (+23.75%)
- 確定: 2955件 (Win 878 / Loss 1164 / Flat 913) / pending 1件 / skip 3220件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000590 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.75

## 6. Latest Market Context

- 更新: 2026-09-16T15:21:22.121522+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=75674.5
- Funnel: target 1059 → liquid 151 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +148.52% | $26,403,954.03 |
| BR/USDT:USDT | +129.24% | $34,164,479.41 |
| LSK/USDT:USDT | +55.01% | $29,931,508.17 |
| BULLA/USDT:USDT | +20.81% | $3,788,872.32 |
| HEI/USDT:USDT | +19.89% | $1,117,807.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +4.91% | +4.90% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.37% | +1.35% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.26% | +1.25% |
| RAY/USDT:USDT | below_1h_threshold | +1.15% | +1.13% |
| BR/USDT:USDT | below_1h_threshold | +1.13% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
