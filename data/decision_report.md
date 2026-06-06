# Decision Report

- generated_at: 2026-06-06T04:21:13.868348+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5782**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.46% / filled 20/20。**
- 全期間 MARKET基準: n=5782, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.46% | **+2.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.51% | **+2.51%** |
| MARKET | 20/20 | 100.0% | +2.46% | **+2.46%** |
| LIMIT_BB3S | 4/19 | 21.1% | +3.14% | **+0.66%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.22% | **+0.42%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +0.30% | **+0.19%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.00% | **+0.00%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | -0.08% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1012件 (Win 239 / Loss 313 / Flat 460) / skip 1331件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T04:21:11.039233+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.01% price=60050.2
- Funnel: target 771 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HOME/USDT:USDT | +35.79% | $5,480,662.48 |
| VELVET/USDT:USDT | +25.91% | $2,020,914.12 |
| OPN/USDT:USDT | +18.38% | $23,013,265.92 |
| ALLO/USDT:USDT | +17.43% | $8,197,842.70 |
| CLO/USDT:USDT | +15.24% | $1,695,390.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +3.66% | +4.67% |
| SIREN/USDT:USDT | below_1h_threshold | +1.87% | +2.88% |
| ALLO/USDT:USDT | below_1h_threshold | +1.19% | +2.20% |
| VELVET/USDT:USDT | below_1h_threshold | +1.11% | +2.12% |
| HEI/USDT:USDT | below_1h_threshold | +1.09% | +2.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
