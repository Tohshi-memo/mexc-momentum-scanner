# Decision Report

- generated_at: 2026-07-04T12:48:38.469919+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8262**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8262, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.03% | **+0.41%** |
| LIMIT_6PCT | 4/20 | 20.0% | +2.04% | **+0.41%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.01% | **+0.00%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.24% | **-0.17%** |
| LIMIT_BB3S | 2/18 | 11.1% | -4.00% | **-0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.77% | **+1.77%** |
| MARKET_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.30% | **+0.91%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.06% | **+0.37%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.23% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$331.93** / 初期 $100.00 (+231.93%)
- 確定: 2579件 (Win 815 / Loss 860 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000465 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $331.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1036件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0402 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T12:48:28.328187+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=62571.8
- Funnel: target 834 → liquid 154 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.3 >= 65=1, 4h RSI 90.2 >= 65=1, 4h RSI 85.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +101.41% | $71,247,758.08 |
| ANSEM/USDT:USDT | +85.91% | $5,746,699.39 |
| HMSTR/USDT:USDT | +71.99% | $11,540,325.76 |
| TLM/USDT:USDT | +71.22% | $54,294,247.55 |
| BAS/USDT:USDT | +47.06% | $4,567,182.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_relative_strength | +5.06% | +4.88% |
| MIRA/USDT:USDT | below_1h_threshold | +4.58% | +4.40% |
| BTW/USDT:USDT | below_1h_threshold | +4.17% | +3.98% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.27% | +3.09% |
| BAS/USDT:USDT | below_1h_threshold | +2.31% | +2.13% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
