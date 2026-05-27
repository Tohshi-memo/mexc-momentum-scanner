# Decision Report

- generated_at: 2026-05-27T16:38:54.108043+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4932**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.41% / filled 20/20。**
- 全期間 MARKET基準: n=4932, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.45% | **+1.45%** |
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.35% | **+1.22%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.34% | **+1.08%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.92% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.04% | **+0.67%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.02% | **+0.56%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | -0.06% | **-0.03%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$96.67** / 初期 $100.00 (-3.33%)
- 確定トレード: 66件 (TP 18 / SL 45 / EXP 3)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.67
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 684件 (Win 172 / Loss 220 / Flat 292) / skip 809件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-27T16:38:52.429925+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=75050.0
- Funnel: target 774 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +2.53% | $2,082,222.78 |
| PLAY/USDT:USDT | +2.50% | $20,715,474.99 |
| SNDKSTOCK/USDT:USDT | +1.70% | $5,528,488.94 |
| MRVLSTOCK/USDT:USDT | +1.49% | $1,976,965.11 |
| WDCSTOCK/USDT:USDT | +1.46% | $3,610,520.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +2.77% | +3.10% |
| H/USDT:USDT | below_1h_threshold | +2.63% | +2.96% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.70% | +2.03% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.50% | +1.83% |
| WDCSTOCK/USDT:USDT | below_1h_threshold | +1.47% | +1.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
