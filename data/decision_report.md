# Decision Report

- generated_at: 2026-05-09T08:32:43.863399+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3867**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.67% / filled 20/20。**
- 全期間 MARKET基準: n=3867, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.93% | **+0.93%** |
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.08% | **+0.22%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.11% | **+0.08%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.05% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +0.35% | **+0.29%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.29% | **+0.25%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.26% | **+0.09%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定トレード: 29件 (TP 7 / SL 19 / EXP 3)
- 最新: LUNC/USDT:USDT EXPIRED PnL +3.11% 残高後 $98.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 194件 (Win 48 / Loss 64 / Flat 82) / skip 234件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T08:32:41.001286+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=80377.5
- Funnel: target 767 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYM/USDT:USDT | +31.49% | $2,998,772.14 |
| PHAROS/USDT:USDT | +22.88% | $16,509,068.12 |
| ZEREBRO/USDT:USDT | +22.01% | $1,681,180.70 |
| SAHARA/USDT:USDT | +19.51% | $1,493,523.63 |
| CORE/USDT:USDT | +18.42% | $2,993,624.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAHARA/USDT:USDT | below_relative_strength | +5.02% | +4.78% |
| RAVE/USDT:USDT | below_1h_threshold | +4.21% | +3.97% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.55% | +3.31% |
| BILL/USDT:USDT | below_1h_threshold | +3.10% | +2.86% |
| AGT/USDT:USDT | below_1h_threshold | +2.46% | +2.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
