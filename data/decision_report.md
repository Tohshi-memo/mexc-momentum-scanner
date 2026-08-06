# Decision Report

- generated_at: 2026-08-06T12:46:43.866374+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10604**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10604, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.13% | **-1.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.74% | **+0.52%** |
| LIMIT_5PCT | 14/20 | 70.0% | +0.39% | **+0.28%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.24% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.95% | **+2.37%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.59% | **+2.07%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +5.41% | **+1.89%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +5.11% | **+1.79%** |
| MARKET_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |

## 2. $100 Live Portfolio

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定トレード: 175件 (TP 67 / SL 103 / EXP 5)
- 最新: COTI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.05
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$596.41** / 初期 $100.00 (+496.41%)
- 確定: 3795件 (Win 1203 / Loss 1249 / Flat 1343) / skip 3370件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $596.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.70** / 初期 $100.00 (+44.70%)
- 確定: 1434件 (Win 400 / Loss 339 / Flat 695) / skip 2581件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0472 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $144.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1146件 (Win 365 / Loss 448 / Flat 333) / pending 0件 / skip 934件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000259 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-06T12:46:28.336842+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=64505.4
- Funnel: target 955 → liquid 191 → pre 50 → checked 50 → surge 6 → strict 1
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.8 >= 65=1, 4h RSI 82.2 >= 65=1, 4h RSI 96.3 >= 65=1, 4h RSI 89.5 >= 65=1, 4h RSI 78.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CASHCAT/USDT:USDT | +78.56% | $1,743,987.74 |
| CTSI/USDT:USDT | +68.82% | $2,306,995.60 |
| HFT/USDT:USDT | +61.55% | $5,043,315.80 |
| ZBT/USDT:USDT | +51.17% | $3,908,611.41 |
| TAKE/USDT:USDT | +42.32% | $1,701,887.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +2.69% | +2.82% |
| TAKE/USDT:USDT | below_1h_threshold | +2.65% | +2.78% |
| MMT/USDT:USDT | below_1h_threshold | +2.15% | +2.28% |
| ROBO/USDT:USDT | below_1h_threshold | +1.80% | +1.93% |
| BTW/USDT:USDT | below_1h_threshold | +1.57% | +1.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
