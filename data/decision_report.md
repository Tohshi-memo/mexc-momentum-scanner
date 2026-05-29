# Decision Report

- generated_at: 2026-05-29T05:29:59.373911+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5010**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=5010, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +0.82% | **+0.65%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.89% | **+0.62%** |
| ASK | 20/20 | 100.0% | +0.57% | **+0.57%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.49% | **+0.44%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.61% | **+0.43%** |
| MARKET_LONG | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.57% | **+0.29%** |
| ASK_LONG | 20/20 | 100.0% | +0.25% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.23** / 初期 $100.00 (+28.23%)
- 確定: 732件 (Win 175 / Loss 222 / Flat 335) / skip 839件
- 成長率目線: 平均log +0.000340 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account +0.00% 残高後 $128.23

## 4. Latest Market Context

- 更新: 2026-05-29T05:29:56.023325+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=73543.6
- Funnel: target 777 → liquid 148 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +96.35% | $36,681,073.17 |
| CTR/USDT:USDT | +36.96% | $1,167,849.52 |
| DELLSTOCK/USDT:USDT | +36.74% | $8,075,121.81 |
| CLO/USDT:USDT | +18.42% | $1,537,836.86 |
| AIGENSYN/USDT:USDT | +16.45% | $1,106,002.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.35% | +4.25% |
| CTR/USDT:USDT | below_1h_threshold | +3.91% | +3.81% |
| GUA/USDT:USDT | below_1h_threshold | +3.65% | +3.55% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.71% | +1.61% |
| WLD/USDT:USDT | below_1h_threshold | +1.69% | +1.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
