# Decision Report

- generated_at: 2026-05-29T04:09:50.991166+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5003**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.55% / filled 20/20。**
- 全期間 MARKET基準: n=5003, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.60% | **+1.60%** |
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.44% | **+1.22%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.65% | **+0.45%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.80% | **+0.90%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +1.12% | **+0.67%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.37% | **+0.11%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.08% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.23** / 初期 $100.00 (+28.23%)
- 確定: 729件 (Win 175 / Loss 222 / Flat 332) / skip 835件
- 成長率目線: 平均log +0.000341 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.23

## 4. Latest Market Context

- 更新: 2026-05-29T04:09:48.826754+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=73214.7
- Funnel: target 777 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +70.30% | $31,111,117.01 |
| CLO/USDT:USDT | +34.28% | $1,355,021.46 |
| DELLSTOCK/USDT:USDT | +33.54% | $7,536,403.25 |
| AR/USDT:USDT | +12.11% | $1,753,405.00 |
| AIGENSYN/USDT:USDT | +10.65% | $1,045,712.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SWARMS/USDT:USDT | below_1h_threshold | +1.91% | +1.98% |
| RIVER/USDT:USDT | below_1h_threshold | +1.40% | +1.47% |
| BSB/USDT:USDT | below_1h_threshold | +1.07% | +1.14% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.61% | +0.68% |
| VVV/USDT:USDT | below_1h_threshold | +0.52% | +0.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
