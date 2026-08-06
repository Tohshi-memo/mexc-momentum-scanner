# Decision Report

- generated_at: 2026-08-06T11:36:26.514367+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10586**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10586, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.18% | **-1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.42% | **+0.64%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.81% | **+0.57%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.98% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.80% | **+2.38%** |
| MARKET_LONG | 20/20 | 100.0% | +2.06% | **+2.06%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.47% | **+1.48%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.18% | **+1.09%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +2.73% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定トレード: 175件 (TP 67 / SL 103 / EXP 5)
- 最新: COTI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.05
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$596.41** / 初期 $100.00 (+496.41%)
- 確定: 3795件 (Win 1203 / Loss 1249 / Flat 1343) / skip 3352件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $596.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$145.06** / 初期 $100.00 (+45.06%)
- 確定: 1420件 (Win 396 / Loss 332 / Flat 692) / skip 2577件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0513 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $145.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1146件 (Win 365 / Loss 448 / Flat 333) / pending 0件 / skip 918件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000216 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-06T11:36:14.194090+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64601.9
- Funnel: target 955 → liquid 188 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HFT/USDT:USDT | +66.45% | $4,441,632.85 |
| HEI/USDT:USDT | +59.50% | $72,883,567.66 |
| CTSI/USDT:USDT | +55.68% | $1,507,359.00 |
| BLESS/USDT:USDT | +49.18% | $120,919,579.55 |
| CASHCAT/USDT:USDT | +45.24% | $1,376,317.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CTSI/USDT:USDT | below_1h_threshold | +4.37% | +4.35% |
| BTW/USDT:USDT | below_1h_threshold | +4.24% | +4.22% |
| CYS/USDT:USDT | below_1h_threshold | +2.20% | +2.19% |
| RESOLV/USDT:USDT | below_1h_threshold | +2.06% | +2.04% |
| ZRO/USDT:USDT | below_1h_threshold | +1.81% | +1.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
