# Decision Report

- generated_at: 2026-05-31T10:56:40.055049+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5188**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.12% / filled 20/20。**
- 全期間 MARKET基準: n=5188, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.55% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.13% | **+1.02%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.97% | **+0.83%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.35% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.70** / 初期 $100.00 (+25.70%)
- 確定: 823件 (Win 189 / Loss 246 / Flat 388) / skip 926件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $125.70

## 4. Latest Market Context

- 更新: 2026-05-31T10:56:34.577744+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=73838.7
- Funnel: target 773 → liquid 123 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +47.49% | $5,558,293.24 |
| AIA/USDT:USDT | +36.25% | $2,779,410.49 |
| TA/USDT:USDT | +23.43% | $2,446,223.15 |
| PORTAL/USDT:USDT | +22.88% | $12,257,686.49 |
| HIVE/USDT:USDT | +15.79% | $2,796,427.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.95% | +4.92% |
| HIVE/USDT:USDT | below_1h_threshold | +4.38% | +4.35% |
| PUNDIX/USDT:USDT | below_1h_threshold | +1.64% | +1.61% |
| TA/USDT:USDT | below_1h_threshold | +1.62% | +1.59% |
| RAVE/USDT:USDT | below_1h_threshold | +1.38% | +1.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
