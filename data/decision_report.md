# Decision Report

- generated_at: 2026-06-18T07:20:31.267315+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7017**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.39% / filled 20/20。**
- 全期間 MARKET基準: n=7017, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| ASK | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.14% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.15% | **+0.12%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.02% | **+0.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$215.07** / 初期 $100.00 (+115.07%)
- 確定: 1863件 (Win 521 / Loss 591 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $215.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.16** / 初期 $100.00 (+6.16%)
- 確定: 290件 (Win 82 / Loss 77 / Flat 131) / skip 138件
- 成長率目線: 平均log +0.000206 / 幾何平均 +0.021% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0753 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $106.16

## 5. Latest Market Context

- 更新: 2026-06-18T07:20:26.838714+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=64139.1
- Funnel: target 793 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +118.94% | $39,725,785.43 |
| O/USDT:USDT | +71.67% | $3,287,023.09 |
| SYN/USDT:USDT | +64.01% | $5,245,984.66 |
| H/USDT:USDT | +33.73% | $31,504,406.83 |
| HOME/USDT:USDT | +32.53% | $2,067,622.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| O/USDT:USDT | below_1h_threshold | +4.88% | +4.74% |
| HOME/USDT:USDT | below_1h_threshold | +4.08% | +3.95% |
| ALLO/USDT:USDT | below_1h_threshold | +3.21% | +3.07% |
| RIF/USDT:USDT | below_1h_threshold | +2.82% | +2.69% |
| ENA/USDT:USDT | below_1h_threshold | +2.40% | +2.27% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
