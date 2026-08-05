# Decision Report

- generated_at: 2026-08-05T09:56:25.294808+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10388**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10388, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.06% | **+0.74%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.49% | **+0.44%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.31% | **+0.22%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.17% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.21% | **+0.61%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.34% | **+0.60%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.29% | **+0.52%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.92% | **+0.29%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.03% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$611.41** / 初期 $100.00 (+511.41%)
- 確定: 3767件 (Win 1195 / Loss 1234 / Flat 1338) / skip 3182件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $611.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.75** / 初期 $100.00 (+43.75%)
- 確定: 1314件 (Win 371 / Loss 309 / Flat 634) / skip 2485件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0934 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $143.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.99** / 初期 $100.00 (+18.99%)
- 確定: 1130件 (Win 364 / Loss 436 / Flat 330) / pending 5件 / skip 727件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000312 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRVT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.99

## 6. Latest Market Context

- 更新: 2026-08-05T09:56:14.401230+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=64135.0
- Funnel: target 945 → liquid 184 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.3 >= 65=1, 4h RSI 81.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +80.95% | $35,833,469.99 |
| HEI/USDT:USDT | +68.65% | $19,359,990.34 |
| HFT/USDT:USDT | +58.84% | $3,172,987.96 |
| CASHCAT/USDT:USDT | +32.44% | $1,004,029.49 |
| SYN/USDT:USDT | +30.63% | $4,178,636.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +3.68% | +3.62% |
| SYN/USDT:USDT | below_1h_threshold | +3.37% | +3.31% |
| BLESS/USDT:USDT | below_1h_threshold | +3.19% | +3.13% |
| CAP/USDT:USDT | below_1h_threshold | +3.18% | +3.12% |
| 1000RATS/USDT:USDT | below_1h_threshold | +2.98% | +2.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
