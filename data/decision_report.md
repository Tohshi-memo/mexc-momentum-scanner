# Decision Report

- generated_at: 2026-07-04T11:52:18.168321+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8255**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8255, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| ASK | 20/20 | 100.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.24% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.78% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$325.39** / 初期 $100.00 (+225.39%)
- 確定: 2572件 (Win 810 / Loss 858 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000459 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $325.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1029件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0406 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T11:52:09.064810+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=62470.6
- Funnel: target 834 → liquid 157 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.8 >= 65=1, 4h RSI 86.1 >= 65=1, 4h RSI 75.0 >= 65=1, 4h RSI 75.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +82.81% | $50,898,992.25 |
| HMSTR/USDT:USDT | +80.78% | $9,849,275.02 |
| ANSEM/USDT:USDT | +75.52% | $5,608,679.45 |
| LAB/USDT:USDT | +70.31% | $62,951,267.11 |
| BAS/USDT:USDT | +48.92% | $4,417,527.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +4.93% | +4.95% |
| BTW/USDT:USDT | below_1h_threshold | +4.72% | +4.74% |
| SPX/USDT:USDT | below_1h_threshold | +4.29% | +4.31% |
| M/USDT:USDT | below_1h_threshold | +3.36% | +3.38% |
| MIRA/USDT:USDT | below_1h_threshold | +3.13% | +3.15% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
