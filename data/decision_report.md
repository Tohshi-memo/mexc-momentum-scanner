# Decision Report

- generated_at: 2026-06-25T23:19:47.593655+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7591**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=7591, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.43% | **+0.04%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -1.73% | **-0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.19% | **+1.07%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.25% | **+0.67%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.80% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$103.17** / 初期 $100.00 (+3.17%)
- 確定トレード: 40件 (TP 15 / SL 24 / EXP 1)
- 最新: DRAM/USDT:USDT EXPIRED PnL +1.79% 残高後 $103.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.24** / 初期 $100.00 (+119.24%)
- 確定: 2132件 (Win 629 / Loss 715 / Flat 788) / skip 2020件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $219.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 377件 (Win 103 / Loss 100 / Flat 174) / skip 625件
- 成長率目線: 平均log +0.000194 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0493 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XPL/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-25T23:19:43.013464+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.41% price=60058.4
- Funnel: target 807 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +15.26% | $1,669,730.68 |
| IP/USDT:USDT | +14.72% | $3,012,628.48 |
| IDOL/USDT:USDT | +12.89% | $1,589,663.15 |
| HEI/USDT:USDT | +12.33% | $6,175,112.08 |
| FOGO/USDT:USDT | +11.29% | $2,613,309.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IP/USDT:USDT | below_1h_threshold | +3.51% | +3.10% |
| AIN/USDT:USDT | below_1h_threshold | +3.34% | +2.93% |
| KORU/USDT:USDT | below_1h_threshold | +2.94% | +2.53% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.56% | +2.15% |
| SOXL/USDT:USDT | below_1h_threshold | +1.97% | +1.56% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
