# Decision Report

- generated_at: 2026-11-07T08:36:22.192518+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18362**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18362, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.89% | **-0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.45% | **+1.09%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.09% | **+0.62%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.47% | **+2.22%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.39% | **+1.68%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.33% | **+1.51%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.49% | **+1.12%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.84% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,469.37** / 初期 $100.00 (+1369.37%)
- 確定: 7058件 (Win 2029 / Loss 2254 / Flat 2775) / skip 7865件
- 成長率目線: 平均log +0.000381 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,469.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.01** / 初期 $100.00 (+291.01%)
- 確定: 4728件 (Win 1272 / Loss 1042 / Flat 2414) / skip 7045件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0693 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARIA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $391.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000199 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-07T08:36:11.626476+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=76083.3
- Funnel: target 1089 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +56.46% | $61,778,964.57 |
| AIN/USDT:USDT | +45.30% | $8,285,356.87 |
| ONE/USDT:USDT | +21.17% | $17,295,708.09 |
| LYN/USDT:USDT | +9.76% | $1,862,780.92 |
| ARIA/USDT:USDT | +7.74% | $1,312,410.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +1.54% | +1.50% |
| IDOL/USDT:USDT | below_1h_threshold | +0.46% | +0.42% |
| MUU/USDT:USDT | below_1h_threshold | +0.44% | +0.40% |
| UNI/USDT:USDT | below_1h_threshold | +0.41% | +0.37% |
| LSK/USDT:USDT | below_1h_threshold | +0.35% | +0.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
