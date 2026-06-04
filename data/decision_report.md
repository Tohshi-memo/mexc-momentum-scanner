# Decision Report

- generated_at: 2026-06-04T11:27:37.372760+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5622**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.20% / filled 20/20。**
- 全期間 MARKET基準: n=5622, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+3.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.20% | **+3.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +3.74% | **+3.74%** |
| MARKET | 20/20 | 100.0% | +3.20% | **+3.20%** |
| LIMIT_1PCT | 14/20 | 70.0% | +2.22% | **+1.55%** |
| LIMIT_2PCT | 12/20 | 60.0% | +2.02% | **+1.21%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.71% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_7PCT_LONG | 13/20 | 65.0% | +0.32% | **+0.21%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -0.65% | **-0.23%** |

## 2. $100 Live Portfolio

- 残高: **$98.55** / 初期 $100.00 (-1.45%)
- 確定トレード: 95件 (TP 29 / SL 63 / EXP 3)
- 最新: OPN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.55
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1006件 (Win 239 / Loss 312 / Flat 455) / skip 1177件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T11:27:34.929620+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=62539.9
- Funnel: target 771 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EPIC/USDT:USDT | +29.22% | $5,891,922.37 |
| OPN/USDT:USDT | +27.72% | $35,238,983.35 |
| SIREN/USDT:USDT | +22.93% | $5,203,377.08 |
| HEI/USDT:USDT | +20.14% | $4,562,365.38 |
| BEAT/USDT:USDT | +11.85% | $17,136,331.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.96% | +3.72% |
| PLAY/USDT:USDT | below_1h_threshold | +2.94% | +2.71% |
| BCH/USDT:USDT | below_1h_threshold | +1.90% | +1.66% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.72% | +1.48% |
| HEI/USDT:USDT | below_1h_threshold | +1.64% | +1.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
