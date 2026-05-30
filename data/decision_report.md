# Decision Report

- generated_at: 2026-05-30T06:54:43.085348+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5106**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5106, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.90% | **-0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +7.32% | **+1.83%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.85% | **+1.16%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.72% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.76% | **+1.76%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK_LONG | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.69% | **+0.93%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.53% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.00** / 初期 $100.00 (+26.00%)
- 確定: 763件 (Win 177 / Loss 228 / Flat 358) / skip 904件
- 成長率目線: 平均log +0.000303 / 幾何平均 +0.030% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.00

## 4. Latest Market Context

- 更新: 2026-05-30T06:54:40.451964+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=73544.0
- Funnel: target 773 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +72.01% | $13,467,403.40 |
| LAB/USDT:USDT | +22.93% | $130,105,560.17 |
| ID/USDT:USDT | +21.21% | $6,737,559.25 |
| XLM/USDT:USDT | +20.01% | $471,238,499.42 |
| BASED/USDT:USDT | +17.25% | $3,058,033.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +4.16% | +4.19% |
| BEAT/USDT:USDT | below_1h_threshold | +1.69% | +1.72% |
| H/USDT:USDT | below_1h_threshold | +1.54% | +1.57% |
| RAVE/USDT:USDT | below_1h_threshold | +1.44% | +1.48% |
| GRASS/USDT:USDT | below_1h_threshold | +1.22% | +1.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
