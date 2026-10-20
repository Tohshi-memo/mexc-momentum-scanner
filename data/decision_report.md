# Decision Report

- generated_at: 2026-10-20T10:36:29.001195+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17055**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17055, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.00% | **+0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.24% | **+0.52%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.61% | **+0.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 10/10 | 100.0% | +2.64% | **+2.64%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.35% | **+1.88%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.89% | **+1.61%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.63% | **+1.22%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.51% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$121.36** / 初期 $100.00 (+21.36%)
- 確定トレード: 247件 (TP 91 / SL 149 / EXP 7)
- 最新: BAT/USDT:USDT SL_HIT PnL -3.97% 残高後 $121.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,324.12** / 初期 $100.00 (+1224.12%)
- 確定: 6481件 (Win 1885 / Loss 2068 / Flat 2528) / skip 7135件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $1,324.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$282.23** / 初期 $100.00 (+182.23%)
- 確定: 3803件 (Win 1046 / Loss 886 / Flat 1871) / skip 6663件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0657 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $282.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5215件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000274 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T10:36:17.129752+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=81488.8
- Funnel: target 1078 → liquid 161 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.8 >= 65=1, 4h RSI 69.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +89.47% | $8,730,604.95 |
| ALT/USDT:USDT | +26.76% | $1,864,985.87 |
| PHA/USDT:USDT | +18.40% | $19,222,588.36 |
| BR/USDT:USDT | +15.87% | $48,327,002.76 |
| A/USDT:USDT | +11.86% | $23,224,543.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +2.82% | +2.77% |
| APR/USDT:USDT | below_1h_threshold | +2.19% | +2.15% |
| CHIP/USDT:USDT | below_1h_threshold | +1.73% | +1.68% |
| PHA/USDT:USDT | below_1h_threshold | +0.91% | +0.86% |
| ZRO/USDT:USDT | below_1h_threshold | +0.64% | +0.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
