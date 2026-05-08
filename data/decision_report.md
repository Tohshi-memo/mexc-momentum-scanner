# Decision Report

- generated_at: 2026-05-08T13:27:32.635491+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3785**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.02% / filled 20/20。**
- 全期間 MARKET基準: n=3785, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+2.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.02% | **+2.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.05% | **+2.05%** |
| MARKET | 20/20 | 100.0% | +2.02% | **+2.02%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.48% | **+0.81%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.96% | **+0.77%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +8.00% | **+5.33%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.40% | **+1.20%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.35% | **+0.74%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 26件 (TP 7 / SL 17 / EXP 2)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 155件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T13:27:29.849930+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.44% price=79634.8
- Funnel: target 773 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHAROS/USDT:USDT | +46.43% | $11,727,156.85 |
| BSB/USDT:USDT | +40.39% | $12,067,261.16 |
| PLAY/USDT:USDT | +38.89% | $11,903,882.70 |
| COLLECT/USDT:USDT | +29.79% | $1,090,683.02 |
| AGT/USDT:USDT | +27.43% | $5,829,150.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +2.87% | +3.31% |
| LAB/USDT:USDT | below_1h_threshold | +2.86% | +3.30% |
| GALA/USDT:USDT | below_1h_threshold | +2.34% | +2.78% |
| COLLECT/USDT:USDT | below_1h_threshold | +1.87% | +2.31% |
| CHIP/USDT:USDT | below_1h_threshold | +1.84% | +2.28% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
