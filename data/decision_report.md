# Decision Report

- generated_at: 2026-05-22T21:24:14.862013+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4741**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=4741, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_10PCT | 3/20 | 15.0% | +2.30% | **+0.35%** |
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.95% | **+0.88%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.22% | **+0.67%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.57% | **+0.51%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$96.20** / 初期 $100.00 (-3.80%)
- 確定トレード: 61件 (TP 16 / SL 42 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $96.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.43** / 初期 $100.00 (+24.43%)
- 確定: 587件 (Win 149 / Loss 189 / Flat 249) / skip 715件
- 成長率目線: 平均log +0.000372 / 幾何平均 +0.037% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $124.43

## 4. Latest Market Context

- 更新: 2026-05-22T21:24:12.492255+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=75993.3
- Funnel: target 764 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +77.60% | $40,148,332.00 |
| BILL/USDT:USDT | +15.85% | $16,188,097.16 |
| BEAT/USDT:USDT | +7.95% | $41,030,841.36 |
| LAB/USDT:USDT | +4.19% | $28,956,888.59 |
| GUA/USDT:USDT | +3.40% | $1,168,689.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +1.81% | +1.74% |
| BILL/USDT:USDT | below_1h_threshold | +1.75% | +1.68% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.31% | +1.24% |
| BANANAS31/USDT:USDT | below_1h_threshold | +1.25% | +1.18% |
| LAB/USDT:USDT | below_1h_threshold | +0.73% | +0.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
