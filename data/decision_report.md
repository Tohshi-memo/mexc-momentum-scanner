# Decision Report

- generated_at: 2026-06-02T10:17:16.275360+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5440**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5440, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.87% | **+0.87%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.42% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +1.11% | **+0.33%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +0.05% | **+0.02%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.17% | **-0.03%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.12% | **-0.08%** |
| ASK_LONG | 20/20 | 100.0% | -0.19% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$96.14** / 初期 $100.00 (-3.86%)
- 確定トレード: 85件 (TP 24 / SL 58 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.14
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.97** / 初期 $100.00 (+33.97%)
- 確定: 952件 (Win 224 / Loss 287 / Flat 441) / skip 1049件
- 成長率目線: 平均log +0.000307 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $133.97

## 4. Latest Market Context

- 更新: 2026-06-02T10:17:13.706322+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=69663.8
- Funnel: target 772 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +40.26% | $2,785,330.34 |
| MRVLSTOCK/USDT:USDT | +31.36% | $4,649,551.02 |
| ESPORTS/USDT:USDT | +26.90% | $12,797,561.87 |
| UB/USDT:USDT | +24.63% | $2,921,911.67 |
| USELESS/USDT:USDT | +21.81% | $1,951,139.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.74% | +4.35% |
| MYX/USDT:USDT | below_1h_threshold | +3.03% | +2.64% |
| USELESS/USDT:USDT | below_1h_threshold | +2.99% | +2.60% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +2.56% | +2.17% |
| ICP/USDT:USDT | below_1h_threshold | +2.31% | +1.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
