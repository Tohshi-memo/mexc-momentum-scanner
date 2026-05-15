# Decision Report

- generated_at: 2026-05-15T07:08:52.821202+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4325**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.40% / filled 20/20。**
- 全期間 MARKET基準: n=4325, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+3.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.40% | **+3.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +3.46% | **+3.46%** |
| MARKET | 20/20 | 100.0% | +3.40% | **+3.40%** |
| LIMIT_1PCT | 16/20 | 80.0% | +3.50% | **+2.80%** |
| LIMIT_2PCT | 13/20 | 65.0% | +3.49% | **+2.27%** |
| LIMIT_ATR | 11/20 | 55.0% | +2.85% | **+1.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.36% | **+0.75%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.42% | **+0.25%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.33% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 44件 (TP 11 / SL 30 / EXP 3)
- 最新: SKYAI/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.42** / 初期 $100.00 (+20.42%)
- 確定: 377件 (Win 97 / Loss 131 / Flat 149) / skip 509件
- 成長率目線: 平均log +0.000493 / 幾何平均 +0.049% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PEAQ/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $120.42

## 4. Latest Market Context

- 更新: 2026-05-15T07:08:49.512112+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=80583.0
- Funnel: target 761 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PEAQ/USDT:USDT | +30.71% | $3,549,965.48 |
| GWEI/USDT:USDT | +26.62% | $1,258,476.14 |
| UP/USDT:USDT | +21.35% | $4,188,128.33 |
| FIGSTOCK/USDT:USDT | +14.05% | $3,183,063.06 |
| TAC/USDT:USDT | +10.74% | $2,200,713.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.98% | +0.93% |
| GUA/USDT:USDT | below_1h_threshold | +0.95% | +0.90% |
| CHIP/USDT:USDT | below_1h_threshold | +0.94% | +0.89% |
| FIGSTOCK/USDT:USDT | below_1h_threshold | +0.75% | +0.70% |
| STAR/USDT:USDT | below_1h_threshold | +0.67% | +0.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
