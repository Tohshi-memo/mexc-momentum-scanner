# Decision Report

- generated_at: 2026-06-18T07:27:33.032429+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7018**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.99% / filled 20/20。**
- 全期間 MARKET基準: n=7018, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.99% | **+1.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.99% | **+1.99%** |
| ASK | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.46% | **+0.73%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.02% | **+0.01%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.10% | **-0.08%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.74% | **-0.37%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$214.00** / 初期 $100.00 (+114.00%)
- 確定: 1864件 (Win 521 / Loss 592 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $214.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.79** / 初期 $100.00 (+5.79%)
- 確定: 291件 (Win 82 / Loss 78 / Flat 131) / skip 138件
- 成長率目線: 平均log +0.000193 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0693 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.79

## 5. Latest Market Context

- 更新: 2026-06-18T07:27:25.396058+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=64212.1
- Funnel: target 793 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +123.53% | $39,993,761.55 |
| O/USDT:USDT | +72.34% | $3,363,175.60 |
| SYN/USDT:USDT | +58.79% | $5,305,755.35 |
| H/USDT:USDT | +35.39% | $31,591,095.00 |
| HOME/USDT:USDT | +32.30% | $2,091,158.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| O/USDT:USDT | below_relative_strength | +5.10% | +4.85% |
| CLO/USDT:USDT | below_1h_threshold | +4.42% | +4.17% |
| RIF/USDT:USDT | below_1h_threshold | +4.39% | +4.14% |
| ESPORTS/USDT:USDT | below_1h_threshold | +4.11% | +3.86% |
| HOME/USDT:USDT | below_1h_threshold | +3.93% | +3.68% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
