# Decision Report

- generated_at: 2026-05-29T05:25:14.797003+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5008**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.63% / filled 20/20。**
- 全期間 MARKET基準: n=5008, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.63% | **+1.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.71% | **+1.71%** |
| MARKET | 20/20 | 100.0% | +1.63% | **+1.63%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.36% | **+0.95%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.46% | **+0.88%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.03% | **+0.82%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.97% | **+0.58%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.57% | **+0.23%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.41% | **+0.21%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.37% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.23** / 初期 $100.00 (+28.23%)
- 確定: 730件 (Win 175 / Loss 222 / Flat 333) / skip 839件
- 成長率目線: 平均log +0.000341 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account +0.00% 残高後 $128.23

## 4. Latest Market Context

- 更新: 2026-05-29T05:25:09.251107+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=73520.0
- Funnel: target 777 → liquid 148 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +88.25% | $35,655,737.08 |
| DELLSTOCK/USDT:USDT | +35.74% | $8,058,256.99 |
| CTR/USDT:USDT | +34.44% | $1,152,661.16 |
| AIGENSYN/USDT:USDT | +16.45% | $1,078,637.20 |
| CLO/USDT:USDT | +16.42% | $1,530,388.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_relative_strength | +5.01% | +4.94% |
| INJ/USDT:USDT | below_1h_threshold | +1.92% | +1.85% |
| CTR/USDT:USDT | below_1h_threshold | +1.66% | +1.59% |
| WLD/USDT:USDT | below_1h_threshold | +1.59% | +1.52% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.41% | +1.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
