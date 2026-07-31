# Decision Report

- generated_at: 2026-07-31T07:46:30.260869+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9973**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9973, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.14% | **+0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.44% | **+0.97%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.14% | **+0.92%** |
| LIMIT_10PCT | 2/20 | 10.0% | +7.36% | **+0.74%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.08% | **+0.42%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.92% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 10/10 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.97% | **+0.92%** |
| MARKET_LONG | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.57% | **+0.46%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.48% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$558.49** / 初期 $100.00 (+458.49%)
- 確定: 3564件 (Win 1139 / Loss 1161 / Flat 1264) / skip 2970件
- 成長率目線: 平均log +0.000483 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $558.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.57** / 初期 $100.00 (+42.57%)
- 確定: 1267件 (Win 357 / Loss 291 / Flat 619) / skip 2117件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1481 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $142.57

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.56** / 初期 $100.00 (+10.56%)
- 確定: 810件 (Win 263 / Loss 322 / Flat 225) / pending 6件 / skip 634件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000424 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $110.56

## 6. Latest Market Context

- 更新: 2026-07-31T07:46:22.530576+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.45% price=63916.8
- Funnel: target 920 → liquid 177 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.2 >= 65=1, 4h RSI 97.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +67.76% | $10,729,472.31 |
| GIGGLE/USDT:USDT | +36.12% | $3,174,040.35 |
| AXTISTOCK/USDT:USDT | +33.23% | $4,587,927.57 |
| MMT/USDT:USDT | +30.45% | $12,263,369.77 |
| BULLA/USDT:USDT | +29.34% | $1,295,410.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +3.88% | +4.34% |
| SAND/USDT:USDT | below_1h_threshold | +3.46% | +3.91% |
| CAP/USDT:USDT | below_1h_threshold | +3.22% | +3.68% |
| CFX/USDT:USDT | below_1h_threshold | +2.10% | +2.56% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.15% | +1.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
