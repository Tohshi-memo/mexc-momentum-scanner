# Decision Report

- generated_at: 2026-05-23T10:59:08.458196+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4770**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.71% / filled 20/20。**
- 全期間 MARKET基準: n=4770, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+2.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.71% | **+2.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.71% | **+2.71%** |
| ASK | 20/20 | 100.0% | +2.65% | **+2.65%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.64% | **+1.31%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.55% | **+0.30%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.48% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | -0.32% | **-0.23%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | -0.38% | **-0.32%** |
| MARKET_LONG | 20/20 | 100.0% | -0.34% | **-0.34%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 62件 (TP 17 / SL 42 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +6.60% 残高後 $97.16
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.91** / 初期 $100.00 (+20.91%)
- 確定: 616件 (Win 150 / Loss 195 / Flat 271) / skip 715件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $120.91

## 4. Latest Market Context

- 更新: 2026-05-23T10:59:03.866760+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=74694.9
- Funnel: target 764 → liquid 133 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.0 >= 65=1, 4h RSI 78.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +129.53% | $77,878,901.10 |
| BEAT/USDT:USDT | +24.10% | $69,192,000.30 |
| IN/USDT:USDT | +20.07% | $2,046,406.53 |
| GMTTOKEN/USDT:USDT | +16.87% | $2,694,882.44 |
| BILL/USDT:USDT | +12.25% | $16,953,419.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +2.07% | +1.99% |
| MYX/USDT:USDT | below_1h_threshold | +1.59% | +1.50% |
| SIREN/USDT:USDT | below_1h_threshold | +1.26% | +1.17% |
| GRASS/USDT:USDT | below_1h_threshold | +1.20% | +1.11% |
| VVV/USDT:USDT | below_1h_threshold | +1.00% | +0.91% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
