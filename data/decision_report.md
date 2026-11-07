# Decision Report

- generated_at: 2026-11-07T04:21:30.091023+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18352**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18352, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.81% | **-1.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.30% | **+0.45%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_BB3S | 3/19 | 15.8% | +0.91% | **+0.14%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.20% | **+0.07%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.67% | **+1.84%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.97% | **+1.78%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +4.35% | **+1.52%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.89% | **+1.23%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.34% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,478.48** / 初期 $100.00 (+1378.48%)
- 確定: 7048件 (Win 2026 / Loss 2249 / Flat 2773) / skip 7865件
- 成長率目線: 平均log +0.000382 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,478.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$388.82** / 初期 $100.00 (+288.82%)
- 確定: 4718件 (Win 1269 / Loss 1040 / Flat 2409) / skip 7045件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0133 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $388.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6512件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000120 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-07T04:21:14.909405+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=75840.0
- Funnel: target 1089 → liquid 154 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +42.80% | $5,240,450.51 |
| AKE/USDT:USDT | +25.36% | $62,500,513.08 |
| ONE/USDT:USDT | +20.38% | $14,755,444.04 |
| LYN/USDT:USDT | +18.44% | $1,803,137.48 |
| BTW/USDT:USDT | +14.21% | $6,812,536.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MVLL/USDT:USDT | below_1h_threshold | +1.04% | +1.06% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.65% | +0.68% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +0.65% | +0.67% |
| DRAM/USDT:USDT | below_1h_threshold | +0.53% | +0.56% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.53% | +0.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
